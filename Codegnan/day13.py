'''
#Fibonacci series
------------------
def fibonacci():
    num=0
    num1=1
    n=int(input("Enter number of terms:"))
    print(num,num1,end=" ")
    for i in range(0,n-2):
        sum=num+num1
        num,num1=num1,sum
        print(sum,end=" ")
fibonacci()
o/p:
Enter number of terms:7
0 1 1 2 3 5 8

# Remove duplicates in list
def rem_dup():
    arr=list(map(int,input("Enter a list of numbers:").split()))
    any=[]
    for i in arr:
        if i not in any:
            any.append(i)
    print("By removing duplicates:",any)
rem_dup()
o/p:
Enter a list of numbers:5 5 32 5 6 7 8
By removing duplicates: [5, 32, 6, 7, 8]

# count words in paragraphs
def count_words():
    any=list(input("Enter any paragraph:").split())
    print(len(any))
    count=0
    for j in any:
        count+=1
    print(count)
count_words()
o/p:
Enter any paragraph:hi hello how are you code python kavya deepthi reshma kanchana
11
11




a=list(map(int,input().split()))
e=[]
o=[]
for i in a :
    if(i%2 == 0):
        e.append(i)
    else:
        o.append(i)
print(f"Even Numbers: {e}")
print(f"Odd Numbers: {o}")
print(max(set(a)))
print(min(set(a)))


a=tuple(input().split())
d={}
s=set(map(int,input().split()))
product=input("Product : ")
price=int(input("Price : "))
d[product]=price
print(f"Tuple : {a}")
print(f"Dictionary : {d}")
print(f"Set : {s}")






n=int(input())
a=0
b=1
c=0
fib=[]
print(0,1,end=" ")
for i in range(n-2):
    c=a+b
    if c>50:
        print()
        print("Loop Stopped")
        break
    a,b=b,c
    print(c,end=" ")
else:
    print()
    print("Loop Completed Successfully")



N=int(input())
assert N>0 , "Number must be Greater than 0"
i=1
while(i<=N):
    i+=1
    if(i%4 == 0):
        continue
    print(i,end=" ")
else:
    print("\nCompleted")

n=int(input())
sum=0
for i in range(0,n+1):
    for j in range(0,i+1):
        sum+=i
        print(sum)
        if sum>50:
            print()
            print("Loop Stopped")
            break
    else:
        print("Loop Completed Successfully")
'''
'''
#1.even or odd
num=list(map(int,input().split()))
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"Even Numbers:{even}")
print(f"Odd Numbers:{odd}")
print(max(num))
print(min(num))

#2.
t=input("Tuple:").split()
p=input("Product:")
pr=int(input("Price:"))
s=set(map(int,input().split()))
t1=tuple(t)
d[p]=pr
print(f"Tuple:{t1}")
print(f"Dictionary:{d}")
print(f"Set:{s}")

#3.
salary=int(input())
bonus=0
if salary>=70000:
    bonus=(20*salary)/100
elif salary>=50000:
    bonus=(15*salary)/100
elif salary>=30000:
    bonus=(10*salary)/100
else:
    bonus=(5*salary)/100
fbonus=float(bonus)
print(f"Bonus:{fbonus:-1f}")

#4.
n=int(input())
sum=0
for i in range(0,n):
    for j in range(0,i+1):
        sum+=j
        if sum<=50:
            print(sum,end="")
        else:
            break
else:
    print("Loop Completed Successfully")

n=int(input())
assert n>0;"Assertion Error:Number must be greater than 0"
while(n%4!=0):
    print(n,end="")
else:
    Continue
print("Completed")
'''


s=float(input())
if(s>=70000):
    b=(s*20)/100
    print(f"Bonus : {b}")
elif(s>=50000):
    b=(s*15)/100
    print(f"Bonus : {b}")
elif(s>=30000):
    b=(s*10)/100
    print(f"Bonus : {b}")
else:
    b=(s*5)/100
    print(f"Bonus : {b}")
