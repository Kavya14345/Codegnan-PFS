'''                    
Conditional statements:
-----------------------
elif Condition:
----------------
--> used to check more conditions
eg:
std_marks=int(input("Enter marks: "))
if std_marks>=90:
    print("A")
elif std_marks>=80:
    print("B")
elif std_marks>=70:
    print("C")
elif std_marks>=60:
    print("D")
elif std_marks>=50:
    print("E")
elif std_marks>=35:
    print("Pass")
elif std_marks>=0:
    print("Fail")

eg-2:
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print(f"{num1} is the greater than {num2} and {num3}")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater than {num1} and {num3}")
elif num3>num1 and num3>num2:
    print(f"{num3} is greater than {num1} and {num2}")

Nested-if:
----------
-->declaring if statement in if statement
eg:
SBI_bank={"ATM PIN":"6600"}
pin=input("Enter your 4-digit ATM Pin number:")
if len(pin)==4:
    if pin in SBI_bank['ATM PIN']:
        print("you can withdraw your money")
    else:
        print("Invalid pin")
else:
    print("Please enter your 4 digit pin")

For statement:
-------------
--> used to iterate over a sequence.
eg:
any="kavya"
for i in any:
    print(i)

range()
-------
range() is in-built function use to generate number in sequential manner
syntax: range(start,end,step-optional)
eg:
for i in range(63,200,4):
    print(i)

else in for
-----------
--> once the iterations completed this else will be executed
eg:
for i in range(1,10,2):
    print(i)
else:
    print("end of the code")


While Loop
----------


Control Statements
==================
1. break
--> used to exit from the loop based on the condition
eg:
for i in range(1,10):
    print(i)
    if i==5:
        break

2. continue
--> skips the current iteration matched with the condition
eg:
for i in range(1,10):
    if i==5:
        continue
    print(i)

3. pass
--> it is a space holder
eg:
for i in range(1,10):
    if i==3:
        pass

'''
i=int(input())
while i<5:
    print(i)
    i+=1
























