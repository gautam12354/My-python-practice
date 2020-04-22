
# https://developers.google.com/machine-learning/guides/text-classification
#https://hackernoon.com/tagged/python          --> Best
# https://www.programiz.com                            Almost everything
# https://python.doctor/page-apprendre-variables-debutant-python
#https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/
#https://data-flair.training/blogs/features-of-python/
#http://pythontutor.com/visualize.html#mode=display                               *********Best way to understand
#https://www.udemy.com/pythonautomation/   check this course
#https://github.com/codingforentrepreneurs/30-Days-of-Python
#https://www.pythonforbeginners.com/games/
#http://pythontutor.com/
#Virtual environments
# Python programs can be stopped at any time by pressing Ctrl-C (on Windows) or Ctrl-D (on Mac and Linux)
# https://pynative.com/print-pattern-python-examples/
# https://hackernoon.com/tired-of-bookmarking-pages-scrap-it-instead-b398622f77d
# https://www.howtogeek.com/113439/how-to-change-your-browsers-user-agent-without-installing-any-extensions/
# https://hackernoon.com/how-to-scrape-a-website-without-getting-blacklisted-271a605a0d94
# https://www.w3resource.com/
# https://www.python.org/dev/peps/pep-0008/#class-names
# https://data-flair.training/blogs/artificial-intelligence-vs-machine-learning-vs-dl-vs-ds/


#comment
#( ''' or """ ) this is called Docstring

#Virtual enviroment for specific project
>>>python -m venv my-project
>>>source my-project/bin/activate
>>>pip install all-the-modules 

#install package from .whl file
#WEBSITE FOR .WHL FILE OF ALL PACKAGES: https://www.lfd.uci.edu/~gohlke/pythonlibs/
>>>pip install C:/some-dir/some-file.whl        #some-file.whl is a file in some location in computer      

#_____________________#
#chr() in Python
#The chr() method returns a string representing a character whose Unicode code point is an integer.
#The chr() method takes only one integer as argument.
print(chr(71), chr(97), chr(117), chr(116), chr(97), chr(109)) 

#clear Screen in Command window
>>>import os
>>>os.system("cls")

#To know path in python shell where you are
>>>import os
>>>os.getcwd()


# Change directory 
>>>os.chdir("/path/to/your/folder")

# List all files and directories in current directory
>>>os.listdir('.')

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   PRINT FUNCTION  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# it display values to the screen

>>>fruit = 'apple'
>>>print(fruit)
'apple'
>>>print('orange')
orange

# Print Two statement at once
>>>print(“Hi”) ; print(“Hello”)
Hi
Hello

>>>print(True==True)
True

>>>print(True!=True)
False

>>>print(not True is True)
False
>>>print(not True is not True)
True

>>>print(100-32 == 68)
True

>>>print(10**2 is 100)
True

>>> print((1, 2) + (3, 4))
(1, 2, 3, 4)

>>> print(1,000,000)
1 0 0   

>>>print(1_000_000)
1000000

>>>print(000000000)
0

#_____________________#
#The sep separator is used between the values. It defaults into a space character.
#After all values are printed, end is printed.
>>>print(1, 2, 3, sep=' < ')
1 < 2 < 3

>>>print(1, 2, 3, sep=' , ')
1 , 2 , 3

>>>print(1, 2, 3,sep='\n')
1
2
3

#printing 3 different values
>>> print('Hi', 'hello world', 'bye bye')
Hi hello world bye bye

#New line with print function
>>>s = 'First line.\nSecond line.'                      # \n means newline
>>>s                                                    # without print(), \n is included in the output
'First line.\nSecond line.'

>>> print(s)                                          # with print(), \n produces a new line
First line.
Second line.

>>> print('C:some\name')                      # here \n means newline!
C:some
ame

>>>len(s)              #Inbuild length function for the string length
24

# Search for a character inside a list 
print(any("a" in word for word in ["apple", "absolutely", "application"]))


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Format !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Format method --> to replace string in 

# .format can be used to format strings, like this:
"{} can be {}".format("Strings", "interpolated")             # => "Strings can be interpolated"
-->'Strings can be interpolated'

# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")  
-->"Bob wants to eat lasagna"

#The String format() Method
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))    
We are the knights who say "Ni!"

# on specific position
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

#no need to convert in string for a number
>>>version =3
>>>print('I love python {}.'.format(version))
I love python 3.

#formate Specification
#Formating String Alignment
< Left  --> if not specify then it is considered
^ Center
> Right
>>>print('{0:8} | {1:<8}'.format('fruit','Quantity'))    #first formate range for first element second for second 
fruit    | Quantity
>>>print('{0:8} | {1:<8}'.format('Apple','3'))           #
Apple    | 3
>>>print('{0:8} | {1:<8}'.format('Orange','10'))
Orange   | 10


#Formating String - Data Types
f      Flotes
.Nf    N= The number of decimal Places

>>>print('{0:8} | {1:<8.2f}'.format('Orange',2.3333333))
Orange   | 2.33


#getting user Input
>>>fruit = input('Enter a name of fruit: ')
>>>print('{} is a lovely fruit.'.format(fruit))
apple is a lovely fruit.


# Strings - formatting v3 (f-strings) 
>>>model = "2950M" 
>>>wan = 4 
>>>ios = "12.2" 
>>>f"Cisco model: {model}, {wan} WAN slots, IOS {ios}"

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Sleep for a 30 seconds
import time
print("Sleeping")
time.sleep(30)                    # sleep for a while... interrupt me!
print("Done Sleeping")


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! INPUT FUNCTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Input function (By default python Interpreter takes input as a string)
a=input('Eter first No:')
b=input('Enter Second No:')
c=a+b
print(c)

--> Eter first No:2
--> Eter Second No:3
-->23                       #because its add 2 or 3 as a string

#Typecaste inpute as a integer to add for mathematical calculation
a=int(input('Eter first No:'))
b=int(input('Enter Second No:'))
c=a+b
print(c)

--> Eter first No:2
--> Eter Second No:3
-->5                       #Now it will add 2 and 3 and return 5


#passing index value in charactor syntex
ch = input('Enter a char:')[0]
print(ch)

-->Enter a char:gjjhh
-->g

#Eval function(evaluate a function)
result = eval(input('Enter a Expression:'))
print(result)

-->Enter a Expression:5+9+6-4
-->16

#taking inpute as a aruguments
#***Run as python test.py 23 22
import sys

a = int(sys.argv[1])         #pass 1 because at index 0 filename.py
b = int(sys.argv[2])         #pass 2 because at index 1 first no  
c=a+b
print(c)

-->45

#Accepting password on command line
from getpass import getpass
username = input('Username: ')
password = getpass('password: ')         #it will hide text while taking input from keyboard

print("Logging In....") 


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.
>>> s = 'Don'
>>> s
'Don'
>>> a, b, c = s # Unpack into variables
>>> a
'D'
>>> b
'o'
>>> c
'n'

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Type Convertion !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Type conversion functions
#To int
>>> int(3.99999)
3
>>> int(-2.3)
-2

#float converts integers
>>> float(32)
32.0
>>> float('3.14159')
3.14159

#str converts its argument to a string
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'

>>>quantity_s ='3'           #enclose within '' no becomes string
>>>total =int(quantity_s)+2 
>>>total
5

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DATES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
--> datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

#The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,


# dates support calendar arithmetic
>>>from datetime import date
>>> birthday = date(1993, 10, 26)
>>> now = date.today()
>>> age = now - birthday
>>> age.days
14368

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#system Info
import sys
print(sys.version_info)
print(sys.version)


#create a folder
import os
os.mkdir("New folder")                  # create a folder new folder

#create multiple folders
import os
folders = ['folder1','folder2','folder3','folder4']
for x in folders:
   os.mkdir(x)

#Create tree structure folder
>>>from os import makedirs
>>>makedirs('1/2/3/4/5/6/7/8/9/1/1/2/3/3/4/4/5/65/6/6/6/7/7/88/8/9/2/23/2/3/5/6/8/9//5/4/3/2/2//1/3/5/6/6/778/88/2/3/4/5/')   


#range function
>>>list(range(5))
[0, 1, 2, 3, 4]


#change directory
>>>os.chdir('my_path')

#to check any directory exist on current location or not
>>>os.path.isdir('music')

#Mouse position
>>>import pyautogui
>>>pyautogui.position()

#click
pyautogui.click(10, 5)

#locateOnScreen, a pyautogui method to locate the extension' x & y coordinates in screen
v = pyautogui.locateOnScreen("E:\\python\\New 11022019\\Click chrome extention\\findicon.PNG") ##save the extension as image

#trigger click event using the pyutogui click method on perticular location
>>>import pyautogui
>>>pyautogui.click(x=v[1267],y=v[49],clicks=1,interval=0.0,button="left")

#swap the no
>>>x, y = 10, 20
>>>print(x, y) 
>>>x, y = y, x 
>>>print(x, y)

#Enumerate
#The enumerate () method adds a counter to an iterable and returns the enumerate object.
>>>names = ['Rajesh', 'Rahul', 'Aarav', 'Sahil', 'Trevor']
>>>enumerate(names)
<enumerate object at 0x031D9F80>
>>>list(enumerate(names))
[(0, 'Rajesh'), (1, 'Rahul'), (2, 'Aarav'), (3, 'Sahil'), (4, 'Trevor')]


#Random numbers
import random
for i in range(10):
	x = random.random()

print(x)

#random number between range
>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
9


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Print The File Path Of Imported Modules
>>>import os; 
>>>import socket; 
  
>>>print(os)                     #it will print os module file path
>>>print(socket)                 #it will print socket module file path


#ZIP (dictionary out of two lists)
>>>keys = ['a', 'b', 'c']
>>>vals = [1, 2, 3]
>>>zipped = dict(zip(keys, vals))
>>>print(zipped)
{'a': 1, 'b': 2, 'c': 3}

#Universally Unique IDs (or ‘UUIDs’)
#there are over 2¹²² possible UUIDs that can be generated
>>>import uuid
>>>user_id = uuid.uuid4()
>>>print(user_id)

#printing out any large, nested object(complex structured objects in an easy-to-read format)
import pprint
url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
pprint.pprint(users)

#Adding breakpoint in code we can add it anywhere in code
import pdb     #module for it

pdb.set_trace()       #add this on anywhere in code to set breakpoint on  that place


#_________________________________________________________________________________#
#Emoji
from emoji import emojize
print(emojize(":thumbs_up:"))

#_________________________________________________________________________________#
# Shallow and deep copy
# Shallow copy: Shallow copy creates a new object and then use the reference to refer the inner objects. 
>>> a = [[1,2],[3,4]]
>>> b = a.copy()
>>> print(id(a) == id(b))
False
>>> print(id(a[0]) == id(b[0]))
True

# Deep copy: deep copy create a new object and recursively copy the inner objects too. 
>>> from copy import deepcopy
>>> a = [[1,2],[3,4]]
>>> b = deepcopy(a)
>>> print(id(a) == id(b))
False
>>> print(id(a[0]) == id(b[0]))
False


#________________________________________________________________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  Module  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#A Python module is a package to encapsulate reusable code.
#Modules contain functions and classes.
#Modules are imported using the import keyword
#Import Module
#Now, you can access the functions or variables in that module with the ‘.’ (dot) Operator.

# prints a list of existing modules installed
>>>print(help('modules'))

# Importing - Module
>>>import os
#Reading Module Documentation
>>>help(os)                              

# Know about the list(Buit-in mutable Sequence)
>>>help(list)                            


# Importing only a variable (pi) from the math module
>>>from math import pi


# Importing only a function (sin()) from the math module; there's no need to add the parantheses of the function when importing it
>>>from math import sin

# Importing all the names (variables and functions) from the math module
>>>from math import *

#Installing a non-default Python 3 module in Windows is done from the command line
>>>pip install openpyx


#_________________________________________________________________________________________________________________#
#                                            Creating our Own Module

#calc module(save it as calc.py in same location)
def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b  

#using this module
from calc import *            # to use all calc funcction(1st case)
from calc import sub          #use only sub function(2nd case)

a =7
b=18

#first case
a= add(a,b)  
print(a)    

#second case
a = calc.sub(a,b)
print(a)

#________________________________________________________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Set !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Python also includes a data type for sets. A set is an unordered collection with no duplicate elements.
#You can change elements of set unlike tuple.
#Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                                                        # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}

# fast membership testing
>>> 'orange' in basket                 
True
>>> 'crabgrass' in basket
False

# Demonstrate set operations on unique letters from two words

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>>b
{'z', 'c', 'm', 'a', 'l'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

#Inline if elese(Ternary operator)/Conditional Operator
[on_True] if [expression] else [on_False]
>>>print('a is 20' if a==20 else 'a is not 20')             #Do somthing if condition else do somthing
>>>print('a is 20' if a==21 else 'a is not 20')	
>>>b = True if a==20 else False
>>>print(b)
True


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# isinstance() -->The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo 
                 #class (second argument).

#The isinstance() takes two parameters:
      # object - object to be checked
      # classinfo - class, type, or tuple of classes and types

#seprate integer and string from a list of string and integers
items = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]

str_items = []
num_items = []

for i in items:
    
    if isinstance(i, float) or isinstance(i, int):
        num_items.append(i)
    elif isinstance(i, str):
        str_items.append(i)
    else:
        pass

print(str_items)
# output --> ['Mic', 'Phone', 'Justin', 'Bag', 'Cliff Bars']

print(num_items)
# output --> [323.12, 3123.123, 134]

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Map Reduce Filter !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Filter() function in python use two argument first is function and second one is list it will filter based on function


def is_even(n):
  return  n%2==0

def is_odd(n):
    return n%2!=0

nums = [233,5,32,2,21,34,56,6,7,8]

evens = list(filter(is_even,nums))              #list in return list()

odds = list(filter(is_odd,nums))              #list in return list()

print("Totals Enens:",evens)
print("-------------------------")
print("Totals Odds",odds)


#_________________________________________________________________________________________________________________________#
#map() in python
#takes value and apply some operation

#prog 1
x = [1, 2, 3, 4, 5] 
def square(num): 
    return num*num 
print(list(map(square, x)))

#prog 2
nums = [233,5,32,2,21,34,56,6,7,8]

evens = list(filter(lambda n: n%2==0,nums))          #use lambda 

doubles = list(map(lambda n: n*2,evens))         #map also takes two argument function and the sequence

print(evens)
print(doubles)

#________________________________________________________________________________________________________________________#
#reduce() in python


from functools import reduce

nums = [233,5,32,2,21,34,56,6,7,8]

evens = list(filter(lambda n: n%2==0,nums))              #use lambda 

doubles = list(map(lambda n: n*2,evens))         #map also takes two argument function and the sequence

print(doubles)

sum = reduce(lambda a,b:a+b,doubles)                 #reduce also takes two argument function and the sequence 

print(sum)


#________________________________________________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! convert one sequence to another !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

>>> set([1,2,3])
{1, 2, 3}
>>> tuple({5,6,7})
(5, 6, 7)
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> dict([[1,2],[3,4]])             #To convert to dictionary, each element must be a pair
{1: 2, 3: 4}
>>> dict([(3,26),(4,44)])
{3: 26, 4: 44}


#________________________________________________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ranges Function !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Ranges -In Python 3 it returns an iterator. Cannot be sliced.

#defining a range
>>>r = range(10)
>>> print(r)
range(0, 10)

# Check the type of range
>>> type(r)
<class 'range'>

#converting a range to a list
>>>list(r)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#slicing a range by using the list() function first
>>>list(r)[2:5]
[2, 3, 4]

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Try / Except / Else / Finally !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Try / Except / Else / Finally - handling an exception when it occurs and telling Python to keep executing the rest of the lines 
# ...of code in the program.

try: 
	print(4/0)  #in the "try" clause you insert the code that you think might generate an exception at some point 

except ZeroDivisionError: 
	print("Division Error!") #specifying what exception types Python should expect as a consequence of running the code inside the "try" block and how to handle them 

else: 
	print("No exceptions raised by the try block!") #executed if the code inside the "try" block raises NO exceptions 

finally: 
	print("I don't care if an exception was raised or not!") #executed whether the code inside the "try" block raises an exception or not 


#result of the above block: 
--> Division Error! 
--> I don't care if an exception was raised or not!                                                                                                                                  



#_______________________________________________#
try:
	if '1' != 1:
		raise "SomeError"
	else:
		print("someError has not occur")

except:
	print("SomeError has occured")	

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!














































































































































