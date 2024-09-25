'''
Task Description:
In this task, we develop a Body Mass Index (BMI) Calculator that can be used to 
calculate your BMI value and weight status while taking your age into 
consideration. Use the "metric units" tab if you are more comfortable with the 
international standard metric units. The referenced weight range and calculation 
formula is listed below.

The program requirement is as follows:
1. Allow users to run your program with three input arguments by passing three 
   values to the program: the choice of units, height, and weight.

2. Your program will read the three arguments and calculate BMI using the 
   following two formulas:
    BMI = weight(kg)/height2(m2) (Metric Units)
    BMI = 703 * weight(lb)/height2(in2) (Imperial (U.S.) Units)
    NOTE: The formulas to calculate BMI are based on two of the most used unit 
          systems.

3. After user inputs all the numbers, if the input numbers are invalid, you need 
   to present an error message "Your input is invalid!". Otherwise, you need to 
   print out BMI and category. The output payment requires to have 2 precisions. 
   For instance, if BMI is 23.456, it should print 23.46. If BMI is 23, it should 
   print 23.00.

Reference:
Your BMI is a measurement of your body weight based on your height and weight. 
Although your BMI does not actually "measure" your percentage of body fat, it is a 
useful tool to estimate a healthy body weight based on your height. Due to its ease 
of measurement and calculation, it is the most widely used diagnostic indicator to 
identify a person's optimal weight depending on his height. Your BMI "number" will 
inform you if you are underweight, of normal weight, overweight, or obese. However, 
due to the wide variety of body types, the distribution of muscle and bone mass, etc., 
it is not appropriate to use this as the only or final indication for diagnosis.

BMI Table for Adults:
This is the World Health Organization's (WHO) recommended body weight based on BMI 
values for adults. It is used for both men and women, age 18 or older.
______________________________________
|Category         | BMI range - kg/m2|
|____________________________________|
|Severe Thinness  | <= 16            |
|Moderate Thinness| >16 - 17         |
|Mild Thinness    | >17 - 18.5       |
|Normal           | >18.5 - 25       |
|Overweight       | >25 - 30         |
|Obese Class I    | >30 - 35         |
|Obese Class II   | >35 - 40         |
|Obese Class III  | >40              |
|____________________________________|

NOTE: You must strictly follow the input and output format.
Example output is as follows. Note that '%0.2f\tSevere Thinness' should be used.

Running example:
C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py metric 1.80 78
24.07 Normal

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py metric 1.78 48
15.15 Severe Thinness

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py metric 1.60 126
49.22 Obese Class III

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py imperial 68.90 154.32
22.85 Normal

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py imperial 85.63 135.68
13.01 Severe Thinness

C:\INF1002\Lab1\AverageCalculator> python BMICalculator.py abc
Your input is invalid!
'''
import sys
# write your code here
def BMICalculator():

    bmi = 0
    bmi_range = ''
    height = 0
    weight = 0

    # check that exactly 3 inputs (unit system, height, weight) are passed through
    if len(sys.argv) != 4:
        print('Your input is invalid!')
        return
    
    unit = sys.argv[1]
    # check if unit system is valid (metric or imperial)
    if unit.lower() != 'metric' and unit.lower() != 'imperial':
        print('Your input is invalid!')
        return
    
    # check if height and weight are valid inputs (numbers)
    # program will exit if not
    try:
        height = float(sys.argv[2])
        weight = float(sys.argv[3])
    except ValueError:
        print('Your input is invalid!')
        return

    # use formula depending on unit system
    if unit.lower() == 'metric':
        bmi = weight/(height**2)
        
    elif unit.lower() == 'imperial':
        bmi = 703 * (weight/(height**2))

    # assign bmi range
    if bmi <= 16:
        bmi_range = '\tSevere Thinness'
    elif bmi <= 17:
        bmi_range = '\tModerate Thinness'
    elif bmi <= 18.5:
        bmi_range = '\tMild Thinness'
    elif bmi <= 25:
        bmi_range = '\tNormal'
    elif bmi <= 30:
        bmi_range = '\tOverweight'
    elif bmi <= 35:
        bmi_range = '\tObese Class I'
    elif bmi <= 40:
        bmi_range = '\tObese Class II'
    elif bmi > 40:
        bmi_range = '\tObese Class III'
        
    print('%0.2f'%bmi,bmi_range)
        

if __name__=='__main__':
    BMICalculator()
    
