'''
Nested Loops
============
eg:
for i in range(1,10):
    for j in range(1,2):
        print(j)

eg:
num=int(input())
for i in range(1,11):
    print(f"{num}X{i}={i*num}")

eg:
so="Python"
print(so[::-1]) #reverse the string
    (or)
so=input("enter a word:")
string=""
for j in so:
    string=j+string
print(string)

eg:
so=input("enter a word:")
string=""
for j in so:
    string=j+string
if string==so:
    print(f"{so} is a palindrome")
else:
    print(f"{so} is not a palindrome")

eg:
num=int(input("Enter a number:"))
length=len(str(num))
arm=0
for i in str(num):
    arm+=int(i)**length
if arm==num:
    print(f"{num} is an armstrong")
else:
    print(f"{num} is not an armstrong")

eg:
num=int(input())
fac=0
for i in range(1,num):
    if num%i==0:
        fac+=i
if fac==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

eg:
num=int(input())
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

eg:
num=int(input())
for i in range(1,num+1):
    print(i*'*')

eg:
alp=int(input())
for i in range(1,alp+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()

eg:
num=int(input())
count=0
for i in range(1,num+1):
    for j in range(1,i+1):
        count+=1
        print(count,end=" ")
    print()

eg:
num=int(input())
count=0
for i in range(1,num+1):
    for j in range(1,i+1):
        count+=1
        print(i,end=" ")
    print()

eg:
num=int(input())
count=0
for i in range(num,0,-1):
    for j in range(1,i+1):
        count+=1
        print('*',end=" ")
    print()

eg:
num=int(input("Enter height of the triangle:"))
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()

eg:
num=int(input("Enter height of the triangle:"))
for j in range(num,0,-1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()

'''


