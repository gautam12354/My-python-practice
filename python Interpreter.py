
#clear Screen in Command window
>>>import os
>>>os.system("cls")

#it is not string it should be inside quotes
>>> this is a word
  File "<stdin>", line 1
    this is a word
                 ^
SyntaxError: invalid syntax

#simple string
>>>"this is a word"
"this is a word"

#no can be declared
>>>123
123

#concatenate variables 
>>>prefix = 'Py'
>>>prefix + 'thon'              #Now prefix hold the 'py' string
'Python'


# length of string
>>>len("gautam")
6

#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
>>> 'Py' 'thon' 
'Python'

#MConcatenate two string on interpreter
>>>"hi how are you" + " Gautam"               
 'hi how are you Gautam'

#interactive operator"_"
>>>_                          #it is reference to the output of the last executed expresssion
9
>>>print(_)
9

#Basic operation on Interpreter
>>>3+3
6
>>>6-2
4
>>>5*6
30
>>9/4
2.25
>>>9/4.0
2.25

# super long interter also possible
>>>2**100
1267650600228229401496703205376

#Multiplying string
>>>'2'*2
'22'
>>>'abc'*2
'abcabc'


#Adding Adding and substracting substracting numbers
>>> 2++2
4
>>> 2--2
4

# exponentiation: it raises a number to a power 5³:
>>> 5**3
125 

# The ** operator is evaluated right to left.
>>> 2**2**3**1                               # it first 2**2**3**1-->2**2**3 --> 2**8-->256
256

#get binary value of number
>>> bin(5)
‘0b101’

#Modulo operator --> (this means finding out the remainder after division of one number by another)
>>>3%2
1
>>>4%2
0

# ^ is used for exponentiation, but in Python it is a bitwise operator called XOR
>>> 6 ^ 2
4

#Highest priority: raising to a power; Medium priority: division, multiplication and modulo; Low priority: addition and subtraction 
>>>100 - 5 ** 2 / 5 * 2 #1st: 5 ** 2, second: / then *, third - ; 
90.0


#________________________________________________________________________________________________#

#1 has a Boolean value of True, and 0 has that of False So:
>>> True/2
0.5

>>> False*2
0

#True is equivant to 1 and false is equivant to 0 automatically
>>> True == 1
True
>>> False == 0
True
>>> 

#For “not equal” use !=
>>>1 != 2         
True

# Note "and" and "or" are case-sensitive
>>>True and False  
=> False

>>>False or True   
=> True


#check condition on interpreter
>>>y = 100 < 10
>>>y
False

#________________________________________________________________________________________________#

#(Type checking) --> If you are not sure what type a value has, the interpreter can tell you
#take y value from the above condition 
>>>type(y)
<class 'bool'>

>>> type(17)
<class 'int'>

>>> type(3.2)
<class 'float'>

>>> type('2')
<class 'str'>
#________________________________________________________________________________________________#

# number should not be started with zero
>>> 02+02                         
  File "<stdin>", line 1
    02+02
     ^
SyntaxError: invalid token

#not in first or not in second place
>>> 2+02
  File "<stdin>", line 1
    2+02
       ^
SyntaxError: invalid token

#It can be in middle
>>> 202
202

#not allowed to take any space betwwen number
>>> 2 3                          
  File "<stdin>", line 1
    2 3
      ^
SyntaxError: invalid syntax

#Not possible assign variable in no
>>>42 = n                            
  File "<stdin>", line 1
SyntaxError: can't assign to literal                                                                                                                

# true and false must be in first letter Capital 
>>> true and false or not false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined

#________________________________________________________________________________________________#
# Comparators

>>>1===2
False
>>>1>2
False
>>>1<2
True
>>>1<=2
True
>>>1!=2
True

>>>37>29 and 37<40
True

>>>37>29 or 37<40
True

>>>not 37 > 29
False

# order of operation for Booleans not and or
>>> True and False or not False
True
>>> True and False or True
True
>>> False or True
True
>>> True and False or not False
True
>>> (True and False) or (not False)
True
>>>

#________________________________________________________________________________________________#
#Numbers - conversion between numeric types 
>>>int(1.5) 
1 
>>>float(2) 
2.0 

#Numbers - Useful Functions 
>>>abs(5) #the distance between the number in between parantheses and 0 
5
#returns the same result as abs(5)
>>>abs(-5)  
5

#returns the largest number
>>>max(1, 2) 
2

#returns the smallest number
>>>min(1, 2)  

#another way of raising to a power
>>>pow(3, 2)
9

# Some more In-built function of python
>>>len( 'world')
5

>>>type("hello")
<class 'str'>

>>> "hello world I am gautam I love python".split()
['hello', 'world', 'I', 'am', 'gautam', 'I', 'love', 'python']

>>> "gautam".upper()
'GAUTAM'



# Booleans - logical operations 

>>>(1 == 1) and (2 == 2) #result is True; AND means that both operands should be True in order to get the expression evaluated as True 
True

>>>(1 == 1) or (2 == 2) #result is True; when using OR, it is enough if only one expression is True, in order to have True as the final result 
True

>>>not(1 == 1) #result is False; using the NOT operator means denying an expression, in this case denying a True expression 
False

>>>not(1 == 2) #result is True; using the NOT operator means denying an expression, in this case denying a False expression 
True

>>>None, 0, 0.0, 0L, 0j, empty string, empty list, empty tuple, empty dictionary #these values always evaluate to False 

>>>bool(None) #returns False; function that evaluates values and expressions 
False

>>>bool(0) #returns False; function that evaluates values and expressions 
False

>>>bool(2) #returns True; function that evaluates values and expressions 

>>>bool("router") #returns True; function that evaluates values and expressions
True

















