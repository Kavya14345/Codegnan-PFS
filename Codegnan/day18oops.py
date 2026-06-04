'''
oops
=====

1.Class
--> it is a blueprint or a template used to create object
eg:
class stu_:
    name='kavya'

class stu_:
    def edu_(self):
        print("I am studying in b.tech")
    def sports_(self):
        print("Cricket")
        print("tennis")
s1=stu_()
s1.edu_()
s1.sports_()
o/p:
I am studying in b.tech
Cricket
tennis

2.Object
--> an object is an instance of a class
eg:
class stu_:
    name='kavya'
s1=stu_()
print(s1.name)
o/p:
kavya

Attributes
----------
-->These are the variables that belongs to a class or an object.
class stu_:
    name='kavya'
    age=21
s1=stu_()
print(s1.name)
print(s1.age)

methods
--------
-->the functions defined inside the class is methods
class pfs:
    def py_thon(self):
        pfs_da='batch_03'
        print("This is pfs and da batch 3")
    def flask(self):
        pfs='batch_03'
        print("This is pfs batch 3")
a=pfs()
a.py_thon()
a.flask()

constructor()    __init__
-------------
--> a constructor is a special method that is automatically called when an object is created
eg:
class ATM:
    def __init__(self,Balance,name):
        self.Balance=Balance
        self.name=name
    def bal_check(self):
        print(f"{self.name} your total balance is {self.Balance+700}")
    def name_(self):
        print(self.name)
card=ATM(Balance=566566,name='kavya')
card.bal_check()
card.name_()

Access Specifiers
-----------------
1.public(no underscore)
--> this can be accessed from anywhere in the program
eg:
class stu_:
    name='kavya'
s1=stu_()
print(s1.name)
2.protected(_)
--> this is represented using a single underscore
eg:
class stu_:
    _name='kavya'
s1=stu_()
print(s1._name)#protected

3.private(__)
-->this is represented using double underscore
eg:
class stu_:
    __name='kavya'
s1=stu_()
print(s1._stu___name)#private

Encapsulation
-------------
-->is the process of binding data and methods together
eg:
class bank:
    def __init__(self,balance):
        self.__balance=balance
    def depo_(self,amount):
        self.__balance+=amount
    def get_bala(self):
        return self.__balance
acc=bank(1000)
acc.depo_(738465)
print(acc.get_bala())


'''






































































































































































