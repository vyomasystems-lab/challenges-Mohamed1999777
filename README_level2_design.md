# Level2_design Verification

The verification environment is setup using ![image](https://user-images.githubusercontent.com/100050717/182041595-fe527e9d-01b2-41fb-8894-438dfa688dd1.png)
 provided for the hackathon.

## Verification Environment


A based Python test is developed.

The values are assigned to the input port using random generated data to sources inputs 1, 2, and 3 
  
        mav_putvalue_src1 = random.randint(0, (2**32)-1)
        mav_putvalue_src2 = random.randint(0, (2**32)-1)
        mav_putvalue_src3 = random.randint(0, (2**32)-1)

then a for loop to verify all instructions. A python dictionary stores all instructions keys are instruction and value is its corresponding binary representation


  

for x in instructions:
        mav_putvalue_instr = instructions[x]


The assert statement is used for comparing the  outut to the expected value.

## The following error is seen:
![level2](https://user-images.githubusercontent.com/100050717/182041448-737f5273-57eb-493f-8f14-6db1e2d74188.PNG)
## Test Scenario *(Important)*
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x5
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x40007033
- Test Inputs: DUT instruction = ANDN ( 0x40007033 ) 
- Expected Output:              0x1
- Observed Output in the DUT:   0xb

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
The design has the following bugs 
* ANDN instruction output doesn't match ANDN model output  


## Verification Strategy
 The input data is randomised 
 all instructions  were tested 
## Is the verification complete ?
  More direct test for the corner cases of sources operands need to be done
