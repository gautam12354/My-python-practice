!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  File Operation  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

# Opens/creates a new file for writing; the "w" method also creates the file for writing if the file doesn’t exist and overrides the file 
# ...if the file already exists; remember to close the file after writing to it to save the changes!
file = open("testfile.txt","w")         #creating a file  with write mode
 
#writing text to file
>>>file.write("Hello World")                          #writing in to it 
>>>file.write("This is our new text file")            #writing in to it
>>>file.write("and this is another line.")            #writing in to it
>>>file.write("Why? Because we can.")                 #writing in to it


# *** close file always after modification and then you can see the modification ***
>>>file.close()                                       


#"r" is the file access mode for reading and it is the default mode when opening a file
>>>file = open("testfile.txt", "r")
>>>file
<_io.TextIOWrapper name='testfile.txt' mode='r' encoding='cp1252'>

#checking the mode in which a file has been opened
>>>file.mode
'r'

# Method that returns the entire content of a file in the form of a string
>>> file.read()
'Hello World'

# Read only first 10 charactors
>>>print(file.read(10))

# Returns the file content one line a ta time, each time you use the method
>>>file.readline() 

#returns a list where each element is a line in the file
>>>file.readlines()

# Moving the cursor at the beginning of the file
>>>file.seek(0)
0

#checking the current position of the cursor inside the file
>>>file.tell()
0

#______________________________________#
# New File

>>>newfile = open("newfile.txt", "w")


# This method takes a sequence of strings as an argument and writes those strings to the file
>>>newfile.writelines(["Cisco", "Juniper", "HP", "\n"])

# Opening a file for appending
>>>newfile = open("newfile.txt", "a")

# Opens a file for both writing and reading at the same time
>>>newfile = open("newfile.txt", "w+")

# Opens for exclusive creation, failing if the file already exists
newfile = open("newfile.txt", "x")

# Checking if a file is closed
>>>newfile.closed


# Using the with-as solution, the files gets closed automatically, without needing the close() method
with open("python.txt", "w") as f:
	f.write("Hello Python!\n")

#Truncating files - the file should be open for reading AND writing, not just reading! 
>>>f = open("D:\\test.txt", "r+")

# This deletes all the content inside the file
>>>f.truncate()
                   

#Truncating files - the file should be open for reading AND writing, not just reading! 
>>>f = open("D:\\test.txt", "r+") 

#this will keep the first 10 characters in the file and delete the rest
f.truncate(10) 
                      
# Files - writing and appending to a existing file
>>>fh = open("hello.txt", "a")              #for append 
>>>fh.write("We Meet Again World") 
>>>fh.close 
