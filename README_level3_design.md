# challenges-Mohamed1999777
# level3_design  Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. 

The values are assigned to the input port as arandom value 
    
    for i in range(10):
        A = f'{random.getrandbits(32):=032b}'
        B = f'{random.getrandbits(32):=032b}'


The assert statement is used for comparing the  outut to the expected value.

The following error is seen:

![level3_design_bug](https://user-images.githubusercontent.com/100050717/182199012-e4d6f744-56e5-47ec-babc-ba3a821dcd5f.PNG)

## Test Scenario *(Important)*
- A  =  52855.671966552734 
- B  = -39019.27978515625 
- model[Expected out]       =  13836.392181396484 
- DUT[result from module]   = -13836.392181396484


Output mismatches for the above inputs proving that there is a design bug

## Design Bug
The design has the following bugs

* There is a problem in the sign of the result
* The bug habbens when A is bigger than B and A is positive and B is negative , the result is correct but the sign isn't correct
 
## Verification Strategy
 The input data is randomised 
 all selection lines were tested 
## Is the verification complete ?
 Yes
