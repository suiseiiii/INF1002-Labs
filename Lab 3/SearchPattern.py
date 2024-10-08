r'''
Task Description:
     In this task you will write a program that reads two sequences of numbers. 
     The first sequence of numbers is called candidate, and the second sequence of 
     numbers is called pa􀆩ern. Your program will determine if the pa􀆩ern is found 
     entirely in the candidate. To be considered found entirely, all elements of 
     pattern must be in the candidate sequence a consecu􀆟ve positions. You must 
     output the number of found patterns, or 0 if the pattern is not found in 
     the candidate.

     Input: 
          Allow the users to input two sequences, the first sequence is the candidate, 
          and the second sequence is the pattern.
     Output: 
          The number of pattern sequence appearing in the candidate sequence (in ONE line).

     Running Example:
     C:\INF1002\Lab3\PatternSearching>python SearchPattern.py 1,2,3,1,2 1,2
     Pattern appears 2 time!
'''

import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def SearchPattern():
     
     try:
          candidate = sys.argv[1]
          pattern = sys.argv[2]
          print(f'Pattern appears {candidate.count(pattern)} time!')
     except ValueError:
          return

if __name__=='__main__':
     SearchPattern()
      
