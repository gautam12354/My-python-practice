#_________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  Dictionaries !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Dictionary is one of the Python’s built-in data types and it defines one-to-one relationships between keys and values.
'''
* You cannot have duplicate keys in a dictionary values may be. Altering the value of an existing key will delete the old value.
* You can add new key-value pairs at any time.
* Dictionaries have no concept of order among elements its unodered. They are simple unordered collections.Stored data like Map.
* it is mutable.
* it is index as well in form of keys

'''


# empty dictionary
>>>my_dict = {}

# dictionary with integer keys
>>> my_dict = { 1:'msft', 2: 'IT'}

# dictionary with mixed keys
>>> my_dict = {'name': 'Aarav', 1: [ 2, 4, 10]}

# using built-in function dict()
>>>my_dict = dict({1:'msft', 2:'IT'})

# From sequence having each item as a pair
>>> my_dict = dict([(1,'msft'), (2,'IT')])

# Accessing or Extracting a value for a specified key
>>> my_dict[1]
'msft'
>>> my_dict[2]
'IT'

# Can't access key by value
>>> my_dict['IT']
Traceback (most recent call last):
   File "<pyshell#177>", line 1, in <module>
   my_dict['IT']
KeyError: 'IT'
>>>

# Dictionaries
>>> my_dict
{1: 'msft', 2: 'IT'}

# Modifies an existing key-value pair
>>> my_dict[2] = 'Software'
>>> my_dict
{1: 'msft', 2: 'Software'}

#Adds a new key-value pair to the dictionary
>>> my_dict[3] = 'Microsoft Technologies'
>>> my_dict
{1: 'msft', 2: 'Software', 3: 'Microsoft Technologies'}

# Dictionaries
>>> my_dict
{1: 'msft', 2: 'Software', 3: 'Microsoft Technologies', 4: 'Operating System','Bill Gates': 'Owner'}

# Deleting a specific key-value pair from the dictionary
>>> del my_dict['Bill Gates']
>>> my_dict
{1: 'msft', 2: 'Software', 3: 'Microsoft Technologies', 4: 'Operating System'}


# The number of key-value pairs in the dictionary
>>> len(my_dict)
4

#delete All key value
>>> my_dict.clear()
>>> my_dict
{}

# Dictionary
>>> dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
>>> dict1
{'Vendor': 'Cisco', 'Model': '2600', 'IOS': '12.4', 'Ports': '4'}

# Verifies if "IOS" is a key in the dictionary
>>>"IOS" in dict1
True

# Verifies if "IOS2" is not a key in the dictionary 
>>>"IOS2" not in dict1
True

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Dictionaries - Methods !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Dictionary
>>> dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
>>> dict1
{'Vendor': 'Cisco', 'Model': '2600', 'IOS': '12.4', 'Ports': '4'}

# Returns a list having the keys in the dictionary as elements
>>> dict1.keys()
dict_keys(['Vendor', 'Model', 'IOS', 'Ports'])


# Returns a list having the values in the dictionary as elements
>>> dict1.values()
dict_values(['Cisco', '2600', '12.4', '4'])


# Returns a list of tuples, each tuple containing the key and value of each dictionary pair
>>> dict1.items()
dict_items([('Vendor', 'Cisco'), ('Model', '2600'), ('IOS', '12.4'), ('Ports', '4')])


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Using Loop to access key value using items() 
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)


# Dictionay also contains list tuples in vales
>>>Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
>>> Dict["D"]
(4, 4, 4)

