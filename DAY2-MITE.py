# -*- coding: utf-8 -*-
"""
Created on Mon Jul  10 18:20:57 2018
DAY-2-MITE, MANGALORE
@author: pooja
"""
"""
Lists are a mutable data type. 

Series of elements in [square brackets] separated by commas. 

Elements can be of different data type.
"""
#list
l=[1,2,3,4,5,8]
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
l2.remove(5)#When you know the element you want to remove
l2.reverse()

List = [ 19, True, 'Charts', 3.1459 ]
List[0] = True
List[1] = 24
List[3] = 'Books'
for i in List:
    print(type(i))

l1 = ['a', 'b', 'c']
l2 = ['d', 'e']
l1.extend(l2) 
print( l1)

#don't need the removed value, use the del operator:

l = ['a', 'b', 'c']
del l[1] 
print (l)

#del more than one item
l = ['a', 'b', 'c', 'd', 'e', 'f'] 
del l[1:5] 
print (l)


"""
TUPLE
can hold any data type 
values separated by commas, 
Enclosed in (parenthesis) 
"""
T = (1, 6, False, True, 'wow',35.3)
#(11) is NOT a tuple (it's a 4 in parenthesis)‏
#(11,) is a tuple of length 1 (note the trailing comma)‏
#Tuples are good when you want to group a few variables together
#(firstName, lastName)   (x,y)
"""
IMMUTABLE
"""
t = (11, 22, 33)
t1 = t
t += (44,)
print(t)
print(t1)
"""
TRY THIS
"""
T= (11, 22, 33)
T=T+(11)

"""
SORTING?
"""
T= (100,11, 22, 33)
print(sorted(T))

t1=('a','g','e')
sorted(t1)





"""
Sequence to tuple
"""
a= "I belong to India"
at = tuple(a)
print(at)

a=1000






"""
DICTIONARIES

use ANY immutable data type as an index. 
associate a key (unique), with a value (any data).
{key:value, key:value.....}
Key and values are separated by a colon 
Paris of entries are separated by commas
Dictionary is enclosed within curly braces
"""
#Retrieving value
D= { 1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V' }
D[1]
D[2]
#assigning new values to existing keys
D[1] = 'one'
print(D[1])

l=['one','two','three','four','five']
D.values()
D.keys()
D.items()

d1={1:123,2:[12,22,33], 3:['item1','item2','item3']}
    
d1[1]
d1[2][2]
d1[3][0]

d2={1:{'A':'Apple', 'B': 'Ball','C':{1:'Cam',2:'Car'}},2:123}
    
d2[1]['A'].upper()
d2[1]['C'][2] 
d2[2]  = d2[2]+5  
    

#creating new key/value pairs
D[10]	= 'X'
print(D[10])

"""
get( INDEX, DEFAULT) 
"""

d2.get(3,'None')	
D.get(5, 'None') 	
D.get(500, 'NONE')	
D.get('test', 'None')   

age = {'Alice' : 25, 'Carol': 'twenty-two'}
age.items()		
age.keys()		
age.values()	


age = {'Alice': 26 , 'Carol' : 22}
age.update({'Bob' : 29})	
age.update({'Carol' : 26})

"""
SETS
Sets are an unordered collection of unique elements. We can construct them by using the set() function. Let's go ahead and make a set to see how it works
"""
X  = set() 
X.add(1)
print(X)









"""  
note the curly brackets. This does not indicate a dictionary! 
Although you can draw analogies as a set being a dictionary with only keys.
We know that a set has only unique entries. 
So what happens when we try to add something that is already in a set?
"""
# add a different element 
X.add(2) 
print(X) 
# try to add the same element 
X.add(1) 
"""
notice how it won't place another  there. 
That's because a set is only concerned with unique elements! 
We can cast a list with multiple repeat elements to a set to get the unique elements.
"""
# Create a list with repeats 



list1 = [1,1,2,2,3,4,5,6,1,1] 
# Cast as set to get unique values 
set(list1) 


s='this is supposed to be a very difficult day for students, who are going for a picnic. Today it is raining heavily and weather deaprtment has issued a warning too.'





"""
Booeans Python comes with ooleans (with predefined True and False displays that are basically just the integers  and ). It also has a placeholder object called one. Let's walk through a few quick examples of ooleans (we will dive deeper into them later in this course).
"""
# Set object to be a boolean 
a = True 
print(a)


"""
We can also use comparison operators to create booleans. """

b=3
c=7
print(b>c)
print(b<c)




















