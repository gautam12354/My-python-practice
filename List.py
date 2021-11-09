!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! List !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# List(Built-in mutable sequence.) 
# If no argument is given, the constructor creates a new empty list.
# Tuples are mutable


#empty List
>>>[]
[]

# List Forming
>>>['some string']
['some string']
>>>['some string',]
['some string']

>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#Return the number of times apple appears in the list
>>> fruits.count('apple')                                                        
2

# Find index of banana
>>> fruits.index('banana')                  
3

# Find next banana starting a position from 4
>>> fruits.index('banana', 4)  
6

#Reverse the elements of the list in place.
>>> fruits.reverse()                   
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

#Appends object at the end.(Add item in list)
>>> fruits.append('grape')                                         
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

#Sort Elements alphabetically
>>> fruits.sort()                                                               
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']       

#pop(remove) remove the last item
>>> fruits.pop()                                                   
'pear'

#remove 1 index item and specify the index value whichever you want
>>>fruits.pop(1)                                                       
'apple'

#coppy the list
>>>a= fruits.copy()
['apple','banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']                                 

#remove all element from Equivalent to del a[:]
>>> fruits.clear()                                                    
>>> fruits
[]


#returns the smallest element (value) in the list 
>>>list2 = [-11, 2, 12]
>>>min(list2)
-11
#returns the largest element (value) in the list
>>>max(list2)
12

#removing an element from the list by value
>>>list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
>>> list1.remove("Avaya")
>>> list1
['Cisco', 'Juniper', 10, 10.5, -11]


#Inserting an element at a particular index
>>>list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
>>>list1.insert(2, "Nortel")
>>>list1
['Cisco', 'Juniper', 'Nortel', 10, 10.5, -11]

# sorted returns a new list, while sort returns the same list reorganized.
# sorted -->sort the elements of a list in descending order and creates a new list at the same time
>>>list2 = [9, 99, 999, 1, 25, 500]
>>>sorted(list2, reverse = True)
[999, 500, 99, 25, 9, 1]


#concatenating two lists
>>> x = [1, 2, 3]
>>> y=['suman','gautam','hema']
>>> x+y
[1, 2, 3, 'suman', 'gautam', 'hema']

#repetition of a list
>>>list1 = [9, 99, 999, 1, 25, 500]
>>>list1*3
[9, 99, 999, 1, 25, 500, 9, 99, 999, 1, 25, 500, 9, 99, 999, 1, 25, 500]


#The del statement
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]


#_____________________________________________________________#
# append() vs extend()
# append()  --> method adds a single item to the end of the list
x = [1, 2, 3]
x.append([4, 5])
x.append('abc')
print(x)
# gives you
[1, 2, 3, [4, 5], 'abc']

# extend() --> method takes one argument, a list, and appends each of the items of the argument to the original list
>>> list1 = [1, 2, 3]
>>> list2=['suman','gautam','hema']
>>> list1.extend(list2)
>>> list1
[1, 2, 3, 'suman', 'gautam', 'hema']

# Adding also a string that will added one by one
x = [1, 2, 3]
x.extend([4, 5])
x.extend('abc')
print(x)
# gives you
[1, 2, 3, 4, 5, 'a', 'b', 'c']

#_____________________________________________________________#
#using variable for index
>>>list_n=['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>>x=0
>>>list_n[x]
'banana'
>>>list_n[x+1]
'apple'

# Adding list Values by sum function
>>> list=[6,7,8,9]
>>> total=sum(list)
>>> total
30
>>>average=total/len(list)       #for find average
>>>average
7.5

#Copy list to another variable
>>> a = [1, 2, 3]
>>> b = a
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> a.append(4)
>>> b
[1, 2, 3, 4]
>>> a == b
True
>>> a is b
True
>>> c = list(a)           #identical copy of our list object.
>>> c
[1, 2, 3]
>>> a == c
True
>>> a is c
False        #Boom! This is where we get a different result. Python is telling us that c and a are pointing to two different objects, even though their contents might be the same.


#Store all values of List in new separate variables
a = [1, 2, 3] 
x, y, z = a  
print(x) 
print(y) 
print(z)

# We also nest tuples and other data structures in List
>>> L = ["Michal Jackson",10.1,82,[1,2],('A',1)]
>>> L
['Michal Jackson', 10.1, 82, [1, 2], ('A', 1)]

# Replace List Value using index
>>> A = ["disco",10,1.2]
>>> A[0] = "Hard rock"
>>> A
['Hard rock', 10, 1.2]  

# Convert string to list using split method
>>>"hard rock".split()
['hard', 'rock']

>>>"A,B,C,D".split(",")
['A', 'B', 'C', 'D']


# clone list
>>> A= ["hard rock",1,10.2]
>>> B = A[:]
>>> B
['hard rock', 1, 10.2]

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! List Slicing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Lists - slicing (works the same as string slicing, but with list elements instead of string characters)

#How slices Work
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

>>>a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r']

#slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
>>>a_list[5:15]
['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

#slice starting at index 5 up to the end of the list
>>>a_list[5:]
['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']

#slice starting at the beginning of the list up to, but NOT including, index 10
>>>a_list[:10]
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#returns the entire list
>>>a_list[:]
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']

#returns the last element in the list
>>>a_list[-1]
'r'

#returns the second to last element in the list
>>>a_list[-2]
'q'

#extracts a certain sublist using negative indexes
>>>a_list[-9:-1]
['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']

#returns the last 5 elements in the list
>>>a_list[-5:]
['n', 'o', 'p', 'q', 'r']

#returns the list minus its last 5 elements
>>>a_list[:-5]
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

#Skips every second element of the list
>>> a_list[::2]
['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q']

# Print list element in a gap of three
>>> a_list[::3]
['a', 'd', 'g', 'j', 'm', 'p']

# Print list element in a gap of four
>>> a_list[::4]
['a', 'e', 'i', 'm', 'q']

# Returns a_list's elements in reverse order
>>>a_list[::-1]
['r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']





#_________________________________________________________________________________________________________#
# Special syntax for the stride of a slice in the form somelist[start:end:stride].(stride syntex)
>>>a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
>>>odds = a[::2]
>>>evens = a[1::2]                         #select every second item starting at the beginning
>>>print(odds)
['red', 'yellow', 'blue']
>>>print(evens)
['orange', 'green', 'purple']
>>>print(a[::-2])                             #select every second item starting at the end and moving backwards
['purple', 'green', 'orange']

>>>a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>>a[2::2]                
['c', 'e', 'g']
>>>a[-2::-2]           
['g', 'e', 'c', 'a']
>>>a[-2:2:-2] 
['g', 'e']
>>>a[2:2:-2] 
[]
>>>b = a[::2] 
['a', 'c', 'e', 'g']
>>>c = b[1:-1] 
['c', 'e']

>>> l = [10, 20, 30, 40, 50, 60]
>>> l[:2] # split at 2
[10, 20]
>>> l[2:]
[30, 40, 50, 60]

#slicing object
>>> s = 'bicycle'
>>> s[::3]
'bye'
>>> s[::-1]
'elcycib'
>>> s[::-2]
'eccb'



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! List Comprehensions !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Syntex for List Comprehension
"""
new_list = [ expression for element in old_list if condition]
new_list    
The resulting list.
expression
The operation performed whenever an element fulfills the given condition, like i**3 in previous example. The result of this expression is stored in new_list.
for element in old_list
Iterates over each element in old_list
if condition
Apply a condition using an If-statement.
"""

# Suppose you wish to find cube of all numbers in a list and store them in a new list. Using a for loop, we can code this as follows:
list = [1, 2, 3, 4]
cube_list = []

for i in list:
  cube_list.append(i**3) 

print(cube_list)  #  Output: [1, 8, 27, 64]

#using List Comprehension
list = [1, 2, 3, 4]
cube_list = [i**3 for i in list]

print(cube_list) # Output: [1, 8, 27, 64]

list = [1, 2, 3, 4]
new_list = [i**3 if i%2 == 0 else i**2 for i in list]

print(new_list) # Output: [1, 8, 9, 64]

#______________________________________#

#List Comprehensions to create a list from -5 to 5 range
>>>b = [value for value in range(-5,5)]
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]



#List Comprehensions
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>>list=[1,2,3]
>>>for i in list:
   print(i)
 1
 2
 3

>>>for i in list:
   print(i*2)
 1
 4
 9


#__________________________________#
#this listcomp combines the elements of two lists if they are not equal
>>>a= [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
>>>a
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#create List 
>>> vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]

# filter the list to exclude positive numbers
>>> [x for x in vec if x <= 0]
[-4,-2, 0]

# apply a function to abs the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]

# create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(8)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]                        #num,elem is variable it can be changed
[1, 2, 3, 4, 5, 6, 7, 8, 9]

#Even Sqaures
>>> even_squares = [x * x for x in range(10) if not x % 2]
>>> even_squares
[0, 4, 16, 36, 64]


#List comprehensions can contain complex expressions and nested functions:
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']

#Passing an integer after the ':' will cause that field to be a minimum number of characters wide
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')

Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678


#Using object
stuff = list()                   #constructs an object of type list
stuff.append('python')           #call the append method
stuff.append('chuck')            #call the append method
stuff.sort()                     #calls the sort() method
print (stuff[0])                 #retrieves the item at position 0
print (stuff.__getitem__(0))     #calls the __getitem__() method in the stuff list with a parameter of zero.
print (list.__getitem__(stuff,0))#verbose way of retrieving the 0th item in the list


#dictionary comprehension
>>>dict1 = {x: x * 2 for x in range(10)}
>>> dict1
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#_____________________________________________________________________________________________________________________#
#Taking Inpute as in list

# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 

#__________________________________________________________________________________________________________________________#
# Nested LList

>>>list = [1,['a','b',['kill','bat','cup'],'c'],3]
# Access the letter ‘t’ in ‘bat’
>>>list[1][2][1][2]
't'
>>>list[1][2][1]
'bat'

#__________________________________________________________________________________________________________________________#
# Operation(Multiplication) Between Two List
list1 = [4, 5, 6]
list2 = [10, 20, 30] 
for i in list1: 
	for j in list2: #for nesting 
		print(i*j)

40 80 120 50 100 150 60 120 180 #result of the above block

# add 2 to each element in the list x(operation between two list in single line)
x = [2, 3, 4, 5, 6]  
y = [a + 2 for a in x] 
print(y)

[4, 5, 6, 7, 8] # result of ablove code


#__________________________________________________________________

# saort the list based on their lengh
name = ['carlos','Ray', 'james','gone']
print(sorted(name, key = len))











