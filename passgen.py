import os
import random
import pyperclip as pc
from letters import alphabets,numbers,symbols

def getUpperAlpha(alpha):
  x=[]
  for i in range(1,4):
    x.append(random.choice(alpha).upper())
  return x

def getLowerAlpha(alpha):
  x=[]
  for i in range(1,5):
    x.append(random.choice(alpha).lower())
  return x

def getNumbers(alpha):
  x=[]
  for i in range(1,3):
    x.append(str(random.choice(alpha)))
  return x

def getSymbols(alpha):
  x=[]
  x.append(str(random.choice(alpha)))
  return x

gUA = getUpperAlpha(alphabets)
gLA = getLowerAlpha(alphabets)
gNs = getNumbers(numbers)
gSs = getSymbols(symbols)
final_list = gUA+gLA+gNs+gSs
random.shuffle(final_list)
random.shuffle(final_list)
str1 = ''.join(final_list)
pc.copy(str1)
ans="Generated a new password for you: "+str1
ans1="Copied to clipboard ☑️"
print('\n',ans.center(os.get_terminal_size().columns),ans1.center(os.get_terminal_size().columns))
