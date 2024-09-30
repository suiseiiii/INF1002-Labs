r'''
Task Description: 
      In this task, we need to design one recursive function digit_recursive(x) to 
      calculate how many digits a positive number has. For instance, 10 has two 
      digits, and 122 has three digits, and 5679 has four digits. HINT: The number 
      of digits can be calculated by repeatedly dividing by 10 (without keeping the 
      remainder) until the number is less than 10. 

      Please write another function digit_iterative(x) to achieve the same 
      functionality to calculate the number of the digits of x but uses while loop. 
      Write one main program to allow users to input one number and call these two 
      functions to evaluate the output.

      The example executions are shown as follows: 
      
Note: 
      Your output should be in ONE line

Running example:
      C:\INF1002\Lab4\CountDigits> python CountDigits.py 789
      The number of digit(s) calculated by recursive is 3 and by iterative is 3.
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

def digit_recursive(x):
      x = int(x)
      if x > 10:
            return 1 + digit_recursive(x // 10)
      else:
            return 1
 
def digit_iterative(x):
      digits = 0
      x = int(x)
      while x > 0:
            digits += 1
            x = x // 10
      return digits

def CountDigits():
      num = sys.argv[1]
      recursive_digits = digit_recursive(num)
      iterative_digits = digit_iterative(num)
      print(f'The number of digit(s) calculated by recursive is {recursive_digits} and by iterative is {iterative_digits}.')


if __name__=='__main__':
      CountDigits()
      



