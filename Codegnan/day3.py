'''

1.Program to convert 24h clock into nrml clock

time="20:45"
parts=time.split(":")
print(parts) #gives as list
hours=int(parts[0])
mins=int(parts[1])
print(f"{time} is converted into {hours-12}:{mins}pm")

User Input:
----------
time=input("enter 24 hours time:")
parts=time.split(":")
print(parts) #gives as list
hours=int(parts[0])
mins=int(parts[1])
print(f"{time} is converted into {hours-12}:{mins}pm")


List
-----
-->List is a collection of different datatypes .It is represented in [] square brackets and separated by commas(,)
--> it is mutable
eg:
any=[1,"Kavya",[1,2]]
print(any)

any=[1,"Python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4]]
# for 'p' -> print(any[2][2][1][8])
# for 89 -> print(any[2][4])

List Methods
-------------
1. append() -> this method is used to add new item into list, and it will in the last index position.

syntax --> variable_name.append(item)
eg:
any=[1,2,3]
any.append(6)
print(any)
any.append(20)
print(any)

cannot add items but can add values is considered as 1 item
eg: 
any=[1,2,3]
# any.append(20,90)
# print(any)#gives error
any.append([20,90])
print(any) # gives answer

2. extend() -> This method is used to add iterable into list and it will in the last index position, each value or substring is each index in the list
syntax -> variable_name.extend(iterable)

eg:
any=[1,2,3]
any.append("Python")
any.extend("Python")
any.append("[4,5]")
any.extend("[4,5]") # gives separately
any.append([4,5])
any.extend([4,5])
print(any)

3. pop() -> used to remove the item from the list,but will mention here index position in the pop method
syntax -> variable_name.pop(index position)
eg:
any=[1,2,3,4,5,6]
any.pop() # by default removes last index 
print(any)
print(any.pop()) #shows which is removed
any.pop(2) # particular value will be removed in that index
print(any)

4. remove() -> directly removes the exact value in list
eg:
any=[1,2,3]
# any.remove() # gives error-it should have any argument
any.remove(1)
print(any)

-> string cannot be removed but string as a item in list can be removed
so=["Python",90,"Java"]  # removes string as item
so.remove("Python")
print(so)


Immutable(string) VS Mutable(list)
-----------------------------------
Immutable- could not be able to modify on that particular variable

mutable- can able to modify on that particular variable

eg:
so="Python is a"
so.replace("Python","Java")  
print(so)   # can't replace because string is immutable directly
print(so.replace("Python","Java")) # indirectly can do for just outside methods
any=[1,2,3]
print(any.append(6)) # gives None as result as it can modify directly which does not holds it
print(any) # gives modified list

'''


      
