r'''
Task Description:
In this task, you are going to design one program to check the popular characters
in a given string. You need to write one program to calculate the top 5 most 
frequent characters. The following are some hints that may help you design this program. 
	. String has a cool function that you can use to return a copy of the string 
     in which all case-based characters have been lowercased. 
	. To get the top 5 most frequent characters after sorting them, you need to 
     extract all the characters first and figure out one way to calculate the frequency 
     of each character. Then select the top 5 characters. 
	. The output must in the descending order of character frequency. If there are 
     characters with the same frequency, they must be printed in ascending ASCII order.
	. Print out the top 5 characters and their counts in the screen. (Your output should be in one line)

Running Examples:
C:\INF1002\Lab2\CountPopularChars>python CountPopularChars.py sdsERwweYxcxeewHJesddsdskjjkjrFGe21DS2145o9003gDDS
d:7,s:7,e:6,j:4,w:3
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def CountPopularChars():

     # converts all characters in the string to lower case
     chars = sys.argv[1].lower()
     chars_dict = {}

     # counts number of characters in input. if it is the first time a character is seen, counter is set to 1. if it is not the first time, counter is incremented by 1
     for char in chars:
          if char not in chars_dict:
                 chars_dict[char] = 1
          elif char in chars_dict:
                chars_dict[char] += 1
     
     # sorts the dict in descending order
     chars_dict = dict(sorted(chars_dict.items(), key=lambda char:char[0]))
     sorted_chars_dict = sorted(chars_dict.items(), key = lambda count:count[1], reverse=True)
     sorted_chars_dict = sorted_chars_dict[:5]
     result = ','.join(f"{char}:{count}" for char, count in sorted_chars_dict)
     
     print(result)

if __name__=='__main__':
      CountPopularChars()
      
