# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 18:48:46 2018
Day 2: MITE, Mangalore
@author: pooja
"""

#LIST COMPREHNSION

s='word'
l=[]
for i in s:
    l.append(i)

l1=[i for i in s ] 
l2=[x*2 for x in range(0,10)]

l3=[x**2 for x in range(0,10)]
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 11:35:06 2018

@author: pooja
"""

#List comprehension

s='word'
l=[]
for i in s:
    l.append(i)

l1=[i for i in s ] 
l2=[x*2 for x in range(0,10)]

l3=[x**2 for x in range(0,10)]

l4=[x for x in range(0,10) if x%2==0 ]

c=[25, 25.6,34,456,78,89]
tf=[9/5*x+32 for x in c]

lnt=[x**2 for x in [x**2 for x in range(11)]]

l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
mat=[l1,l2,l3]
matlc=[item[1] for item in mat]

lz=zip(l1,l2)

for i in lz:
    print(i)

lzc=[i for i in zip(l1,l2)]

def square(num):
    return num**2
    
square=lambda num: num**3

square(56)

names=['Pooja','Aman','Manisha','Sophia','Shravan','Varun','Jerry']
list(map(lambda s: s[::-1], names))


l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]

list(map(lambda x,y:x+y, l1,l2))
list(map(lambda x,y,z:x+y+z, l1,l2,l3))

d1={1:'A', 2:'B'}
d2={3:'C', 4:'D'}
list(zip(d1,d2.values()))

#enumerate()

l=['a','b','c']
for num,item in enumerate(l):
    print(item)
    print(num)

l=['June', 'July', 'August']
list(enumerate(l, start=6))
l=[False, 0,0,0]
all(l)
any(l)
l1=[True,1,1]
all(l1)
any(l1)
square(145)
nums=[5,56,48,45]
l=[]
for i in nums:
    l.append(square(i))
    
l=[square(i) for i in nums]    
    
list(map(square,nums))

"""
'word'
output: 'even'
'sixty'
output: 's'
"""
def myfunc(string):
    if len(string)%2==0:
        return 'even'
    else:
        return string[0]

names=['Pooja','Aman','Manisha','Sophia','Shravan','Varun','Jerry']

list(map(myfunc,names))
"""
--------------------------------------------------------------------------
"""
#display 420 without using integer
print(int((str(0b100)+str(0b10)+str(0b00))))

s=str(0b100)
s1=str(0b10)
s3=str(0b00)
print(int(s+s1+s3))
print(ord('A'))
#---------------------------------------------------------------
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:17:11 2018

@author: pooja
"""

#display 420 without using integer
print(int((str(0b100)+str(0b10)+str(0b00))))

s=str(0b100)
s1=str(0b10)
s3=str(0b00)
print(int(s+s1+s3))
print(ord('A'))

"""
WAP take a sentence as an input
is any letter in it is 'A' or 'a'
convert it to 'X'
return the updated sentence.
"""
def changestring(string):
    l=string.split()
    l1=[]
    for i in range(len(l)):
        if l[i]=='A' or l[i]=='a':
            l[i]='X'
        return ''.join(l)
print(changestring('WAP take a sentence as an input'))         
#            ............................

phrase = "A bird in the hand..." 
for char in phrase:   
    if char=='A' or char=='a':     
        print ("X",)   
    else:     
        print (char,) 




for i in 'word':
    print(i)


for i in 'word':
    print(i,end='')

def factorial(x):   
    fac=1 
    if x==1 or x==0:     
        return 1   
    else:     
        for i in range(1, x+1):       
            fac=fac*i   
        return fac 
"""
Displays which Letters are in the 
First String but not in the Second
"""
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)-set(s2))

print("The letters are:")
for i in a:
    print(i)
"""

Modify the following replace function 
so that where the first occurrence 
of replace_string in test_string is 
replaced by bodega.  
Tests:  
replace("Hi how are you?", "you") should return 
"Hi how are bodega?"  
replace("Love is in the air", "air") should return
 "Love is in the bodega"

"""
test_string='How are you today'
replace_string='you'
def replace(test_string, replace_string):  
    x=test_string.find(replace_string)  
    t=test_string[x:]  
    x1=t.find(' ')  
    s='bodega'  
    if x1<0:      
        transformed_string=test_string[0:x] + s  
    else:      
        transformed_string=test_string[0:x]+s+t[x1:]  
    return transformed_string  

    
    """
Remove the nth Index 
Character from a Non-Empty String
"""
def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last     
      
      
string=input("Enter the sring:")
n=int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))


"""
to Detect if Two Strings are Anagrams
"""




s1=input("Enter first string:")
s2=input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")

      
"""
to Read a List of Words and 
Return the Length of the Longest One
"""
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The word with the longest length is:")
print(temp)

"""
Program to Check if a Number is a Palindrome
"""
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
"""
Define a function scrabble_score that takes a 
string word as input 
and returns the equivalent scrabble score for that word.
 
Assume your input is only one word
 containing no spaces or punctuation. 
As mentioned, no need to worry about score multipliers! 
For example: the word "Helix" would score 
15points due to the sum of the 
letters: 4 + 1 + 1 + 1 + 8. 
"""
score = {"a": 1, "c": 3, "b": 3, "e": 1, 
"d": 2, "g": 2, "f": 4, "i": 1, 
"h": 4, "k": 5, "j": 8, "m": 3, 
"l": 1, "o": 1, "n": 1, "q": 10, 
"p": 3, "s": 1,"r": 1, "u": 1, "t": 1, 
"w": 4, "v": 4, "y": 4,"x": 8, "z": 10}
def scrabble_score(word):   
    word=word.lower()   
    total=0   
    for w in word:     
        total=total+score[w]   
    return total
scrabble_score('wordofthemonth')


#---------------------------------------------------------------
hobbies = [] 
for i in range(3):   
    hobby=input("Enter your hobby:" )   
    hobbies.append(hobby) 
    print(hobbies) 
#------------------------------------------ 
phrase = "A bird in the hand..." 
for char in phrase:   
    if char=='A' or char=='a':     
        print ("X",)   
    else:     
        print (char,) 
#-----------------------------------------      
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'} 
for key in d:   print (key,d[key]) 
#------------------------------------------------ 
choices = ['pizza', 'pasta', 'salad', 'nachos'] 
print ('Your choices are:') 
for index, item in enumerate(choices):   
    print (index+1, item) 
#--------------------------------------------------   
list_a = [3, 9, 17, 15, 19] 
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90] 
for a, b in zip(list_a, list_b):   
    if a>b:     
        print (a)   
    else:     
        print (b) 
#------------------------------------------------------------------ 
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape'] 
print ('You have...') 
for f in fruits:   
    if f == 'tomato':     
        print ('A tomato is not a fruit!')      
        break   
        print ('A', f) 
    else:   
        print ('A fine selection of fruits!') 
#----------------------------------------------------------------------- 
def is_int(x):   
    absolute = abs(x)   
    rounded = round(absolute)   
    return absolute - rounded == 0 
 #---------------------------------------------------------------------- 
def factorial(x):   
    fac=1 
    if x==1 or x==0:     
        return 1   
    else:     
        for i in range(1, x+1):       
            fac=fac*i   
            return fac 
#---------------------------------------------------------------------- 
def is_prime(x):   
    if x>1:     
        for n in range(2,x):       
            if x%n==0:         
                return False     
            else:       
                return True   
        else:     
            return False 
#-------------------------------------------------------------------- 
def reverse(text):   
    t=""   
    x=len(text)-1   
    while x>=0:     
        t = t+text[x]     
        x-=1   
        return t 
#----------------------------------------------------------------------   
""" Modify the following replace function so that where the first occurrence 
of replace_string in test_string is replaced by bodega.  
Tests:  
replace("Hi how are you?", "you") should return "Hi how are bodega?"  
replace("Love is in the air", "air") should return "Love is in the bodega"
"""  




def replace(test_string, replace_string):  
    x=test_string.find(replace_string)  
    t=test_string[x:]  
    x1=t.find(' ')  
    s='bodega'  
    if x1<0:      
        transformed_string=test_string[0:x] + s  
    else:      
        transformed_string=test_string[0:x]+s+t[x1:]  
    return transformed_string  
    
    
""" 
Define a function scrabble_score that takes a string word as input 
and returns the equivalent scrabble score for that word. â€¢ 
Assume your input is only one word containing no spaces or punctuation. 
â€¢ As mentioned, no need to worry about score multipliers! 
For example: the word "Helix" would score 15points due to the sum of the 
letters: 4 + 1 + 1 + 1 + 8. 
""" 
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,"x": 8, "z": 10}  
def scrabble_score(word):   
    word=word.lower()   
    total=0   
    for w in word:     
        total=total+score[w]   
    return total  
""" 
Write a function called censor that takes two strings, text and word, as input.
It should return the text with the word you chose replaced with asterisks. 
For example:  
censor("this hack is wack hack", "hack") should return:  
"this **** is wack ****" 
Assume your input strings won't contain punctuation or upper case letters. 
The number of asterisks you put should correspond to the number of letters
in the censored word.  
""" 
def censor(text,word):   
    s=text.split()   
    for i in range(len(s)):     
        if s[i]== word:       
            s[i]='*'*len(word)       
            text=" ".join(s)   
            return text  
censor("hi its a new begining", 'new') 

""" Define a function called count that has two arguments called sequence 
and item. Return the number of times the item occurs in the list. 
For example: count([1, 2, 1, 1], 1) should return 3 
(because 1 appears 3 times in the list). 
""" 
def count(sequence, item):   
    count=0   
    for i in sequence:     
        if i==item:       
            count+=1   
            return count  
count([5,5,4,8,7,5,5], 5) 
""" 
Define a function called purify that takes in a list of numbers,  
removes all odd numbers in the list, and returns the result.  
For example, purify([1,2,3]) should return [2] 
""" 
def purify(l):   
    l1=[]   
    for i in l:     
        if i%2==0:       
            l1.append(i)   
            return l1 
purify([4,8,9,6,5,5,3,1,8])         
"""
Define a function called product that takes a list of integers as input  
and returns the product of all of the elements in the list.  
For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100). 
""" 
def product(l):   
    s=1   
    for i in l:     
        s=s*i   
        return s 
product([5, 6, 4])
""" 
Write a function remove_duplicates that takes in a list and  
removes elements of the list that are the same. 
For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2]. 
""" 
l=[4,8,9,6,5,5,3,1,8] 
def remove_duplicates(l):   
    l1=[]   
    for i in l:     
        if i not in l1:       
            l1.append(i)   
            return l1 
remove_duplicates(l)  

def median(l): 
  x=int(len(l)/2)   
  l=sorted(l)   
  median = (l[x - 1] + l[x]) / 2.0   
  return float(median)  

""" Write a function called median that  takes a list as an input and 
returns the median value of the list. 
For example: median([1, 1, 2]) should return 1. 
""" 
def median(l):   
    x=len(l)   
    l=sorted(l)   
    if x==1:       
        median = l[0]   
    elif x%2==0:       
        x=int(x/2)       
        median = (l[x - 1] + l[x]) / 2.0   
    else:       
        x= int((x/2)+0.5)       
        median = l[x]   
    return float(median) 
l=[6, 8, 12, 2, 23]  
median(l=[1]) 
#function to print out the list of grades, one element at a time. 
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5] 
def print_grades(grades_input):   
    for i in grades_input:     
        print(i) 
print_grades(grades)  
""" define a function, grades_sum, that does the following:  
Takes in a list of scores, scores Computes the sum of the scores 
Returns the computed sum. Call the newly created grades_sum function  
with the list of grades and print the result. 
""" 
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5] 
def grades_sum(l):   
    sum=0   
    for i in l:     
        sum+=i   
        return sum 
print (grades_sum(grades)) 
#finding average 
def grades_average(grades_input):   
    l=float(len(grades_input))   
    avr=grades_sum(grades_input)/l   
    return avr 
print(grades_average(grades)) 
#computing grade variance 
def grades_variance(score):   
    avr=grades_average(score)   
    variance=0   
    for s in score:     
        a=(avr-s)**2     
        variance=variance+a   
        total = variance/len(score)   
        return total 
print(grades_variance(grades)) 
#computing std dev 
def grades_std_deviation(variance):   
    return variance**0.5 
variance=grades_variance(grades) 
print(grades_std_deviation(variance))  
#EXAMPLE OF LIST COMPREHENSION  
#even numbers between 0-50 
evens_to_50 = [i for i in range(51) if i % 2 == 0] 
print (evens_to_50)  
#square of even numbers between 1-11 
even_squares = [x**2 for x in range(1,11) if (x%2==0)] 
print (even_squares)

""" 
Use a list comprehension to create a list, cubes_by_four. 
The comprehension should consist of the cubes of the numbers 1 through 10 
only if the cube is evenly divisible by four. Finally, print that list 
to the console. 
""" 
cubes_by_four = [x**3 for x in range(1,11) if (x**3)%4==0] 
print (cubes_by_four)
#printing only odd indices using stride 
my_list = [1,3,4,2,5,6,7,12,34] 
# List of numbers 1 - 10 
print (my_list[::2]) 
#A negative stride progresses through the list from right to left. 
backwards=my_list[::-1] 
print(backwards)  
''' LAMBDA FUNCTION ''' 
languages = ["HTML", "JavaScript", "Python", "Ruby"] 
print (filter(lambda x: x=='Python', languages)) 
squares=[x**2 for x in range(1,11)] 
print(filter(lambda x: 30<x<70, squares)) 
""" 
Use a list comprehension to create a list, threes_and_fives, 
that consists only of the numbers between 1 and 15 (inclusive) 
that are evenly divisible by 3 or 5. 
""" 
threes_and_fives=[x for x in range(1,16) if (x%3==0 or x%5==0)] 
#extract out the message..it is reversed and message is every other letter 
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI" 
message=garbled[::-2] 
""" 
Create a new variable called message. 
Set it to the result of calling filter() 
with the appropriate lambda that will filter out the "X"s. 
The second argument will be garbled. Finally, print your message to the console. 
""" 
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX" 
message=filter(lambda x:x!='X',garbled ) 
print (message) 
"""
In Python, you can write numbers in binary format by starting the number with 
0b.
"""
print (0b1)
print (0b10)   
print (0b11)   
print (0b100)  
print (0b101)
print (0b110)
print (0b111)
print ("******") 
print (0b1 + 0b11) 
print (0b11 * 0b11)

"""  
In order to print a number in its binary representation,  
you can use the bin() function. 
bin() takes an integer as input and  
returns the binary representation of that integer in a string.  
represent numbers in base 8 and base 16 using the oct() and hex() functions. 
""" 
print (bin(1)) 
print (bin(2)) 
print (bin(5)) 

""" 
int(): When given a string containing a number and the base that number is in,
the function will return the value of that number converted to base ten. 
""" 
print (int("1",2)) 
print (int("10",2)) 
print (int("111",2)) 
print (int("0b100",2)) 
print (int(bin(5),2)) 
# Print out the decimal equivalent of the binary 11001001. 
print (int("0b11001001", 2))  
#shift operator 
shift_right = 0b1100 
shift_left = 0b1 
shift_right=shift_right>>2 
shift_left=shift_left<<2 
print (bin(shift_right)) 
print (bin(shift_left))  
#and operator
print (bin(0b1110 & 0b101)) 
#or operator 
print (bin(0b1110 | 0b101)) 
#xor operator 
print (bin(0b1110 ^ 0b101)) 
#not operator 
print (~1) 
print (~2) 
print (~3) 
print (~42) 
print (~123)  
#masking 
""" 
Define a function, check_bit4, with one argument, input, an integer. 
It should check to see if the fourth bit from the right is on. 
If the bit is on, return "on" (not print!) 
If the bit is off, return "off". 
""" 
def check_bit4(input1):   
    mask=0b1000   
    a=input1&mask   
    if a>0:     
        return 'on'   
    else:     
        return 'off' 

        """ 
variable, a. Use a bitmask and the value a  in order to achieve a result 
where the third bit from the  right of a is turned on. 
Be sure to print your answer as a bin() string! 
"""
a = 0b10111011 
mask = 0b100 
b=a|mask 
print(bin(b)) 

""" 
8 bit variable a. Use a bitmask and the value a in order to  
achieve a result where all of the bits in a are flipped.  
Be sure to print your answer as a bin() string! 
""" 
a = 0b11101110 
mask=0b11111111 
b=a^mask 
print (bin(b)) 

""" 
Define a function called flip_bit that takes the inputs (number, n).  
Flip the nth bit (with the ones bit being the first bit) and store it in result.  
Return the result of calling bin(result). 
""" 
def flip_bit(number,n):   
    mask=(0b1<<n-1)   
    result=number^mask   
    return (bin(result))   

with open(“file.text”, “r”) as file: 
    data = file.readlines() 
    for line in data: 
        word = line.split() 
        print (word)










