#__________________________________________________________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Conditional execution !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# It is possible in one line
>>>print(‘Hello’) if i > 7 else print(‘Hi’)


#_______________________________________________________________________#

# Simple If Statements
i = 10
if (i > 15): 
  print ("10 is less than 15") 

print ("I am Not in if")

-->
I am Not in if

#_______________________________________________________________________#
# If Else Condition
x=12
if x%2 == 0 :
  print('x is even')
else :
  print('x is odd')

-->
x is even

#_______________________________________________________________________#
#if elif else Statements
#Chained conditionals
x=12
y=2
if x < y:
  print('x is less than y')
elif x > y:                              #elif is an abbreviation of “else if.”
  print('x is greater than y')
else:
  print('x and y are equal')

-->
x is greater than y

#_______________________________________________________________________#

#Nested conditions
i = 10
if (i == 10): 
    #  First if statement 
    if (i < 15): 
        print ("i is smaller than 15") 
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print ("i is smaller than 12 too") 
    else: 
        print ("i is greater than 15")

-->
i is smaller than 15
i is smaller than 12 too        

#2nd program illustrate nested If statement 
x=3
if 0 < x:
  if x < 10:
    print('x is a positive single-digit number.')

-->
x is a positive single-digit number.

#_______________________________________________________________________#
# if-elif-else ladder

i = 20
if (i == 10): 
    print ("i is 10") 
elif (i == 15): 
    print ("i is 15") 
elif (i == 20): 
    print ("i is 20") 
else: 
    print ("i is not present") 


-->
i is 20

#_______________________________________________________________________#
#A Python 'if not' operator
x = 10
if not x > 10:
    print("not retured True")
else:
    print("not retured False")

-->
not retured True

#_______________________________________________________________________#
# Mixed Nesting
for number in range(10): 
  if 5 <= number <= 9:
    print(number)

#result of the above block
5 6 7 8 9

#_______________________________________________________________________#
    
