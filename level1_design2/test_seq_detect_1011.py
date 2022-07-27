# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    IN = [ 1, 0, 1, 1 ] 

    # input driving
    #dut.inp_bit.value = IN


    #await Timer(2, units='ns')
    for i in range(4):
        await RisingEdge(dut.clk)
        dut.inp_bit.value = IN[i]
        await FallingEdge(dut.clk)
        print ("current state = ",dut.current_state.value)            




    assert dut.seq_seen.value == 1, f"Sequence detector result is incorrect: {dut.seq_seen.value} != 1"
    #cocotb.log.info('#### CTB: Develop your test here! ######')
