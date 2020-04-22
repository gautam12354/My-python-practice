# Variable are storage location that have a name.
# your can asign a value to a variable and recall them by the variable name
# Case sensative --> Fruit and fruit are both different variable
# Must start with letter 
# underscore allowed in variable

# No Limit for maximum value for an integer in Python3.


#declare variable
>>> x =5     #type integer
>>> x
5
>>> 5+x
10

>>>fruit = 'apple'   #type string
'apple'

>>>my_var = True #type boolean

#id of a variable
>>>a=10
>>>print(id(a))  #We can get the address (in RAM) of some object through this id() function.
--> 1582487872

#declare variables and check conditions
>>>x, y = 1, 2
>>>x < y
True
>>>x > y
False

>>>x = 1    # Assignment
>>>x == 2   # Comparison
False

#declare two variable of same value
>>> x=y=1
>>> y
1
>>>x
1

#declare two variable at once
>>> x, y = 1, 2
>>> y
2
>>> x
1

#You can also assign different type of value in different type of variable at once
>>>a, b, c = 5, 3.2, "Hello"

>>>print (a)  --> 5
>>>print (b)  --> 3.2
>>>print (c) --> Hellos

#Assign string in three different variable at once
>>>x = y = z = "same"

print (x) -->same
print (y) -->same
print (z) -->same


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Using underscore --> to telll interpreter we use just here variable skip
>>>a,_ = (1,2)   
>>>print(a)
1

print("##############")

#packing(using *) more lenght variables
>>>a,b,*c = (1,2,3,4,5,67,7,87,3)

#unpack and check their values
print(a)  --> 1  #first value
print(b)  --> 2  #Second value
print(c)  --> [3, 4, 5, 67, 7, 87, 3]   #It will contain remaining all

print("##############")

a,b,*_,d = (1,2,3,4,5,6,7,8,9)

print(a)  --> 1  #first value
print(b)  --> 2  #Second value
#print(c)     
print(d)  --> 9 #last value

#______________________________________________#
# declare multiline variable/operation
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a) 
45

# declare multiline variable/operation
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)   

print(a)
45
#_________________________________________________#


