'''
a = list("ABCDEF")
for i, value in enumerate(a):
    print(i, end="  ")
    print(value+"s")
'''


import random
e=0
while e>-2:
    e = random.gauss(0,1)
    print(e)
    #if e<-2:
        #break
print("END")


#실습 코드

data_file = open('us_cities.txt','r')
data_file

next(data_file)
temp = next(data_file)
temp
type(temp)

temp2 = temp.split(":")
temp2
temp2[0]
temp2[1]
int(temp2[1])

temp = next(data_file)
temp
temp2 = temp.split(":")
temp2
temp2[1]

a = temp2[1]
a = a.rstrip("\n")
a

a = [1,2,3]
# next(a)  #error: list is not an iterator
b = iter(a)
b
next(b)

a = range(10)
a
list(a) 
a
#next(a) #error: range is not an iterator either
b = iter(a)
b
next(b)

list("ABCE")


b=  enumerate(a)
next(b)

f = open("us_cities.txt",'r')


a = 10
a = a + 1
a
a += 1
a

a
a *= 2
a
a = a*2

import random
random.gauss(10,20)

import datetime
import datetime as dt
dt

from datetime import datetime
datetime
from datetime import date
date

import random
from random import gauss
gauss(0,1)

import scipy.stats
scipy.stats.norm.cdf(0)
scipy.stats.norm.cdf(-1)

import scipy.stats as ss
ss.norm.cdf(0)

from scipy.stats import norm as foo
foo.cdf(0)


a>50
not a>50

x = 100
if x>90:
    y = "G"
else:
    y = "L"
    
y
y = "G" if x>90 else "L"
y
y = "G" if x>90 else "L" if x>70 else "A"
x = 75
y = "G" if x>90 else "L" if x>70 else "A"
y
x = 50
y = "G" if x>90 else "L" if x>70 else "A"
y
y = "G" if x>90 else ("L" if x>70 else "A")

a = list(range(-5,6))
a
b = [0 if x<0 else 1 for x in a]
b
b = [int(x>=0) for x in a]
b
b = [x for x in a if x>0]
b
#b = [x for x in a if x>0 else x**2]  #Wrong
b = [x if x>0 else x**2 for x in a]
b
#b = [x if x>0 for x in a]  #Wrong


b = [x+1 for x in a]
b
b = [x+1 for x in a if x>0]
b
b = [x+1 if x>0 else x-1 for x in a]
b
a,b,c=[],[],[]
    
