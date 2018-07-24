# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:46:51 2018
DAY-1-MITE, MANGALORE
@author: pooja
"""
2+7# this is the first command for today
x=int(input('Enter any number'))

y=int(input('Enter any number'))
add = x+y
print("addition of x and y is :", add)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)

#STRINGS
s1 = 'Hello'
s2 = "I'm Pooja"
print(s1+' '+s2)
s3= s1+' '+s2
print(s1[4])

print(s3[-1])

print(s3[3:8])

print(s3[:])

print(s3[-8:-3])

print(s1.upper())
print(s3.lower())
print(s3.capitalize())
print(s1.isalpha())

'e' in s1



"""
WAP to display 'is there' and 'no-more'
if a character is there in a string or not.
user will provide a string
user will provide the character
"""

#loop
for i in  s1:
    print (i)

if ('i' in s1):
    print('jjkkk')
else:
    print("jdfhldskj")
    

s=input("Enter the string")
c=input("Enter the character")
if (c in s):
    print ("is there")
else:
    print ("no more")

l=[]
for i in range(len(s)):
    l.append(s[i])
    print(''.join(l))


string = "Computer"
for i in range(len(string)):
    print(string[0:i+1])


string = "Computer"
for i in range(len(string)+1):
    print(string[-i:])
    
i=1
while i in range(len(string)+1):
    print(string[-i:])
    i=i+1
    
"""
Ask the user to input a word in English.
Make sure the user entered a valid word.
Convert the word from English like this:-
Input : SUKUN
Output : UKUNSPK
[(2nd alphabet to end) + 1st alphabet + ‘PK’]
Display the translated result
"""
a = input (" ")
if a.isalpha():
    a=a.upper()
    a1=a[1:] + a[0]+'PK'
    print (a1)
else:
    print('invalid word')


s='This is a beautiful day as it is raining'
l=s.split()
"""
input a string
go through it, and if the length of a word 
is even, print 'Even' else print 'odd'
"""
s= input ("Enter the string")
for i in s.split():
    if len(i)%2==0:
        print("The word '{}' is Even".format(i))
    else:
        print('odd')

s='this is not fair to sart working today'
for i in s.split():
    if i.startswith('s'):
        print('True')
    else:
        print('False')
        
        
        
        
print('Insert one string : {}'.format(s))

students = 'Forty'
print('There are %s students in the class.' % students  )

students = 42
print('There are %d students in the class.' % students)




"""
WAP that prints the integers from 1to100. 
but for multiples of 3 print 'FUZZ'
and multiples of 5 print 'BUZZ'
for numbers which are multiple of both 3 and 5
print'FIZZBUZZ'
"""
for i in range(1,101):
    if (i%3==0 and i%5==0):
        print('FUZZBUZZ')
    elif (i%3==0):
        print('FUZZ')
    elif (i%5==0):
        print('BUZZ')
    
s='hello'
print(s*2)

#list
l2=[1,2,3,40,5,6,8,9,10]
l2=l*2
print(l2)
print(len(l))
for i in range(len(l)):
    print(l[i]*2)
l=['a','b','c','g','z']
s=''.join(l)
print(min(l))
print(min(l2))
print(l2[:3])
l2.append(89)
l2.pop()
l2.pop(3)
l2.remove(5)
l2.reverse()


www.dlithe.com/DLP

username:
password: Password@1234































