
#########################################################  Generator ###################################################################
# Python code to illustrate generator, yield() and next(). 
#Python generators are a simple way of creating iterators.
#Generators are written just like a normal function but we use yield() instead of return() for returning a result. 
#yields the values one at a time; traversing a sequence up to a certain point, getting the result and suspending the execution
#It is more powerful as a tool to implement iterators.
#Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
#The next() function returns the next item in an iterator
"""
Unlike regular functions which on encountering a return statement terminates entirely, generators use yield statement in which the state of 
the function is saved from the last call and can be picked up or resumed the next time we call a generator function.Another great advantage 
of the generator over a list is that it takes much less memory.Generator function contains one or more yield statement instead of return statement.
"""
"""
Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
"""

#Generators - special routines that can be used to control the iteration behavior of a loop; defined using the "def" keyword;

#______________________________#
# Simple generator
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)

#____________________________________________________________________#
# Using function

def generator():                          #creating a generator function
    t = 1
    print('First result is ',t)
    yield t                               
  
    t += 1
    print('Second result is ',t) 
    yield t 
  
    t += 1
    print('Third result is ',t) 
    yield t 
  
call = generator() 
next(call)               #iterate through the items using next()
next(call) 
next(call)


#______________________________________________________________________________________________________________________________#
# Python code to illustrate generator expression  
generator = (num ** 2 for num in range(10))  
for num in generator: 
    print(num) 

#We can also generate a list using generator expressions :
string = 'geek'
li = list(string[i] for i in range(len(string)-1, -1, -1)) 
print(li) 


##################################################################  Iterators #################################################################

#Iterators - an object which allows a programmer to traverse through all the elements of a collection

#Iterators are objects that can be iterated upon.An object which will return data, one element at a time.
#We can build your own iterator using __iter__ and __next__ methods.
#to create iterators, we can use both regular functions and generators
#Most of built-in containers in Python like: list, tuple, string etc. are iterables.

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next() 

>>>print(next(my_iter))
4

>>>print(next(my_iter))
7

>>>print(my_iter.__next__())            ## ....next(obj) is same as obj.__next__()
0

>>>print(my_iter.__next__())
3

## This will raise error, no items left
>>>next(my_iter)



#_____________________________________________________________________________________________________________#
#Building Your Own Iterator in Python
#The __iter__() method returns the iterator object itself. If required
#The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

for i in PowTwo(5):     
    print(i)

#_____________________________________________________________________________________________________________#
############################################ itertools #########################################################

#Itertools - built-in Python module for working with iterable data sets



















