'''
Operators
---------
1. Arithmetic -  +,-,*,%,/,//,**

print(2*3)
print(4%5==0)
print(10**2) # ** -> exponential(power)
print(10/2)
print(32.20//5)

2. Assignment -  =,+=,-=,%=,*=

count=0
for j in range(1,10):
    count+=1 #works as count=count+1
print(count) # result=9

3. Comparision -  ==* ,!,>=,<=,>,<

a=7
b=9
print(a==b)

4. Logical - and(both should be true),or(either one is true is true),not

a=15
if a%3==0 and a%5==0:
    print("True")
a=20
if a%4==0 or a%7==0:
    print("True")

5. Membership - in , not in

a=7
b=[1,2,7,8]
print(a in b)
c=[1,2]
print(a not in c)

6. Identity - is* , is not

# difference b/w is* and ==*

num1=[1,2]
num2=[1,2]
c=num1
print(num1==num2) # == looks for both values are equal or not
print(id(num1))
print(id(num2))
print(id(c))
print(num1 is num2) #is* looks for object , search for whether they are in same location or not
print(c is num1)
print(num1 is not num2)
print(num1 is not c)

# Note: is operator looks for the objecct is same or not

7. Bitwise - &,|,<<,>>

print(5|3)
print(5&3)


print(type(num1)) # type is used to know the datatype

a=9 #immutable
b=7.0
print(a+b)

#Strings - it is sequence of char that are enclosed in ' ' , " " , ''''''
' ' , " ", '''''' (anything in between them) and immutable datatype
any="Python45,&"
print(any)

String Methods:
--------

1. replace()
-> used to replace with new substring
Syntax --->  variable_name.replace("Old string","new string")

any="Python is a language"
print(any.replace("Python","Java"))
print(any)

2. split()
-> used to separate into parts, and it will split based on the substring where before substring is one index and after is another index in the list
Syntax ---> variable_name.split("Substring")

any="Python is a language"
print(any.split())
print(any.split("is"))

3. len()
-> get number of items, substring
syntax ---> len(variable_name)

any="Python is a language"
print(len(any))

4. slicing()
-> can give the access to get particular index from the string
syntax ---> variable_name[starting index : ending index]

any="Python is a language"
print(any[3:10])

5. indexing()
-> used to get the substring present in that index position ....
syntax---> variable_name[index position]
'''

any="Python is a language"
print(any[7])
print(any.index("ang")) # gives the first undex of the substring position


# count,join















