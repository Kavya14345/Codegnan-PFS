'''
(+) - Plus symbol
------------------
for numbers (int) it adds, but for the other datatypes it will act as concatinating the data type.
eg:
a=90
b=8
print(a+b) # do addition
any="Python "
so="is a language"
print(any+so) #do concatenation
an=[1,2]
am=[3,4]
print(an+am) #do concatenation

tuple
------
--> collection of different datatypes ,separated by commas and represented in parenthesis()
-->immutable
eg:
some=(1,"Python",[1,2],(3,4))
print(some[2][1])
print(some[1])
print(some.index((3,4))) #to find the index
print(some)

Methods:
-------
1. count()
--> this is used to count the particular item in the tuple
syntax--> variable_name.count(item)
eg:
some=(1,"Python",[1,2],(3,4),"Python")
print(some.count("Python"))

2. index()
--> used to find out the index position of the item and only gives the first occurrence

eg:
some=(1,"Python",[1,2],(3,4))
print(some[2][1])
print(some[1])
print(some.index((3,4))) #to find the index

first occurrence eg :
some=(1,"Python",[1,2],(3,4),"Python")
print(some.index("Python"))

any=(1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4])
print(any.index(34))
print(any[2][2][1][8])
print(any.index("python"))


Dictionary
----------
--> Dict is a key: value pair, key and value is separated by : and pair is separated by comma and only strings,tuple,numbers are used in keys
--> represented in {} , might have duplicate values not keys
eg:
details={"name": "kavya",
         1:2,
         (1,2):[3,4]}
print(type(details))
print(details)

methods
--------
1. keys()
--> used to get all keys from the dict
syntax---> dict.key()
eg:

details={"name":"kavya",
         "age":21,
         "mobNo":"1232343454",
         "pan":"ygsdhcgsvcgh"}
print(details.keys())

2. values()
--> used to get all values from the dict
syntax --> dict.values()

eg:
details={"name":"kavya",
         "age":21,
         "mobNo":"1232343454",
         "pan":"ygsdhcgsvcgh"}
print(details.values())

3. items()
--> used to get the both keys and values together as items in the dict
syntax --> dict.items()
eg:
details={"name":"kavya",
         "age":21,
         "mobNo":"1232343454",
         "pan":"ygsdhcgsvcgh"}
print(details.items())

details={"name":"kavya",
         "age":21,
         "mobNo":"1232343454",
         "pan":"ygsdhcgsvcgh"}
print(details["name"])  #get value by taking key

4. update()
--> used to add a new key:value pair into dict
syntax--> dict.update({key:value})
eg:
details={"name":"kavya",
         "age":21,
         "mobNo":"1232343454",
         "pan":"ygsdhcgsvcgh"}
details.update({"aadhaar":"7472642534623"})
details["name"]="kanchana" #updates old value
details["aadhaar"]="3647237873254" #updated aadhaar new key's value also
print(details)

5. clear()
--> used to remove all the items in the dict
syntax-->dict.clear()
eg:
details={"name":"kavya",
         "age":21,
         "mobNo":"1232343454",
         "pan":"ygsdhcgsvcgh"}
details.clear()
print(details)

'''




