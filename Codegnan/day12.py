'''
Built-in functions
------------------
print()
input()
len()
max()
min()
type()
sorted()
sort()
eg:
--sorted() VS sort()----
m=[2,1,3,2,3]
print(sorted(m)) #doesn't modify m
print(m)
m.sort() #modifies m
print(m)

======Recursive Functions=====
--> A recursive function that calls itself to solve a problem by breaking it into small or simple sub-problems.
eg:
def fact(num):
    if num==1:
        return 1
    return num*fact(num-1)
print(fact(5))

return()
---------
-->this ends the function execution and sends a value back to the code that called the function,it just holds the value
eg:
def add(a,b):
    return a+b
add(4,5) #it just holds the return o/p value but does not display
res=add(4,5)
print(res)

lambda functions
-----------------
-->also called as single line function
-->it is a small anonymous functions, it will take 'n' no of arguments, but only single arguments only(not multiple expressions)
syntax -->  lambda arguments: expression
eg:
crct
so=lambda a,b,c: a+b+c
print(so(3,4,2))

so=lambda a,b,c: a**b+c
print(so(3,4,2))
so=lambda a,b,c: a+b+a+c
print(so(3,4,2))

error
so=lambda a,b,c: a+b,c+c
print(so(3,4,2))

'''



