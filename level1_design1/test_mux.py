# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
   #"""Test for adding 2 random numbers multiple times"""
        IN0 = 0
        IN1 = 1
        IN2 = 2
        IN3 = 3 
        IN4 = 0
        IN5 = 1
        IN6 = 2
        IN7 = 3
        IN8 = 0
        IN9 = 1
        IN10 = 2
        IN11 = 3
        IN12 = 0
        IN13 = 1
        IN14 = 2
        IN15 = 3
        IN16 = 0
        IN17 = 1
        IN18 = 2
        IN19 = 3
        IN20 = 0  
        IN21 = 1
        IN22 = 2
        IN23 = 3
        IN24 = 0
        IN25 = 1
        IN26 = 2
        IN27 = 3
        IN28 = 0
        IN29 = 1
        IN30 = 2 

 dut.inp0.value  = IN0
 dut.inp1.value  = IN1 
 dut.inp2.value  = IN2 
 dut.inp3.value  = IN3 
 dut.inp4.value  = IN4 
 dut.inp5.value  = IN5 
 dut.inp6.value  = IN6 
 dut.inp7.value  = IN7 
 dut.inp8.value  = IN8  
 dut.inp9.value  = IN9 
 dut.inp10.value = IN10
 dut.inp11.value = IN11
 dut.inp12.value = IN12
 dut.inp13.value = IN13
 dut.inp14.value = IN14
 dut.inp15.value = IN15
 dut.inp16.value = IN16
 dut.inp17.value = IN17
 dut.inp18.value = IN18
 dut.inp19.value = IN19
 dut.inp20.value = IN20
 dut.inp21.value = IN21
 dut.inp22.value = IN22
 dut.inp23.value = IN23
 dut.inp24.value = IN24
 dut.inp25.value = IN25
 dut.inp26.value = IN26
 dut.inp27.value = IN27
 dut.inp28.value = IN28
 dut.inp29.value = IN29
 dut.inp30.value = IN30
  Arr_in=[ IN0, IN1, IN2, IN3, IN4, IN5, IN6, IN7, IN8, IN9, IN10, IN11, IN12, IN13, IN14, IN15, IN16, IN17, IN18, IN19, IN20, IN21, IN22, IN23, IN24, IN25, IN26, IN27, IN28, IN29, IN30 ]  
    for SEL in range(32):

        #SEL = random.randint(0, 32)


        dut.sel.value = SEL

        await Timer(2, units='ns')
        
        cocotb.log.info(f'SEL={SEL:05} model={Arr_in[SEL]:02}  DUT={int(dut.out.value):02}')
        assert dut.out.value == Arr_in[SEL], "Randomised test failed with:Arr_in{SEL}".format(
            SEL=dut.sel.value)
            #  cocotb.log.info('##### CTB: Develop your test here ########')dut._log.info
