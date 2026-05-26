'''
assert
------
--> this is debugging statement used to test whether a condition is true
eg:
num=10
assert num>5
print("True")

num=10
assert num<5 # AssertionError
print("False")

to print condition for assert statment:
age=75
assert age>18,"Age is must be greater than 18"
print("Eligible")

Functions
----------
--> A block of code which only execute when it is called
--> you can pass data,known as parameters into function
--> To avoid repeated lines in code
-->
syntax: def function_name(parameters):  #defining function
            -------------------
            --------------------
        function_name(arguments)    #calling function
eg:
num=int(input())
def even(res):
    if res%2==0:
        print(f"{res} is even")
    else:
        print(f"{res} is odd")
even(num)

ways to pass arguments
----------------------
1. Required arguments
---------------------
-->A function must be called with the same no. of arguments otherwise throws typeerror
eg:
def even(res):
    if res%2==0:
        print(f"{res} is even")
    else:
        print(f"{res} is odd")
even(109,89)

2. Default arguments
---------------------
--> By default, values is defined at parameters even though it will take from arguments.
eg:
def val(name="Kavya"):
    print(name)
val("kavs") #takes arguments values as default value

3. Keyword arguments:
----------------------------
--> we can send arguments with key=value syntax. By this, the order of arguments does not matter...............
eg:
def even(sal,age,name):
    print(name)
    print(sal)
    print(age)
even(name="Kavya",age=34,sal=343454)

4. variable length arguments:
-------------------------------
-->adding a star(*) before the parameter name in the function, receive a tuple of arguments
and can access items with indexes.
eg:
def even(*name):
    print(name[0])  #access by index
even("Kavya","kavs","chintu")


pass by value vs pass by reference
name="kavya"
def even(any):
    print(any)
even(name)

# print prime numbers upto 100
def prime():
    for num in range(2, 101):
        count=0
        for i in range(1,num+1):
            if (num % i) == 0:
                count+=1
        if count==2:
            print(num)
prime()

# print user input tables
num=int(input("Table:"))
def tables():
    for i in range(1,11):
        print(f"{num}X{i}={i*num}")
tables()

# print reverse of the string
def rev():
    so=input()
    print(so[::-1])
rev()
       ---or----
def rev():
    so=input("enter a word:")
    string=""
    for j in so:
        string=j+string
    print(string)
rev()

# check a string palindrome or not
def palin_drome():
    so=input("enter a word:")
    string=""
    for j in so:
        string=j+string
    if string==so:
        print(f"{so} is a palindrome")
    else:
        print(f"{so} is not a palindrome")
palin_drome()

# check a number is an armstrong or not
def arm_strong():
    num=int(input("Enter a number:"))
    length=len(str(num))
    arm=0
    for i in str(num):
        arm+=int(i)**length
    if arm==num:
        print(f"{num} is an armstrong")
    else:
        print(f"{num} is not an armstrong")
arm_strong()

#perfect number
def perfect():
    num=int(input())
    fac=0
    for i in range(1,num):
        if num%i==0:
            fac+=i
    if fac==num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")
perfect()

#patterns

eg-1:
def pat_tern():
    num=int(input())
    for i in range(1,num+1):
        print(i*'*')
pat_tern()
o/p:
6
*
**
***
****
*****
******

eg-2:
def alpha():
    alp=int(input())
    for i in range(1,alp+1):
        for j in range(1,i+1):
            print(chr(64+j),end="")
        print()
alpha()
o/p:
6
A
AB
ABC
ABCD
ABCDE
ABCDEF

eg-3:
def num_ptn():
    num=int(input())
    count=0
    for i in range(1,num+1):
        for j in range(1,i+1):
            count+=1
            print(count,end=" ")
        print()
num_ptn()
o/p:
7
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 

eg-4:
def ind_ptn():
    num=int(input())
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()
ind_ptn()
o/p:
5
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

eg-5:
def rev_stars():
    num=int(input())
    for i in range(num,0,-1):
        for j in range(1,i+1):
            print('*',end=" ")
        print()
rev_stars()

o/p:
5
* * * * * 
* * * * 
* * * 
* * 
*


'''
num=int(input("Enter height of the triangle:"))
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()















