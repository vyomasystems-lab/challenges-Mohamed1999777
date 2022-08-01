# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

# Simple tests for an adder module
import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock
# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1)


@cocotb.test()
async def test_modules(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(5):

        A = f'{random.getrandbits(32):=032b}'
        B = f'{random.getrandbits(32):=032b}'

        dut.a.value = A
        dut.b.value = B

        int_A = A[1:17]
        int_B = B[1:17]

        float_A =  A[17:32]
        float_B =  B[17:32]

        sign_A= A[0]
        sign_B= B[0]

        x_int= int(int_A,2)
        y_int= int(int_B,2)

        x_float = int(float_A,2)/(2**15)
        y_float = int(float_B,2)/(2**15)

        x = x_int + x_float
        y = y_int + y_float
        if sign_A == 1:
            x = x * -1
        else:
            x = x

        if sign_B == 1:
            y = y * -1
        else:
            y = y

        model_result = x + y

        await Timer(2, units='ns')
        
        dut_32 = dut.c.value
        sign_dut = dut_32[0]
        int_dut = dut_32[1:17]
        float_dut = dut_32 [17:32]
        dut_res_int = int(int_dut,2)
        dut_res_float= int(float_dut,2)/(2**15)
        dut_res = dut_res_int + dut_res_float

        if sign_dut == 1:
            dut_res = dut_res * -1
        else:
            dut_res = dut_res

        dut._log.info(f'A={x} B={y} model={model_result} DUT={dut_res}')
        assert ddut_res == model_result, "Randomised test failed with: {X} + {Y} = {Z}".format(
            X=x, Y=y, Z=dut_resma)

