!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   CLASS    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                                         
#Everthing in python is a object (every object has a type)
#Classes  --> Classes provide a means of bundling data and functionality together.
#             And, class is a blueprint for the object. we can create many objects from a class
#Object is simply a collection of data (variables) and methods (functions) that act on those data. 
#A class creates a new local namespace where all its attributes are defined. Attributes may be data or functions.
#A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the ‘.‘ operator.

#______________________________________________________________________________________________________#
#for class object tutorial https://www.programiz.com/python-programming/class
#https://docs.python.org/3/tutorial/classes.html
#https://www.tutorialspoint.com/object_oriented_python/object_oriented_python_building_blocks.htm
#https://www.javatpoint.com/python-constructors

#______________________________________________________________________________________________________#

#The __init__() --> is a special method vwhich is called class constructor or initialization method that Python calls instantoly 
#					when you create a new instance of this class. All classes have a function called __init__().
#                   init() is called everytime when we create a object of that class


#There are also special attributes in it that begins with double underscores (__). For example, __doc__ gives us the docstring of that class.
#classes object could be used to access different attributes of a class.

#Class variable − when a variable declare Inside the class.A variable that is shared by all instances of a class.
#Instance Variable - When a variable is refrencing an instance is known as instance variables.

#self --> when we call init method by default first argument pass is self. It represent object.
#         The self argument is a reference to the class itself, and is used to access variables that belongs to the class.


#______________________________________#
#1 Class Creation and Instantiation

#create our first class and then its instance
class MyClass(object):                              #privously we add () but now it can be escaped 
   pass                                             #just add pass keyword if u don't want to write any data and function for this class(skip for now)
# Create first instance of MyClass
this_obj = MyClass()
print(this_obj)                                    # --> <__main__.MyClass object at 0x03B08E10>

# Another instance of MyClass
that_obj = MyClass()
print(that_obj)                                        # <__main__.MyClass object at 0x0369D390>

#_______________________________________#
#2 Instantiation (creating object of class)
#Class Attributes
#The class attributes can be accessed by the class itself ( className.attributeName) ...
#...as well as by the instances of the class (inst.attributeName).
#define one variable inside the class MyClass() and get the variable from the instances of that class

class MyClass(object):    #”class Name is a class of type object”
   var = 9                                         #declare class variable

print(MyClass.var)                           #print 9 we access class variable by class name

# Create first instance of MyClass
this_obj = MyClass()
print(this_obj.var)                      #get the variable from the instance of that class

# Another instance of MyClass
that_obj = MyClass()
print (that_obj.var)                    #get the variable from the another instance of that class

-->9
-->9
-->9

#___________________________________#
# Access and manipulate class properties
class pet:
    number_of_legs = 0

doug = pet()
doug.number_of_legs = 4                                 #we can assign a new value
print("Doug has %s legs." % doug.number_of_legs)

#____________________#
class pet:
    number_of_legs = 0

    def sleep(self):
        print("zzz")

    def count_legs(self):
        print("I have %s legs" % self.number_of_legs)
            

doug = pet()
doug.number_of_legs = 4
doug.count_legs()

nemo = pet()
nemo.number_of_legs = 0
nemo.count_legs()  

#___________________________________#
#3 Class Variables are variables that are shared by all instances of a class
#assigned in class declaration, are class variables
# class variable should be same for a each instance

class Employee:  
    id = 10;                  #class variable
    name = "ayush"            #class variable  
    def display (self):                       # at the place of self we can write anything
        print(self.id,self.name)

print(Employee.id)
print(Employee.name)

#___________________#
#4 Instance variables are variables used for data that is unique to a particular instance
# Instance variable can be unique for a each intances like (name email pay)

class Employee:
    # Initializing
    def __init__(self,first,last,pay):                        #creating parameterized Constructor employee attributes
        print('init method // constructor called')            #*** It will print as much as object is created in this case for times for all employee object 
        self.first = first                                    #Instance variable *** it is not necessary that we write both side first but while calling according to left side value call
        self.last = last                                      #Instance variable
        self.pay = pay                                        #Instance variable 
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp_1 = Employee('John','Son',60000)
emp_2 = Employee('gautam','Smith',90000)
emp_3 = Employee('gaurav','joshi',60000)
emp_4 = Employee('jitendra','burada',60000)

print(emp_1.first)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print("---------------")

print(emp_2.first)
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

print("---------------")

print(emp_3.first)
print(emp_3.pay)
emp_3.apply_raise()
print(emp_3.pay)

print("---------------")

print(emp_4.first)
print(emp_4.pay)
emp_4.apply_raise()
print(emp_4.pay)


#________________________#
#5 Counting the number of objects of a class

class Student:  
    count = 0  
    def __init__(self):                               #constructor
        Student.count = Student.count + 1  
s1=Student()  
s2=Student()  
s3=Student()  
print("The number of students:",Student.count)

#________________________#
#2nd Counting the number of objects of a class
class PartyAnimal:
    x = 0
    def party(self) :
        self.x = self.x + 1        #count +1 every time when object created
        print("So far",self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()


#______________________________________#
#Using Class FuncDons from Inside a Class When referring to funcDons from within a class  we  must always 
#..prefix the funcDon name with self   (e.g. self.subtract())

class Maths:
    def subtract(self,i,j):
        return i-j

    def testsub(self):
        print(self.subtract(8,4))

m =Maths()
m.testsub()

#______________________________________#
#We can set arbitrary attributes on an instantiated object using the dot notation
class Point:
    pass               #empty Point class with no data or behaviors
p1 = Point()
p2 = Point()
p1.x = 5
p1.y = 4
p2.x = 3
p2.y = 6
print(p1.x, p1.y)
print(p2.x, p2.y)

#_________________________________________________________________________________________#
#7 Combine Instace variable and Class Variable

class Employee:
    no_emps = 0
    raise_amount = 1.04                               #it is fix and it is accessible by all employee
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +last+ '@company.com'

        Employee.no_emps +=1
    
    def fullname(self):
        return self.first + ' ' + self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount )

print(Employee.no_emps)                                 # here 0 because there is not object created till here   

emp_1 = Employee('John','Son',10000)                   #pass first name,last name,pay

print(Employee.no_emps)                                 # here 1 because 1 object is created  

emp_2 = Employee('David','Smith',20000)

print(Employee.no_emps)                                 #Here 2 because 2nd object also created

#Using class we can also call function for any employee
#print(Employee.fullname(emp_1))

print (emp_1.fullname())                                #full name of emp_1
print (emp_1.email)                                     #Email of emp_1
print (emp_1.pay)                                       #Emp_1 pay
emp_1.apply_raise()                                     #call raise on emp1 
print("After raising:",emp_1.pay)                       #Show raised amount of emp_1

print("-------------------------------------------")

print (emp_2.fullname())                                #full name of Emp_2
print (emp_2.email)                                     #Email of Emp_2
print (emp_2.pay)                                       #Emp_2 pay
emp_2.apply_raise()                                     #call raise on emp2
print("After raising:",emp_2.pay)                       #show raised amount that emp_2

#_____________________________________________________________________________________________________________________________#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Object Methods Or Instance method!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Objects can also contain methods. Methods in objects are functions that belongs to the object.
#A function defined in a class is called a method. An instance method requires an instance in order to call it and requires no decorator.
#When creating an instance method, the first parameter is always self.
#Though we can call it (self) by any other name, it is recommended to use self, as it is a naming convention.
# we can use this method for all instances of the class
#***In instace method first argument is instance/object itself for convension we write (self) we can write anything insteed of self***.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):                             #this is instance method and its first argument is object  itself(which is self)                                    
    print("Hello my name is " + self.name)
 
 def is_above_18(self):
     return self.age>18

p1 = Person("John", 36)
p2 = Person("gautam",17)

p1.myfunc()                                       #this is a object method call we call it by object.method name

print("My age is",p1.age)
print(p1.is_above_18())                     #return True if employee age is above 18 otherwise false

#__________________________#
#8 Calling Function

class Employee:  
    id = 10;  
    name = "John"  
    
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))  

emp = Employee()                                           #creating object

emp.display()                                              #call display function  

#________________________________#
#9 Address of a class through function

class MyClass:
	"This is my second class"
	a = 10
	
	def func(self):
		print('Hello Gautam')

# create a new MyClass
ob = MyClass()                                              #The procedure to create an object is similar to a function call.

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()

#_________________#
#Classes as types
#We can use the built-in dir function to examine the capabilities of a variable
class PartyAnimal:
    x = 0
    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal()

print ("Type", type(an))        #it will print type of 

print ("Dir ", dir(an))        #capabilities of a variable

print ("Type", type(an.x))     #int type x

print ("Type", type(an.party))  

#__________________________________________________________________________________________________________________#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Class method !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# it is use less 
#In class method first argument is class as convension we write(cls)

class Person:
    count_instance = 0                                     #class variable/class attributes
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1                     #count +1 each time when init method call means instances created
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    @classmethod     
    def count_instances(cls):                         #this is class method pass cls which is short of class name
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def function():
            pass    

print(Person.count_instances())           #call class method before object creation return 0(CALL IT BY CLASS NAME.CLASS METHOD NAME)

p1 = Person("Gautam","kumar",24)        

print(p1.full_name())                    

print(Person.count_instances())         #call

p2 = Person("vikram","joshi",24)

print(p2.full_name())

print(Person.count_instances())

#______________________________________________#
#Class method as a constructor

class Person:
    count_instance = 0                                     #class variable/class attributes
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1                         #count +1 each time when init method call means instances created
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    @classmethod                                       #class method
    def from_string(cls,string):                       #class method as constructor (first argument class) and string
        first,last,age = string.split(',')               #split string by split method
        return cls(first,last,age)                     #store in different different variable and create object and pass argument


    @classmethod     
    def count_instances(cls):                               #this is class method pass cls which is short of class name
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def function():
            pass    


p1 = Person("Gautam","kumar",24)        
p2 = Person("vikram","joshi",24)


#create new way for crete object
p3 = Person.from_string('vikramant,Serawat,24')            #call class method by
print(p3.full_name())              

#__________________________________________________________________________________________________________________________#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!static method!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Static method not belongs to class or instance, as class/instance methods blongs to class/instance respectively
#It is just lke normal function/method.
#staic method decoretor is used to declare static method
#No need to pass self in static methods

class Person:
    
    @staticmethod
    def hello():                                        # no need to write self 
        print("hello, static method called")
 
Person.hello()            #call static method hello(no need to create a object)

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Constructor!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#A constructor is a special type of method (function) which is used to initialize the instance members of the class.
#Class functions that begins with double underscore (__) are called special functions as they have special meaning.
#Of one particular interest is the __init__() function. This special function gets called whenever a new object of that class is instantiated
#This type of function is also called constructors in Object Oriented Programming (OOP).We normally use it to initialize all the variables.
#The constructor is always named __init__()

#Non parameterized
class Student:    
    # Constructor - non parameterized    
    def __init__(self):    
        print("This is non parametrized constructor")    
    
    def show(self,name):    
        print("Hello",name)    

student = Student()                 #creat abject of Student class   

student.show("John")               #call show fuction with john 

#__________________________________________________________________________________________________________________________________#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Built-in class attributes!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1	__dict__	It provides the dictionary containing the information about the class namespace.
#2	__doc__	It contains a string which has the class documentation
#3	__name__	It is used to access the class name.
#4	__module__	It is used to access the module in which, this class is defined.
#5	__bases__	It contains a tuple including all base classes.

class Student:
   'Common base class for all employees'
   a=10  
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age  
    def display_details(self):  
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))  
s = Student("John",101,22)  
print(s.__doc__)  
print(s.__dict__)                              #it will print all instance variable of s object
print(Student.__dict__)                        #it will print all class variable  
print(s.__module__)
print(s.__bases__)  
print(s.__name__)

#______________________________________#
#12 prog

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)

#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

#First way for print name and salary of emap1
#print(emp1.name,emp1.salary)        
#print(emp2.name,emp2.salary)

#second way for print
emp1.displayEmployee()  #display emp1 name salary
emp2.displayEmployee()  #display emp2 name salary

print("Total Employee %d" % Employee.empCount)

#_____________________________#
#13 prog 

class ComplexNumber:
    
    def __init__(self,r = 0,i = 0):                   #__init__() to initialize the variables (defaults to zero)
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
c1.attr


#_______________________________________________________________________________________________________________________________#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Python In-built class functions!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1	getattr(obj,name,default)	It is used to access the attribute of the object.
#2	setattr(obj, name,value)	It is used to set a particular value to the specific attribute of an object.
#3	delattr(obj, name)	It is used to delete a specific attribute.
#4	hasattr(obj, name)	It returns true if the object contains some specific attribute.'''

class Student:  
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age  
  
#creates the object of the class Student  
s = Student("John",101,22)  
  
#prints the attribute name of the object s  
print(getattr(s,'name'))  
  
# reset the value of attribute age to 23  
setattr(s,"age",23)  
  
# prints the modified value of age  
print(getattr(s,'age'))  
  
# prints true if the student contains the attribute with name id  
  
print(hasattr(s,'id'))  
# deletes the attribute age  
delattr(s,'age')  
  
# this will give an error since the attribute age has been deleted  
print(s.age)  

#_________________________________________________________________________________________________________________________#
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Destructors in Python!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Destructors are called when an object gets destroyed
#destructors are not needed as much Python has a garbage collector that handles memory management automatically.
#The __del__() method is a known as a destructor method in Python. It is called when all references to the object have been deleted.

# Python program to illustrate destructor 
class Employee: 
  
    # Initializing 
    def __init__(self): 
        print('Employee created.') 
  
    # Deleting (Calling destructor) 
    def __del__(self): 
        print('Destructor called, Employee deleted.') 
  
obj = Employee() 
del obj 

-->Employee created.
-->Destructor called, Employee deleted.

#___________________#
# Python program to illustrate destructor 
  
class Employee: 
  
    # Initializing  
    def __init__(self): 
        print('Employee created') 
  
    # Calling destructor 
    def __del__(self): 
        print("Destructor called") 
  
def Create_obj(): 
    print('Making Object...') 
    obj = Employee() 
    print('function end...') 
    return obj 
  
print('Calling Create_obj() function...') 
obj = Create_obj() 
print('Program End...') 


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Python Inheritance    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class
#A class can inherit multiple classes by mentioning all of them inside the bracket. Consider the following syntax...
#...class derive-class(<base class 1>, <base class 2>, ..... <base class n>)

class Animal:  
    
    def speak(self):  
        print("Animal Speaking")  

#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()                                 #derived class dog taking the method of Animal class

#_____________________#
class Car(object):

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")

class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")



c = Car()      #call init method and print statement
c.drive()      #call drive method 
c.stop()       #call stop method

b = BMW()   #inherite the car class
b.drive()   #call drive method from base class
b.stop()    #call drive method from base class

#_____________________________________#

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Multi-Level inheritance !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Multi-level inheritance is archived when a derived class inherits another derived class. There is no limit on the number of levels up to which, the multi-level inheritance is archived in python.
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat() 

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Multiple inheritance  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Python provides us the flexibility to inherit multiple base classes in the child class.

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  

class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  

class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  

d = Derived()  

print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  

#_______________________________________________________________________________________________________________________#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Naming Conventions!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html
#Naming Convension (But in python all are public)
#_name #convension for private name
#__name__ #dunder/magic methods             (It is not convension)

class Phone(object):
    """docstring for Phone"""
    def __init__(self, brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        #self.price=price                 #Simple instance variable
        #self._price= price               #now it is convantion for programmer to indicate private
        self.__price=price                #Now it is private to access this use (_Phone__price)

    def make_a_call(self,Phone_No):
            print(f"calling {Phone_No} ......")                 #place holder for phone_No

    
    def full_name(self):
        return f"{self.brand} {self.model_name}"            

phone1 = Phone("nokia","1100",1000)

#working till it is not changed self.price=price
#print(phone1.price)                              #phone1 price

#working till it is not changed self._price=price
#print(phone1._price)                              #phone1 price print


#print phone1 attributes
print(phone1.__dict__)

#now price is privete for this class to access the price
print(phone1._Phone__price)

phone1.__price=20000                #change phone1 price

print(phone1.__price)                #print new phone1 price


#_______________________________________________________________________________________________________________________#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Encapsulation!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Binding Data and function at one place is called Encapsulation Ex:class
#you can restrict access to methods and variables. This can prevent the data from being modified by accident and is known as encapsulation.
#public methods	  --> Accessible from anywhere
#private methods  --> Accessible only in their own class. starts with two underscores
#public variables --> Accessible from anywhere
#private variables -->Accesible only in their own class or by a method if defined. starts with two underscores
# Encapsulation

class Human():
    # __private is a variable
    __privateVar = "this is __private variable"

    def __init__(self):
        self.className = "Human class constructor"
        self.__privateVar = "this is redefined __private variable"

    # public - available everywhere
    def showName(self, name):
        self.name = name
        return self.__privateVar + " " + name

    # __private - Available only in base class
    def __privateMethod(self):
        return "Private method"

    # _protected - Available in classes - heirs
    def _protectedMethod(self):
        return "Protected method"

    # __private - Available ONLY from the base class
    def showPrivate(self):
        return self.__privateMethod()

    def showProtecded(self):
        return self._protectedMethod()


class Male(Human):
    def  showClassName ( self ):
        return "Male"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


class Female(Human):
    def  showClassName ( self ):
        return "Female"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


h = Human()

print(h.className)                     #print --> "Human class constructor" from constructor instance variable

print(h.showName("Vasya"))             #call showName mrthod with name as a argument  

print(h.showPrivate())                 # return Private method from __privateMethod

print(h.showProtecded())               # return Protected method from __ProtectedMethod
# print(h.privateMethod())
# print(h.protectedMethod())
print("\n")
print("-----------------------------")

m = Male()                              #crete object for Male class that inheriate a Human class
print(m.className)                      #
print(m.showClassName())                #
# print(m.showPrivate())                #this is not accesssible
print(m.showProtected())                
print("\n")
print("-----------------------------")

f = Female()
print(f.className)
print(f.showClassName())
print(f.showProtected())
print("\n")
print("-----------------------------")

#_______________________________________________________________________________________________________________________#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Abstraction!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Abstraction means hiding complexity from user








#_______________________________________________________________________________________________________________________#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Inner class!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#We create a class (Cats) with one inner class (Head).An instance is created that calls also a method in the inner class:

