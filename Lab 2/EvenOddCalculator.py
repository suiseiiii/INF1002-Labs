r'''
Task Description:
In this task, you are assigned to develop one program to help users calculate 
different information based a series of user provided numbers (integers). 
Detailed requirement is provided as follows: 

Input: A series of numbers 
Output: (Your output should be in one line)
	. The summation of the even numbers and summation of the odd numbers in 
       the input list 
	. The difference between the biggest and smallest numbers in the input list
	. The count of even numbers and odd numbers in the input list
	. The "centered" average of the list of integers. The centered average can be 
       calculated as the mean average of the values, after removing the largest and 
       smallest values in the array. If there are multiple copies of the smallest 
       value, ignore all but keep just one copy, and likewise for the largest value. 
       For instance, [12,2,8,7,100] -> 9; [2,2,8,11,100] -> 7

To have a better understanding of the loops, please try to implement 
two programs: one uses "for" and another uses "while" loop.

Running Examples:

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 12,2,8,7,100
The sum of all even numbers is 122, the sum of all odd numbers is 7, the difference between the biggest and smallest number is 98, the total number of even numbers is 4, the total number of odd numbers is 1, the centered average is 9.

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 1,2,abcd,8,11,200,301
Please enter valid integers.
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def EvenOddCalculator():
     
       try:
             numbers = sys.argv[1]
             numbers_list = [int(num) for num in numbers.split(',')]
             numbers_list = sorted(numbers_list)
       except ValueError:
            print('Please enter valid integers.')
            return
       
       even = 0
       even_count = 0
       odd = 0
       odd_count = 0

       # sums of all even/odd numbers and their counts
       for num in numbers_list:
              if num % 2 == 0:
                 even += num
                 even_count += 1
              else:
                 odd += num
                 odd_count += 1

       # difference between biggest and smallest
       smallest = min(numbers_list)
       biggest = max(numbers_list)
       difference = biggest - smallest

       # removes biggest and smallest numbers and their remaining duplicates if any
       sorted_list = numbers_list[1:-1]
       if smallest in sorted_list:
              while smallest in sorted_list:
                     sorted_list.remove(smallest)
              sorted_list.append(smallest)
       if biggest in sorted_list:
              while biggest in sorted_list:
                     sorted_list.remove(biggest)
              sorted_list.append(biggest)

       centered_average = sum(sorted_list) // len(sorted_list)
       
       print(f"The sum of all even numbers is {even}, the sum of all odd numbers is {odd}, the difference between the biggest and smallest number is {difference}, the total number of even numbers is {even_count}, the total number of odd numbers is {odd_count}, the centered average is {centered_average}.")


if __name__=='__main__':
      EvenOddCalculator()
      
