#https://www.programiz.com/python-programming/methods/string
#https://www.programiz.com/python-programming/string

# Using Quotes within Strings
>>> sentence = 'she said, "that is a great tasting apple!"'
>>> sentence
'she said, "that is a great tasting apple!"'
>>> sentence2 = "that's a great tasting apple!"
>>> sentence2
"that's a great tasting apple!"
>>> double  = "she said, \"That's a great tasting apple!\""
>>> double
'she said, "That\'s a great tasting apple!"'
>>> single = 'she said, "That\'s a great tasting apple!"'
>>> single
'she said, "That\'s a great tasting apple!"'


#Strings - indexing 
>>>a = "Cisco Switch" 
>>>a.index("i")
1

#String upper method
var = "Hello, John"
print(type(var)) # ‘str’> or <class 'str'>
print(var.upper()) # upper() method is called, 
--> HELLO, JOHN

# lower method
>>> str = 'WOAH!'
>>> str.lower()
-->'woah!'

# #Strings - concatenating two or more strings
>>>print('I' + 'Love' + 'Python.')
--> ILovePython.

# Strings - repetition / multiplying a string
>>>print('-' *10)
----------

# str() fuction (non string converts in string)
>>>version =3
>>>print('I love Python' + version +'.')
I love Python3.8


#Strings - finding a character 
>>>a = "Cisco Switch"
>>>a.find("sco")               #--> it display the finding chactor position 
2

#count() lets you know how many times a certain character appears in the string.
>>>a = "Cisco Switch" 
>>>a.count("i")
2

>>> number_list =['one', 'two', 'one', 'two', 'two']
>>> number_list.count('two')
-->3


#built in function for lenght of string
>>>fruit = 'apple'
>>>fruit_len = len(fruit)
>>>print(fruit_len)
5
>>>print(len('apple'))
5

#built in function for max
>>> max('Hello world')
'w'                                      #“largest character” in the string

#built in function for min
>>> min('Hello world')
' '                                      #smallest character

#________________________________________________________________________#
#String strip() Function --> remove unwanted characters from either the beginning or ending of a string. 
#To strip whitespace (spaces, tabs, newline characters, etc).
>>> orig_text = '     The cow jumped over the moon!        \n'
>>> print(orig_text.strip())
The cow jumped over the moon!  

#Specify the strip charactor
>>> orig_text = '-----The cow jumped over the moon!$$$$$'
>>> print(orig_text.strip('-$'))
The cow jumped over the moon!

#strip characters from only one side of the string via the String.rstrip() and String.lstrip() methods.
>>> orig_text = '*****The cow jumped over the moon!*****'
>>> print(orig_text.rstrip('*'))
*****The cow jumped over the moon!
>>> print(orig_text.lstrip('*'))
The cow jumped over the moon!***** 


# lstrip() --> Removes all leading whitespace in string.

# rstrip() --> Removes all trailing whitespace of string.

# swapcase() --> Inverts case for all letters in string.

# isdigit() --> Returns true if string contains only digits and false otherwise.

# isnumeric() --> Returns true if a unicode string contains only numeric characters and false otherwise.

# isspace() --> Returns true if string contains only whitespace characters and false otherwise.

#________________________________________________________________________#
# The in Operator
fullstring = "StackAbuse"  
substring = "tack"

if substring in fullstring:  
    print("Found!")
else:  
    print("Not found!")

#The in Operator in checking within string
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False

# Strings --> checking if a character is not part of a string
>>>a = "Cisco"
>>>"b" not in a
True

#________________________________________________________________________#
    
#Strings - checking whether the string starts with a character 
>>>a = "Cisco Switch" 
>>>a.startswith("C")
True

#Strings - checking whether the string ends with a character 
>>>a = "Cisco Switch" 
>>>a.endswith("h")
True

#Create a single string from all the elements in list Using "join" function
>>>a = ["Geeks", "For", "Geeks"] 
>>>print(" ".join(a))
--> Geeks For Geeks

#to .join() for string
>>>print(":".join("Python"))
-->P:y:t:h:o:n

#Reversing String 
>>>string="12345"    
>>>print(''.join(reversed(string)))
-->54321

#Reverse String in another way
>>>a ="GeeksForGeeks"
>>>print("Reverse is", a[::-1])

#________________________________________________________________________#
#Split Strings
>>>word="guru99 career guru99"   
>>>print(word.split(' '))
--->['guru99', 'career', 'guru99']

#Split string on base of some charactor
>>>word="guru99 career guru99"   
>>>print(word.split('r'))
-->['gu', 'u99 ca', 'ee', ' gu', 'u99']

#_________________________________________________________________________________#
#capetize words --> Capitalizes first letter of string.
>>>import string
>>>text = 'Tutorialspoint - simple easy learning.'
>>>print(string.capwords(text))
Tutorialspoint - Simple Easy Learning.

#Word Replacement using replace()
>>>str = "this is string example....wow!!! this is really string"
>>>print(str.replace("is", "was"))                                      # Old text New text
>>>print(str.replace("is", "was", 3))                                   # Now, lets replace first 3 occurrences of ‘is’ with ‘was’.
thwas was string example....wow!!! thwas was really string
thwas was string example....wow!!! thwas is really string

#replace() allows you to replace any character with another character.
>>> str = 'rule'
>>> str.replace('r', 'm')
-->'mule'



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! String Slicing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Strings - slicing 

>>>string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2" 

#slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
>>>string1[5:15]     
'10.110.8.9'

#slice starting at index 5 up to the end of the string
>>>string1[5:]         
'10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2'

#slice starting at the beginning of the string up to, but NOT including, index 10 
>>>string1[:10]
'O E2 10.11' 

#returns the entire string
>>>string1[:]
'O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2'  

#returns the last character in the string
>>>string1[-1]
'2'  

#returns the second to last character in the string
>>>string1[-2]
't'  

#extracts a certain substring using negative indexes
>>>string1[-9:-1]
'Ethernet'  

#returns the last 5 characters in the string
>>>string1[-5:]
'rnet2'  

#returns the string minus its last 5 characters
>>>string1[:-5]
'O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethe'  

#adds a third element called step; skips every second character of the string
>>>string1[::2]
'OE 01089[6/]va1.1.5.,00:0 tent'  

#returns string1's elements in reverse order
>>>string1[::-1]
'2tenrehtE ,00:10:0 ,6.452.911.01 aiv ]5/061[ 9.8.011.01 2E O' 


# Updating Strings --> You can "update" an existing string by (re)assigning a variable to another string.
>>>var1 = 'Hello World!'
>>>print ("Updated String :- ", var1[:6] + 'Python')
--> Updated String :-  Hello Python

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#_________________________________________________________________________________#
#String to charactor
>>>for x in "PYTHON":

   print(x)
   print(end=' ')
   print(x*3)

#Count Vowel in the String
string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels) 


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
Replace a set of multiple sub strings with a new string in main string.
'''

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString    


mainStr = "Hello, This is a sample string"

# Replace multiple characters / strings from a string
# Replace all the occurrences of string in list by AA in the main list 
otherStr = replaceMultiple(mainStr, ['s', 'l', 'a'] , "AA")
print(otherStr)  

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


