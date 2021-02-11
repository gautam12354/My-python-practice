#it needs when we want repeat Some statements more than one time bcoz we cant coppy paste same thing again and again and 
#...it is not a good practice in programming and it is also and manual work which is not good for us.
#.. so we use use loop for this.

#While lopp 
#For loop

#__________________________________________________________________________________________________________________#
										While Loop
# It works on certain condition and for certain retration

while True:                  #it always true it will print below statement continously 
	print('Gautam')

-->
Gautam
Gautam
...

#___________________________________________________________#
# use with Increment
i=1                               #initialization  --> Assign Values
while i<=5:                      #till condition
	print('Gautam')
	i=i+1                        #increament in i

-->
Gautam
Gautam
Gautam
Gautam
Gautam

# use with decrement
i=5                               #initialization  --> Assign Values
while i>=1:                      #till condition
	print('Gautam')
	i=i-1                        #decreament in i

-->
Gautam
Gautam
Gautam
Gautam
Gautam

#___________________________________________________________#
#with string with no
i=1                           #initialization  --> Assign Values

while i<=5:                 #till condition
	print('Gautam',i)
	i=i+1

-->
Gautam 1
Gautam 2
Gautam 3
Gautam 4
Gautam 5

#___________________________________________________________#
#Nested While loop  --> In this it is completed firt inner while loop then go to outer while loop

i=1
j=1
while i<=5:
	print('Gautam')
	while j<=4:
		print('rock')
		j=j+1

	i+=1	

-->
Gautam
rock
rock
rock
rock
Gautam
Gautam
Gautam
Gautam


#New
i=1
while i<=5:
	print('Gautam')
	j=1
	while j<=4:
		print('rock')
		j=j+1

	i+=1	

-->
Gautam
rock
rock
rock
rock
Gautam
rock
rock
rock
rock
Gautam
rock
rock
rock
rock
Gautam
rock
rock
rock
rock
Gautam
rock
rock
rock
rock

#New
i=1
while i<=5:
	print('Gautam',end=' ') #end ='' --> Don't go on new line stay on same line
	j=1
	while j<=4:
		print('rock',end=' ')
		j=j+1

	i+=1	
	print()          #for new Line

-->
Gautam rock rock rock rock
Gautam rock rock rock rock
Gautam rock rock rock rock
Gautam rock rock rock rock
Gautam rock rock rock rock


# Solving Formula 

while True:
	x= int(input("Enter an number: "))
	z= x*x+2*x+3
	print(z)

Enter an number: 10
123
Enter an number: 100
10203
Enter an number: 67
4626
Enter an number: 88
7923
Enter an number:


#_________________________________________________________________________________________________________________________________#
											For LooP
# it works with Sequence like--> list tuple, set array, range function, string
# it fetechs one by one and itself and without any condition 

X = ['gAUTAM',65,3.5]

for i in X:
	print(i)

-->
gAUTAM
65
3.5

#New
x = 'Gautam'
for i in x:
	print(i)

G
a
u
t
a
m

#New
for i in [2,5.5,'Paul']:
	print(i)

-->
2
5.5
Paul

#using simple range function
for i in range(10):
	print(i)                                  #print 1 to 10

#use in desending order number
for i in range(20,10,-1):	
	print(i)                               #it will print 20 to 11 in reverse order

# print numbers using range function
for x in range(1,100,4):       #print no between 1 to 100 and gap betwwen 4 (it will print no between gap of 4 from 1 to 100)
  print(x)

#with delimiter
for x in range(1,30,2):    # from range 1 to 30 betwwen gap of 2
  print(x,"/",end="")      #print with / betwwen no


#exclude based upone some condition
for i in range(1,21):
	if i%5!=0:
		print(i)                   #print number 1 to 20 and excludes which is divisible by 5

#print Table of any no
no = int(input("Enter a no for a table:"))
for x in range(1,11):
  print(x*no)

#A tidily-aligned set of columns giving integers and their squares and cubes:
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
#_______________________________________________________________________________________________________________________________#
												Break And Continue And Pass

#Break --> jump out of the loop
av =5
x= int(input("How many Candies you want?"))

i=1
while i<=x:
	if i>av:
		print("Out of Stock")
		break
	print("Candy")
	i+=1

print("Bye")

-->
How many Candies you want?8
Candy
Candy
Candy
Candy
Candy
Out of Stock
Bye

#new
for i in range(5):
	if i==3:                     #when i=3 statement(no iteration after 3) stop iteration(entire loop break)
		break
	print('Hello',i)	

-->
Hello 0
Hello 1
Hello 2


#Continue --> it don't go out of loop just it only skip the remaining statements and go with iteration
#print no 1 to 100 and skip those values which is divisible by 3 and 5

for i in range(1,101):
	if i%3==0 and i%5==0:
		continue
	print(i)                       #print 1 to 100 and skip divisible by 3 and 5


#new
for i in range(5):
	if i==3:                      #just skip i=3 value statement(no iteration for 3) and continue after that
		continue
	print('Hello',i)	

-->
Hello 0
Hello 1
Hello 2
Hello 4




#Pass --> pass means there is no code just pass it
# print all values which are not odd

for i in range(1,101):
	if i%2==0:
		pass
	else:	
		print(i)	
#_______________________________________________________________________________________________________________________________#
												For Else

# we can use else part with the for loop anlog with if but not the part of the if block.
# found the no which is div by 5 in the list

nums = [45,6,7,98,78,89,43,56,77,67,55]

for num in nums:
	if num%5 ==0:
		print(num)          
		break          #only first number after break

else:
	print("Not Found")

-->
45

#New
nums = [4,6,7,98,78,89,43,56,77,67,51]

for num in nums:
	if num%5 ==0:
		print(num)          
		break          #only first number after break

else:
	print("Not Found")

-->
Not Found




#_______________________________________________________________________________________________________________________________#
												Patterns based upon Loops

* * * *
* * * *
* * * *
* * * *

#Rough
# 1 step prtinting one by one line by line
print('*')
print('*')
print('*')
print('*')

-->
*
*
*
*

# 2 step  printing in same line all four
print('*',end=" ")
print('*',end=" ")
print('*',end=" ")
print('*',end=" ")

-->
* * * *

# 3 step
print('* * * *')
print('* * * *')
print('* * * *')
print('* * * *')

-->
* * * *
* * * *
* * * *
* * * *


# 4 step using loop
for j in range(4):
	print('*',end=" ")       # for first row

print()

for j in range(4):
	print('*',end=" ")       # for Second row

print()

for j in range(4):
	print('*',end=" ")       # for third row

print()

for j in range(4):
	print('*',end=" ")       # for Four row

# 5 step
# We did previously doing same thing so we combine all block within a single for block

for i in range(4):
	for j in range(4):
		print('*',end=" ")       

	print()	

-->
* * * *
* * * *
* * * *
* * * *

#_________________________________________________________________#

*
**
***
****
*****

for i in range(5):                     #i for row
	for j in range(i):                 #j for colomn(don''t go till 4th just till the i value)
		print('*',end=" ")       

	print()
#_________________________________________________________________#												

* * * * *
* * * *
* * *
* *
*

for i in range(5):
	for j in range(5-i):          #no of colomn decreases based upon row no 
		print('*',end=" ")       

	print()
#_________________________________________________________________#
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8 
9 9 9 9 9 9 9 9 9


# 10 is the total number to print
for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
#_________________________________________________________________#
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
#_________________________________________________________________#
# https://www.w3resource.com/python-exercises/python-conditional-exercise-4.php

*                                                                                                             
* *                                                                                                           
* * *                                                                                                         
* * * *                                                                                                       
* * * * *                                                                                                     
* * * *                                                                                                       
* * *                                                                                                         
* *                                                                                                           
* 

n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
#_________________________________________________________________#
# https://medium.com/programminginpython-com/pyramid-pattern-in-python-da016fbac222

      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *

# Range of the triangle
num = int(input("Enter the range: \t "))

# i loop for range(height) of the triangle
for i in range(num):
	# first j loop for printing space ' '
    for j in range((num - i) - 1):               
        print(end=" ")
    # second j loop for printing stars '*'    
    for j in range(i + 1):                      
        print("*", end=" ")
    print()





































