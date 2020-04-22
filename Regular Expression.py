!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Reglar Expression !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Reglar Expression is a special sequence of charactor that helps you match or find other strings or set of strings using a specialized syntex held in pattern.
# ^ --> Matches begining of Line
# $ --> Matches end of line
#. --> Maches any single charactor except newline(using m allow it to match newline as well)
#[...] --> Matches any single charactor in brackets.
#[^...] --> Matches any single charactor not in brackets.
#re* --> Matches 0 or more occurences of preceding expression.
#re+ --> Matches 1 or more occurence of preceding expression.
#re? --> Matches o or 1 occurence of preceding expression.
#re{n} --> Matches exactly n number of occurence of preceding expression.
#re{n,} --> Matches n or more occurence of preceding expression.
#re{n,m} -->Matches atleast n and at most m occurence of preceding expression.
#a|b --> Matches either a or b.
#(re) --> Group regular expression and remember matches text


#Functions of Regular expression:
--Match  --> try to apply the pattern at the start of the string, returning a match object, or none if no match was found.
--Search --> Scan through string looking for a match to the pattern, returning a match object, or none if no match was found.
--Sub --> substitute
--subn --> 
--findall --> match all occurence of a pattern, not just the first one as searh() does.
--finditer
--purge
--split  --> split the sourse string by the occurence of the pattern, returning a list containing the resulting substring.

>>>import re                             #regular string module
>>>m = re.match("^123","123456789")      # check 123 is present at starting of the string or not (pattern, string, flag)(match check only begning of the string)
>>>print(m.group(0))                     # check for group 0
123

#Check charactors in ending of the string
>>>m= re.search("890$","1234567890")       #serach function search in all bengning,middle,end but match only check at begning.
>>>print(m.group(0))  

#findall function(Split string on base of pattern)
>>> m = re.findall("890","12345678901234567890123456789012345678901234567890123456789012345678901234567890")
>>>print(m)                                                                                                   #return match string in a list
['890', '890', '890', '890', '890', '890', '890', '890']    

#sun function
>>>m = re.sub("12","34","121212121212121212",2)            #replace(substitute) 12 by 34(old,new, string)[last n = 2 means only two time substitue]
>>>print(m)
343434343434343434

#split function
>>>m = re.split(",","1,2,3,4,5,6,7,8,9")              #split on the basis of pattern here on base of comma
>>>print(m)                       
['1', '2', '3', '4', '5', '6', '7', '8', '9']

>>> name = 'John Smith'
>>> first_name, last_name = name.split()
>>> print(last_name, first_name, sep=', ')
'Smith, John'

#________________________________________________#
#Validate Email syntex using regular expression

# \w   --> it is used for all a-z,A-z,0-9 All Alphanumeric Values and underscore
# (Dot.) --> In the default mode, this mathes any character expect new line 
>>>import re
>>>m= re.search(r"[\w]+@[\w]+[.][\w]+","test@gmail.comm")
>>>print(m.group(0))
test@dmail.com                                                   #print email only if syntext is right otherwise return none

#________________________________________________#
#Program for ip filtering and replace it with new one
import re
reg_exp = "([\d]{1,3}\.){3}[\d]{1,3}"   #[\d] it is for digit {1,3} --> it means three times only and {3} --> means it will come three times                                  
sub_str = re.sub(reg_exp,"0.0.0.0","Here Ip IS 12.34.56.22")       #replace reg_exp with 0.0.0.0 in string 
print(sub_str)

#________________________________________________#
#mac address substitution in string
import re
mac_add = "AB:CD:EF:12:A1:B3"                 #IN COMBINATION OF TWO DIGIT IN SIX SECTION
expr = "([A-Z0-9]{2}[:]){5}[0-9A-Z]{2}"              #
sub_str=re.sub(expr,"12:23:45:56:87:00",mac_add)
print(sub_str)

#________________________________________________#
#Extract E-mail from text
>>>import re                                                                               #import regular expression package
>>>text = "Please contact us at contact@tutorialspoint.com for further information."+\
        " You can also give feedbacl at feedback@tp.com"                                   #text containing Email   


emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)                      #Extract Email
print(emails)                                                                              #print 

#________________________________________________#
#Extract URL's From text
>>>import re
 
>>>with open("path\url_example.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            >>>print(urls)

