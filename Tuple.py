#_________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Tuple !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Tuples are very similar to list except that the whole set of elements are enclosed in parentheses instead of square brackets.
'''
You cannot add elements to a tuple.
You cannot append or extend a method.
You cannot remove elements from a tuple.
Tuples have no remove or pop method.
Count and index are the methods available in a tuple.
'''

# ********************    Tuples - the same indexing & slicing rules apply as for lists     *********************************


# Creating an empty tuple
>>>my_tuple = ()
>>> my_tuple
()

# New Tuple
>>>tupl = ('Tuple', 'is', 'an', 'IMMUTABLE', 'list')

# Can't Add elements in tuple
>>>tupl.append('new')
Traceback (most recent call last):
   File "<pyshell#148>", line 1, in <module>
      tupl.append('new')
AttributeError: 'tuple' object has no attribute 'append'

# Can't Remove element from Tuple
>>> tupl.remove('is')
Traceback (most recent call last):
   File "<pyshell#149>", line 1, in <module>
      tupl.remove('is')
AttributeError: 'tuple' object has no attribute 'remove'

#returns the element index in the tuple 
>>> tupl.index('list')
4

# check Specefic eleemnt in Tuple exist or not
>>> "is" in tupl
True

# Count specefic element number
>>> tupl.count('is')
1

#__________________________________________________________________________________________________________________________________#
# Creating Tuple
>>>my_tuple = (1, 2, 3, 4)
(1, 2, 3, 4)

# Returns the number of elements in the tuple
>>>len(my_tuple)
4

# Returns the first element in the tuple (index 0)
>>>my_tuple[0]
1

# Tuples - tuple assignment / packing and unpacking
>>>tuple1 = ("Cisco", "2600", "12.4")


#vendor will be mapped to "Cisco" and so are the rest of the elements with their corresponding values; both tuples should have the same number of elements
>>>(vendor, model, ios) = tuple1


# Assigning values in a tuple to variables in another tuple
>>> a = (a, b, c)
>>> b = (1, 2, 3)
>>> a==b
True

# Tuple concatenation
>>>tuple1 + (5, 6, 7)
('Cisco', '2600', '12.4', 5, 6, 7)


# Tuple multiplication
>>>tuple1 * 3
('Cisco', '2600', '12.4', 'Cisco', '2600', '12.4', 'Cisco', '2600', '12.4')

# Check element not exist in tuple
>>>784 not in tuple1
True

# Deleting a tuple
>>>del tuple1


















