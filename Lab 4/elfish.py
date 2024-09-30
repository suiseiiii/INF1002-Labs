r'''
Task Description: 
     A word is considered elfish if it contains the letters: e, l and f in it, in any 
     order. For instance, we would say that the following words are elfish: tasteful, 
     whiteleaf, unfriendly and waffles, because they each contain those letters. Use 
     the recursive function to implement this. Write one program to call your recursive 
     function and tell the user whether the input word is one elfish or not. 
     
     HINT: You can recursively reduce both the elfish letters and input word. 
     The sample executions are provided as follows:

Note: 
     Your output should be in ONE line

Running example: 
     C:\INF1002\Lab4\elfish> python elfish.py waffles
     waffles is one elfish word!

     C:\INF1002\Lab4\elfish> python elfish.py instance
     instance is not an elfish word!
'''

import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

def elfish():
     string = sys.argv[1]
     elf = ['e','l','f']
     check = check_elfish(elf, string)
     if check:
          print(f'{string} is one elfish word!')
     else:
          print(f'{string} is not an elfish word!')
     
def check_elfish(letters, word):
     if not letters:
          return True
     elif len(word) == 0:
          return False
     elif word[0] in letters:
          letters.remove(word[0])
     word = word[1:]
     return check_elfish(letters, word)
          

if __name__=='__main__':
     elfish()
      
