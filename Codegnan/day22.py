'''
Error Handling
--------------

1.try block
--> it will test a block of code for error

2.except block
-->the except block let handle if the code contain errors

try:
    print(a)
except:
    print('hai')

try:
    print(10/0)
except:
    print('this will handle ZeroDivisionError')

a=35
try:
    count(a)
except:
    print("hi")


    
3.else block
--> this will be executed , if the try block has no errors in the code

b='kavya'
try:
    print(b)
except:
    print("hi")
else:
    print("No error")

b=0
try:
    print(b)
    print(a)
    print(c)
    print("kavya"+a)
except TypeError:
    print("This will handle TypeError")
except NameError:
    print("This is will handle NameError")
else:
    print("No error")

Note:
only first error will be considered
programming rules error will not be considered

4.finally block
----------------
--> this will be executed either try block contain error or not
'''
try:
    print("hi")
except:
    print("Error")
else:
    print("No Error")
finally:
    print("The End")











































