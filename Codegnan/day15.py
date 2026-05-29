'''
Modules
=======
--> modules in python is a file that contains python code such as
-variables
-functions
-classes
-statements

Two types of modules
---------------------
user_define:
eg:
#day15.py
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
#another file
import day15
print(day15.add(24,43))
print(day15.sub(34,23))
o/p:
67
11

built_in:

eg:
import math
print(math.sqrt(9))
print(math.factorial(9))
print(math.pow(9,2))
o/p:
3.0
362880
81.0

from math import sqrt
print(sqrt(9))
o/p:
3.0

import math as m
print(m.factorial(9))
print(m.pow(9,2))
o/p:
362880
81.0

import os
#os.mkdir("Demo.txt")
os.rmdir("Demo.txt")

import sys
print(sys.version)
print(sys.exit)
print(sys.path)

import random
print(random.random())
print(random.randint(1000,9999))
o/p:
0.0845006892040695
9127

from collections import Counter,defaultdict
data=['a','b','c','d']
counter=Counter(data)
print(counter)
dd=defaultdict(int)
dd['missing']+=1
print(dd['missing'])
o/p:
Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})
1
'''








































