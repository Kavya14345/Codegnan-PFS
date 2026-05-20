'''
Condition statements
--------------------
1. if
--> gives the output if condition is true
eg:
num=int(input())
if num%2==0:
    print(num)

2. if-else
-->else in the if statement , incase the condition becomes false then it will enter into fall-back(else), it will execute whatever inside it
eg:
num=int(input())
if num%2==0:
    print("even")
else:
    print("odd")

** f-string: calls the value of multiple variables in print statement using {}
eg:
num=6
print(f"{num} is even"}

program-1:
-----------
age=int(input("Enter a number:"))
if age>=18:
    print("We are eligible to vote")
else:
    print(f"we have to wait for {18-age} more years")

program-2:
----------
num1=8
num2=12
if num1>=num2:
    print(f"{num1} is greater number than {num2}")
else:
    print(f"{num2} is greater number than {num1}")

program-3:
-----------
year=int(input("enter an year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

program-4:
----------
vowel=str(input("Enter any alphabet:"))
if vowel in "aeiouAEIOU":
    print(f"{vowel} is a vowel")
else:
    print(f"{vowel} is a consonant")

program-5:
----------
num=int(input())
if num>=0:
    print(f"{num} is a positive integer")
else:
    print(f"{num} is a negative integer")

program-6:
----------
marks=input().split()
if int(marks[1])>=45:
    print(f"{marks[0]} is passed with marks {marks[1]}")
else:
    print(f"{marks[0]} is failed with marks {marks[1]}")

program-7:
----------
num=int(input())
if num%3==0 and num%5==0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

program-8:
-----------
signal=int(input("Enter \n1.Red \n2.Green:"))
if signal==1:
    print("Stop")
else:
    print("Go")
'''

