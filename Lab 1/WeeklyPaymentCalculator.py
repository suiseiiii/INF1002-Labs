'''
Task Description:
Develop one employee weekly payment calculation program as we have discussed in 
Lecture 2. The program requirement is as follows: 
1.	Allow users to run your program with three input arguments by passing three
    values to the program:  the number of working hours, input normal rate and 
    input the overtime rate.

2.	Your program will read the three arguments and calculate the users salary 
    using the following two formulas:
        a.	Payment of the normal hours = normal rate * normal hours
        b.	Payment of the overtime hours = overtime rate * overtime hours
        NOTE: the working hours within 40 belong to normal hours and those beyond 
              40 hours are considered as overtime hours. 

3.	After user inputs all the numbers, if the input numbers are invalid, you need 
    to present an error message "Your input is invalid!". Otherwise, you need to 
    print out the employee's payment of normal hours, his payment of overtime 
    hours and total payment. The output payment requires to have 2 precisions. 
    For instance, if payment is 2300.456, it should print 2300.45. 
    If payment is 2300, it should print 2300.00.
      
NOTE: You have to strictly follow the input and output format. 

Running example:
Assume your program is named as WeeklyPaymentCalculator.py. Example output is as follows: 

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 20 30 100
Normal Salary:600.00, Extra Salary:0.00, Total Salary:600.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 60 30 200
Normal Salary:1200.00, Extra Salary:4000.00, Total Salary:5200.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 10000 10 200
Your input is invalid!

'''
import sys
# write your code here
def WeeklyPaymentCalculator():
    
    working_hours = 0
    normal_rate = 0
    overtime_rate = 0
    overtime_hours = 0
    normal_salary = 0
    extra_salary = 0
    total_salary = 0
    # max hours in a week (7 days 24 hours)
    max_hours = 7 * 24

    # check that exactly 3 inputs (working hours, normal rate, overtime rate) are passed through
    if len(sys.argv) != 4:
        print('Your input is invalid!')
        return

    # check if values are valid inputs (numbers)
    # program will exit if not
    try:
        working_hours = float(sys.argv[1])
        normal_rate = float(sys.argv[2])
        overtime_rate = float(sys.argv[3])
    except ValueError:
        print('Your input is invalid!')
        return

    # makre sure working hours is valid (within max hours of a week and not negative)
    if working_hours > max_hours or working_hours < 0:
        print('Your input is invalid!')
        return

    # calculate overtime hours
    # set working hours to 40 for future calculations
    if working_hours > 40:
        overtime_hours = working_hours - 40
        working_hours = 40

    # calculate salary
    normal_salary =  working_hours * normal_rate
    extra_salary = overtime_hours * overtime_rate
    total_salary = normal_salary + extra_salary

    print('Normal Salary: % 0.2f'%normal_salary + ', Extra Salary:%0.2f' % extra_salary + ', Total Salary:%0.2f' % total_salary)

    


if __name__=='__main__':
    WeeklyPaymentCalculator()
    
