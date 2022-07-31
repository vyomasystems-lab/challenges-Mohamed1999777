# challenges-Mohamed1999777
# level1_design1  Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. 

The values are assigned to the input port as arandom value from 0 to 2 to all 32 mux 
  


then a for loop to change select line from 0 to 31 


  
    for SEL in range(30):
     
     dut.sel.value = SEL

     await Timer(2, units='ns')


The assert statement is used for comparing the  outut to the expected value.

The following error is seen:

![level1_1](https://user-images.githubusercontent.com/100050717/182035514-dada4c56-6462-4cf5-8862-843cd794575f.PNG)

## Test Scenario *(Important)*
- Test Inputs: SEL = 13 
- Expected Output: out=1
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
The design has the following bugs 
* SEL=12 isn't included so whenever selection line is 12 the output is the default value = 0 
* SEL=13 is repeated for both selection line values = 12 and 13 so the output when the selection line is 13 is ambiguious and the simulator choosed the input 12  

## Design Fix
Updating the design and re-running the test makes the test pass.

## Verification Strategy
 The input data is randomised 
 all selection lines were tested 
## Is the verification complete ?
 Yes
