level1_design2 Verification

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.
Verification Environment

The CoCoTb based Python test is developed as explained.

The values are assigned to the input port as an array

then a for loop to assign the input [inp_bit] from 0 to the length of array
    
    IN = [ 1, 0, 0 ,1 , 1 ,0 , 1, 1 ] 
    for i in range(0,len(IN)):
        await RisingEdge(dut.clk)
        dut.inp_bit.value = IN[i]
        await FallingEdge(dut.clk)

The assert statement is used for comparing the outut to the expected value.

The following error is seen:
![level1_2](https://user-images.githubusercontent.com/100050717/182043816-0669eb53-1298-4f0f-b9ea-13b5e1520fc3.PNG)
Test Scenario (Important)

    test_IN = [ 1, 0, 0 ,1 , 1 ,0 , 1, 1 ] 
    Expected Output: out=1
    Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug
Design Bug

The design has the following bugs

The design does't support non-sequence overlapping

Verification Strategy

The input data is randomised all selection lines were tested
Is the verification complete ?

Yes
