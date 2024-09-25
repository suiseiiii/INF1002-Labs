r'''
Task Description:
      In this task, you are going to develop a letter game to count the number of leters
      in the given string.
      Step1:
            Write one functon leter_count(str) that take in one word and returns a dictonary 
            with the frequency counts of the various letters. Upper and lower-case characters 
            are different characters.
            Sample executon:
                  >>leter_count('This')
                  { 'h':1, 'T':1, 'i':1, 's':1}
                  >>le􀆩er_count('Thisisit')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
      Step 2:
            Write one functon double_count(str1, str2) that takes in two words and returns a 
            dictonary with the frequency counts of the various le􀆩ers. Upper and lower-case 
            characters are different characters.
            Sample executon:
                  >> double_count('This', 'isit')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
      Step 3:
            Write one functon various_count(*str) that takes in any number of words and returns 
            a dictonary with the frequency counts of the various le􀆩ers. Upper and lower-case 
            characters are different characters.
            Sample execu􀆟on:
                  >> various_count('This')
                  { 'h':1, 'T':1, 'i':1, 's':1}
                  >> various_count('This', 'isit')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
                  >> various_count('This', 'is, 'it')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
            HINT: In Python, using “def func(*str): list1=str”, list1 can obtain any number of 
            arguments and stores it as a list. You can further get each element from the list 
            and count each word independently. You can implement another func􀆟on to merge two 
            dictonaries. 
            Below is an example:
                  >> def str1(*str)
                        list = str
                        print list
                  >> str1('This', 'is', 'so', 'cool')
                  ('This', 'is', 'so', 'cool')

      Step 4:
            Write one program to allow users to input different number of words and output each
            character's frequency.
            Some of codes read as follows. Please print your results in the characters' ASCII 
            descending order according to this format:

            for item in sorted_total:
            print ('%s:%d' % (item, total[item]), end=' ')

            Note that the following running example is in ONE line, and your output should be in ONE line.

      Running example:
      C:\INF1002\Lab3\CountingLetters>python CountLetters.py Firefox,is,having,trouble,recovering,your,windows,and,tabs
      y:1 x:1 w:2 v:2 u:2 t:2

'''
import sys

# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

#1
def letter_count(tmpStr):

      letter_dict = {}
      for letter in tmpStr:
            if letter.isalpha():
                  if letter not in letter_dict:
                        letter_dict[letter] = 1
                  elif letter in letter_dict:
                        letter_dict[letter] += 1

      return letter_dict

#2 this function, there are two input arguments: two strings
def double_count(str1, str2):
      
      str3 = str1 + str2
      return letter_count(str3)

#3 This one takes only one input arguments
def various_counts(*tmpStr):
      
      str_list = tmpStr
      total_str = ''
      for str in str_list:
            total_str += str

      return letter_count(total_str)
      

def CountLetters():
      
      str = sys.argv[1]
      str_dict = various_counts(str)
      total = dict(sorted(str_dict.items(), key=lambda char:sum(map(ord, char[0])), reverse = True))
      for item in total:
            print ('%s:%d' % (item, total[item]), end=' ')

if __name__=='__main__':
      CountLetters()
      



