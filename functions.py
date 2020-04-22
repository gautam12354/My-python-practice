#Think python Book
                                                """
                                                    DRY = Don't Repeat YourSelf
                                                    Write onre Time Use many Times
                                                                                  """

# functions: --> which are operations that take one or more pieces of data as arguments.e.g: 
#                type('hello') , len( 'world').
# methods: -->   which are attached to a piece of data and called from it using a . to separate the data from the method. e.g: 
                # ' Hello World'.split() , or 'abc'.upper()


# function is a set of reusable code
# function: A named sequence of statements that performs some useful operation. Functions may or may not take arguments and may or may not produce a result.
# function definition: A statement that creates a new function, specifying its name, parameters, and the statements it contains.
# function object: A value created by a function definition. The name of the function is a variable that refers to a function object.
# header: The first line of a function definition.
# body: The sequence of statements inside a function definition.
# parameter: A name used inside a function to refer to the value passed as an argument. function call: A statement that runs a function. 
#           It consists of the function name followed by an argument list in parentheses.
# argument: A value provided to a function when the function is called. This value is assigned to the corresponding parameter in the function.
# local variable: A variable defined inside a function. A local variable can only be used inside its function.
# return value: The result of a function. If a function call is used as an expression, the return value is the value of the expression.
# fruitful function: A function that returns a value.
# void function: A function that always returns None. A special value returned by void functions


#Why functions?
# Creating a new function gives you an opportunity to name a group of statements, which makes your program easier to read, understand, and debug.
# Functions can make a program smaller by eliminating repetitive code. Later,if you make a change, you only have to make it in one place.
# Dividing a long program into functions allows you to debug the parts one at a time and then assemble them into a working whole.
# Well-designed functions are often useful for many programs. Once you write and debug one, you can reuse it.
# Argument --> A value provided to a function when the function is called.
# parameter -->  
# formal argument -->
# actual argument --> 

#_____________________________________________________#
# Fruitful Functions and Void Functions
# Fruitful Function --> Some of the functions we have used, such as the math functions, return results for lack of a better name, I call them fruitful functions. 

>>>x = math.cos(radians)
>>>golden = (math.sqrt(5) + 1) / 2

# void functions --> Other functions, like print_twice, perform an action but don’t return a value.

def print_twice(bruce):
    print(bruce)
    print(bruce)

>>> print_twice('Spam')
Spam
Spams

#___________________________________________________#
#Docstring in Python
def double(num):
    """Function to double the value"""
    return 2*num

double(5)                    # this will return   10
print(double.__doc__)      # this will return --> Function to double the value

#_____________________________________________________#

#function creation
def print_lyrics():                                     #function definition
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

#function call
print_lyrics()    #1st time
print_lyrics()    #2nd time

print(print_lyrics)       #The value of print_lyrics is a function object, which has type “function”


#repeate function which call print_lyrics function 
def repeat_lyrics():                                     #In this fuction we call print_lyrics() function
	print_lyrics()
	print_lyrics()

repeat_lyrics()             #it will print two times

#_______________________________________________________________________________________#
#Inside the function, the arguments are assigned to variables called parameters.

def print_twice(bruce):             #make a function to print twice with argument
	print(bruce)
	print(bruce)

print_twice('Gautam')  #you can pass anything to print twice
-->Gautam
-->Gautam


michael = 'Eric, the half a bee.'
print_twice(michael)                  #A variable as an argument
--> Eric, the half a bee.
--> Eric, the half a bee.

print_twice('Spam '*4)
--> Spam Spam Spam Spam
--> Spam Spam Spam Spam

#_______________________________________________________#

#Variables and Parameters Are Local in function
#return --> to result from a function, we use the return statement in our function
#When you create a variable inside a function, it is local, which means that it only exists inside the function

def addtwo(a, b):   #here a and b is formal arguments
	added = a + b       
	return added

x = addtwo(3, 5)   #(actual arguments a and b)add two function was called with 3 and 5 as arguments we passing values
print(x)

#1 way
def addthree(a,b,c):
    print(a+b+c)               #we can use print instead of return

addthree(5,5,5)    

#2nd way
def addtwo(a, b):
    x = a + b       
    print(x)

addtwo(3, 5)              #add two function was called with 3 and 5 as arguments


#3rd way
def addtwo(num1,num2):                #python is a dynamic type inpute language we can enter int or string anything
    return num1+num2

a= int(input("Enter first no:"))    
b= int(input("Enter second no:"))

total = addtwo(a,b)
print(total)


#greatest number function between three
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
        
print(greatest(10,20,40))

#_______________________________________________________________________________________________________________#
#the concept of main function 
#it call all other function which you want

def function1():
    print("call from function1")

def function2():
        print("call from function2")

def main():
    function1()
    function2()          

main()            #call all function at once

#___________________________________________________________________________________________________________#
#call function by a another function
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)            #call reverse function with text and check it with text


something = input("Enter text: ")
if is_palindrome(something):              #check reverse here
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")


#_________________________________________________________________________#
#Adding optional arguments with default values to the functions we define
def greet(who="Colin"):                  # strore default value colin in who
    print("Hello,", who)
    
greet()
greet(who="Kaggle") # (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")      # it will pass just a string world

#_______________________________________________________________________________________#
#Functions Applied to Functions
#You can supply functions as arguments to other functions
#Functions that operate on other funcitons are called "Higher order functions.

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line 5 25
)

#___________________________#
#Inner Functions
#Inner functions to protect them from everything happening outside of the function, meaning that they are hidden from the global scope.

def outer(num1):
    def inner_increment(num1):  # Hidden from outer code
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)

inner_increment(10)              #give error -->NameError: name 'inner_increment' is not defined 
# outer(10)                      #return 10 11

#___________________#
def has_permission(page):
    def inner(username):
        if username == 'Admin':
            return "'{0}' does have access to {1}.".format(username, page)
        else:
            return "'{0}' does NOT have access to {1}.".format(username, page)
    return inner


current_user = has_permission('Admin Area')
print(current_user('Admin'))

random_user = has_permission('Admin Area')
print(random_user('Not Admin'))

#___________________#
#https://www.guru99.com/learn-python-main-function-with-examples-understand-main.html
#Python Main Function
#When you execute the main function, it will then read the "if" statement and checks whether __name__ does equal to __main__.
#at time of import when we want execute one function at first 

>>>print(__name__)            #at interpreter
--> __main__

#Calc.py
def add():
    print("result 1 is ", __name__)

def sub():
    print("result 2 is ")

def main():
    print("In calc main")
    add()
    sub() 

if __name__ == "__main__":           #if name is main then only call main otherwise other code will use these function as module
    main()

#demo.py
from calc import add

def func1():
    add()
    print("from func1")

def func2():
    print("from func2")    

def main():
    func1()
    func2()    

main()    

--> result 1 is calc
--> from func1
--> from func2

#_______________________#
#returning at a time two results
def add_sub(a,b):
    c= a+b
    d= a-b
    return c,d

result1,result2 = add_sub(5,4)

print("Addition is:",result1,"Substraction is:",result2)


#_________________________________________________________________________________________________________________#
#from Telusko python
#Actual arguments Types:
|__Positional
  |__Kewords 
     __|__Default
          |__variable length
             |__keyword variable length argument

#positional
def person(name,age):          #name and age are formal arguments
    print(name)
    print(age)

person('navin',28)     #we assign according to position sequencialy(these are actual arguments)    


#Kewords
def person(name,age):
    print(name)
    print(age)

person(name='navin',age=28)     #we assign according to keywords   


#default
def person(name,age=18):
    print(name)
    print(age)

person('navin',28)     #here age automatically take 18 no need for age argument(In case we pass it will be override)

#Variable length argument 
#where no of argument is not fixed


def sum(a,*b):     #Now first argument is a and another all argument will be in b
    #c= a+b
    print(a)
    print(b)

sum(4,7,4,56,7,8,8,67,56,4,5)    #a= 4 and b= (7, 4, 56, 7, 8, 8, 67, 56, 4, 5)


#for now adding no to a list of b
def sum(a,*b):     
    
    c=0
    
    for i in b:
        c=c+i

    print(c)    

sum(4,7,4,56,7,8,8,67,56,4,5)    


#keyword variable length argument
def person(name,**data):          #** star means passing many argument but with the help of keyword
    
    print(name)
    print(data)

person('navin',age=28,city='delhi',mob=987655788)

#for printing in a key-value pair
def person(name,**data):

    print(name)
    for i,j in data.items():         #for dictionary key value pair
        print(i,'=',j)
    
person('navin',age=28,city='delhi',mob=987655788)    

#End Actual argument
#_________________________________________________________________________________________#
#function for add even count:

def count(list):
    even = 0
    odd = 0

    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd        

list = [1,2,3,5,66,7,22,23,4,5,66,77,89,90,1,23,34,21]

even,odd = count(list)

print("Even: {} and Odd: {} ".format(even,odd))
        
#__________________________________________________________________________________________________________#
#harshit vashisht
#variable scope in function

def func():
    x= 7            #this variable scope is only inside this function (local variable)
    return x

def fun2():
    print(x)

#fun2()           #error --> this can't be accessible outside function
#print(x)         #error --> this will also be can't accessible

#_______________________#
#we can use by calling that function only

def func():
    x= 7            #this variable scope is only inside this function (local variable)
    return x

print(func())     #print 7 here

#_______________________#
#global variable which is outside the function

x = 5           #global variable
def func():
    x= 7            #this variable scope is only inside this function (local variable)
    return x

print(func())     #print 7 here
print(x)          #print 5 here which is outside the function

#_______________________#
#change globale variable value inside the function by using 'global' keyword

x = 5           #global variable

def func():
    global x      #here we declare x as global and we are changing it now to 7
    x= 7         #(local variable)
    return x

print(func())     #function call
print(x)        #now it will change 5 to 7 and print 7 (beacause function is already called)

#______________________________#
x = 5           #global variable

def func():
    global x      #here we declare x as global and we are changing it now to 7
    x= 7         #(local variable)
    return x

print(x)          #It will print 5 because not yet function is called

print(func())     #function call it will print 7 (which is declare inside the function)
        
print(x)          #now it will change 5 to 7 and print 7 (beacause function is now called)           


#________________________________________________________________________________________________________________#
# Nonlocal Variables --> Nonlocal variable are used in nested function whose local scope is not defined. This means, the variable can be neither in the local nor 
#                        the global scope.
def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()









