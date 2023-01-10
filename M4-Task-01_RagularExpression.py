'''
reg. exp. is a sequence of characters that forms a search pattern.
regex can be used to check if a string contains the specified search pattern.
python has a built-in package called re,which can be used to work with regular expressions.

'''

txt="the rain in spain"
x=txt.find("ai")    #this is not a regex function but a string function
print(x)
x=txt.find("ai",7)  #start finding with 7  index
print(x)

import re 
txt="the rain in spain"
x=re.findall("ai",txt)    #this is a regex function 
print(x)                  #o/p: ['ai', 'ai']
txt="the rain in spain"
x=re.findall("po",txt)    #this is a regex function 
print(x)                  #o/p: []

txt="the rain in spain"
x=re.search("\s",txt)
y=re.search("rain",txt)
print(x)                  #o/p:<re.Match object; span=(3, 4), match=' '>    
print(y)                  #o/p:<re.Match object; span=(4, 8), match='rain'>
                          #span(1st index where word find,last index till+1)
                          #furtur operation can be performe over match
print(y.span)             #<built-in method span of re.Match object at 0x013d2100>
print(y.group)            #<built-in method group of re.Match object at 0x013d2100>

print(y.span())           #(4, 8)(return the span of the word/character)
print(y.group())          #rain(actual word/set from the result)
print(y.start())          #4(starting index)
print(y.end())            #8(ending index+1)

#split a statement,based on a single space
x=re.split("\s",txt)
print(x)
#control the number of occurreneces by specifying the maxsplit parameter
x=re.split("\s",txt,1)
print(x)
#the sub() function replaces the matchs with the text of your choice
x=re.sub("\s","-",txt)
print(x)
x=re.sub("\s","_",txt,2)
print(x)
#MAtch object in regex
x=re.search("ai",txt)
print(x)
print(type(x))
print(x.start())        #return the start index
print(x.span())         #returns the span of the word/character
print(x.group())        #actual word/set. from the result
print(x.end())          #return the end index
x=re.search("pi",txt)   #o/p: none
print(x)

#match object
'''
-a match object is an object containing info. about the search and the result.
-if there is no match,the value none will be returned,instead of the match object.
'''

#find host or domain name from text provided
#1.First Approach (string functions):
data='from kajalrawat3603@gmail.com 12-12-2022 09:14:16'
    #through string
i=data.find("@")
print(i)
j=data.find(" ",i)
print(j)
print(data[i:j+1])
    #through regex
print(re.search("@.*",data).group().split()[0])
x=re.search("@.*",data)
print(x)
x=x.group()
print(x)
x=x.split()[0]
print(x)

#find date from a string
x=re.search("[0-9]{2}\-[0-9]{2}\-[0-9]{4}",data)
print(x.group())

#return all the words of a string that starts with vowel
x=re.findall("\\b[aeiouAEIOU]\S+.*",txt)
print(x)

#return the 1 word of given string8
print(re.split("\s",txt)[0])

#extract all words of a given string
print(re.split("\s",txt))
print(txt.split())

#split a string with multiple delemeters
print(re.split("\s|,|\.",txt))

# . ->fecth atleast one character from string
# * ->upto the end of the string(true for 0 or more)
# + ->upto the end of the string(true for 1 or more)
#\d ->for digit 
# \D ->for none digit                                               
#\\b ->for the beiging of a word
#\ ->escape(for searching a particular element ) 
#[ , ] ->fo giving a range          eg:[0-9],[a,z],[A,Z]
#\. -> to use . operator as character not as regex (keyword)
#^ ->
#{} ->repetation fetch
#? ->
#/w->[0-9],[a-z] [A-Z]
#/W->not of /w
txt1="a12a345678 a9hg u buy"
print(re.findall("\d",txt1))    #all digits fetch
print(re.findall("9\d",txt1))   #digit after 9
print(re.findall("\D",txt1))    #non digit character
print(re.findall("\S",txt1))    #for all characters
print(re.findall("\s",txt1))    #for spacing
print(re.findall("\A",txt1))    #for strings starting character
print(re.findall("\a",txt1))    #for
print(re.findall("\A1",txt1))   #for strings starting character
print(re.findall("\a",txt1))    #for
print(re.findall("\A",txt1))    #for strings starting character
print(re.findall("a?",txt1))    #a is optional 
print(re.findall("a?2",txt1))   #a is optional 
print(re.findall("a?.",txt1))   #a is optional
print(re.findall("a?",txt1))    #

#wap to find all the words start with vowel character
x=re.findall("\\b[aeiouAEIOU]\S+.*",txt)
print(x)

#wap to find all the words start with digit 
txt="12j 12 A 1esd Dfg "
x=re.findall("\\b[0-9]\S*",txt)
print(x)

#wap to fetch all the words which starts with a capital letter 
x=re.findall("\\b[A-Z]]\S.*",txt)
print(x)

# Q1 write a python program to find out all the words that  ends with  a vowel
txt="jgjge jho hgyi hkggj kjgyi ojsgsgh"
print(re.findall("\S*[aeiouAEIOU]\\b",txt))

# Q2 write a python program to find out all the words start with a digit.
txt="123dsgfd 767kjhy yujjbbj"
print(re.findall("\\b[0-9]\S*",txt))

# Q3. write a python program to fetch the date from a string and make sure out of range date should not be fetched.
txt="I have submitted my report to the department on 12.12.2022,12122022,40.34.2022"
x=re.search("([0-2][0-9]|[3][0-1]\.[0-1][0-2]\.[0-9]{4})",txt)
print(x.group())

#Q4. write a python program to fetch all the words which starts with a capital letter.
txt="klmojmjod jgjge hkggj ojsgsgh"
print(re.findall("\\b[A-Z]\S*",txt))

#Q5. write a python program that matches a string that has an a followed by either [A-Z] , [a-z] or [0-9]
txt="ihgiur jgj hkggj ojsgsgh"
x=re.search("a\w*",txt)
print(x)

#Q6. write a python program to search a string which start with y or Y or z or Z


#wap to fetch all the special symbols from the string


#wap to fetch all the words which contain only alphabt and should be of size 3
                                                            #^\w*[]
x=re.search("[a-z]\w*{3}",txt)
print(x)

