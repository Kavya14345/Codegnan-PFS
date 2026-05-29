'''
List Comprehension
-------------------
-->It offers a shortest syntax when moving onto creating a new list from existing list 
syntax--> variable_name=[expression loop condition]
eg:
old=[1,2,3,4,5]
new=[so for so in old]
print(new)
o/p:
[1, 2, 3, 4, 5]

#to print even
old=[1,2,3,4,5,6]
new=[so if so%2!=0 else "even" for so in old ]
print(new)
o/p:
[1, 'even', 3, 'even', 5, 'even']

Generators
-----------
--> generators in python are a special type of itterable allows users to iterate over data efficiently without storing everything in memory.
--> They generate values lazily using yield keyword
eg:

def simple_gen():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("end")
gen=simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
o/p:
Start
1
2
3
end


Why to use gen
--------------
--> Generators do not store the entire dataset in memory, they generate values on the run time
--> Avoiding unnecessary storage of data speed up execution.
--> also used in pipelines topic

how it works:
------------
it looks like normal function but uses the yield keyword instead of return
when the function is called it does not execute immediately, instead , it returns a generate object which can be iterated using loop on the next() function

normal function vs generators
------------------------------
def any(num):
    for i in range(1,num+1):
        yield i*i
a=any(5)
print(next(a))
print(next(a))

def sqr(num):
    res=[]
    for i in range(1,num+1):
        res.append(i*i)
    return res
print(sqr(5))
o/p:
===
1
4
[1, 4, 9, 16, 25]

problem-1:
def vowel():
    so=input()
    any=''
    for j in so:
        if j not in "aeiouAEIOU":
            any+=j
    print(any)
vowel()

'''















