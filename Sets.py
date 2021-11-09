!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Set !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Python also includes a data type for sets. A set is an unordered collection with no duplicate elements.
#You can change elements of set unlike tuple.
# its unodered so set don't record element positions
# sets only have unique elements
#Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

"""
A set is used when you want to store a bunch of elements and be certain that there are only present once. 
Elements of a set must also be immutable. You can think of this as the keys of a dictionary with no associated values or you 
could see it as a list where what matters isn't the order of the elements but whether an element is in the list or not.
"""

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                                                        # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}

# fast element checking in set
>>> 'orange' in basket                 
True
>>> 'crabgrass' in basket
False

# creating set from list
>>>album_list = ["Michal Jackson","Thriller","Thriller",1982]
>>>album_set = set(album_list)
>>>album_set
{'Michal Jackson', 'Thriller', 1982}


# Adding element in set
>>>A= {"Thriller","Black in Black","Ac/DC"}
>>>A.add("NSYNC")
>>> A
{'NSYNC', 'Black in Black', 'Thriller', 'Ac/DC'}

# add multiple elements
>>>A.update("man","Black","Tro")
{'Iron Man', 'a', 'T', ' ', 'Black in Black', 'e', 'Thriller', 'i', 'r', 't', 'k', 'l', 'c', 'n', 'M', 'm', 'B', 'o', 'Ac/DC', 'I'}


# Remove elements from Set
>>>A.remove("NSYNC")
>>>A
{'Black in Black', 'Thriller', 'Ac/DC'}

#___________________________________________________________________________________________#
# Demonstrate set operations on unique letters from two words

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique Elements in set a
{'a', 'r', 'b', 'c', 'd'}
>>>b
{'z', 'c', 'm', 'a', 'l'}

# intersection of two set(common elements available in both set a and b)
>>> a & b                              
{'a', 'c'}

# Union of two setss(All unique elements in set a or b )
>>> a | b                              
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

>>>S = {'A','B','C'}
>>>U = {'A','Z','C'}
>>>U.union(S)
{'Z', 'B', 'C', 'A'}

# defference of set (set of elements that are only in A but not in B)
>>> a - b                              
{'r', 'd', 'b'}

# Symmetric Difference(set of elements in A and B but not in both (excluding the intersection)) 
>>> a ^ b                              
{'r', 'd', 'b', 'm', 'z', 'l'}


#___________________________________________________________________________________________#
Method	Description

add()	Adds an element to the set
clear()	Removes all elements from the set
copy()	Returns a copy of the set
difference()	Returns the difference of two or more sets as a new set
difference_update()	Removes all elements of another set from this set
discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	Returns the intersection of two sets as a new set
intersection_update()	Updates the set with the intersection of itself and another
isdisjoint()	Returns True if two sets have a null intersection
issubset()	Returns True if another set contains this set
issuperset()	Returns True if this set contains another set
pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()	Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
union()	Returns the union of sets in a new set
update()	Updates the set with the union of itself and others

#___________________________________________________________________________________________#

# subset
>>>album_set_1 = {"Thriller","Black in Black","Ac/DC"}
>>>album_set_3 = {"Black in Black","Ac/DC"}
>>>album_set_3.issubset(album_set_1)
True




	