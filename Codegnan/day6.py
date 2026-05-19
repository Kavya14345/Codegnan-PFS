'''
type conversions
-----------------
int-->
eg:
an=78
us=str(an)
om=float(an)
l=list(an) #can't do this
print(om)
print(type(om))
print(type(us))

str-->can't do for string characters but int characters can be converted
eg:
an="908975"
us=int(an)
om=float(an)
l=list(an)
t=tuple(an)
print(om,us,l,t)
print(type(om))
print(type(us))
print(type(l))
print(type(t))

float-->
eg:
an=5654.5553
us=int(an)
om=float(an)
# can't do this l=list(an) t=tuple(an)
s=str(an)
print(om,us,s)
print(type(om))
print(type(us))
# print(type(l)) print(type(t))
print(type(s))

list-->
eg:
an=[3,32,12,65,67]
# can't do this us=int(an) om=float(an)
l=list(an)
t=tuple(an)
s=str(an)
print(l,t,s)
# print(type(om)) print(type(us))
print(type(l))
print(type(t))
print(type(s))

tuple-->
eg:
an=(3,32,12,65,67)
#us=int(an) om=float(an)
l=list(an)
t=tuple(an)
s=str(an)
print(l,t,s)
# print(type(om)) print(type(us))
print(type(l))
print(type(t))
print(type(s))

Userinput
=========
1. int as a user-input
----------------------
num=int(input("Enter a number: "))
print(45+num)

2. str as a user-input
----------------------
num=str(input("Enter a number: "))
print("kavya"+num)
o/p:
Enter a number: 73734623
kavya73734623

3. list as a user-input
-------------------------
num=input("Enter a number: ").split()          o/p: Enter a number: 34 nd 32   ['34', 'nd', '32']
print(num)                                          Enter a number: kndjsbfjr['kndjsbfjr']

4. tuple as a user-input
------------------------
num=tuple(map(int,input("Enter a number: ").split()))
print(num)

5. for all datatypes
---------------------
num=eval(input("Enter:"))
print(type(num))

'''
