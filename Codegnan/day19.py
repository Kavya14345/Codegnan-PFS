'''
Inheritance:
=============
--> The inheritance allows one class to acquire the properties and methods of another class
types
-----
1.single inheritance
--> a child class inherits from a single parent class
eg:
class father:
    def land(self):
        print("My father having 5acres")
class kavs(father):
    def my(self):
        print("I own his")
fam=kavs()
fam.land()
fam.my()
o/p:
My father having 5acres
I own his

2.multiple inheritance
-->inheriting from multiple classes to acquire the properties and methods of another classes
class father:
    def land(self):
        print("My father having 5acres")
class mother:
    def gold(self):
        print("My mother having 1kg gold")
class kavs(father,mother):
    def my(self):
        print("I own both")
fam=kavs()
fam.land()
fam.gold()
fam.my()
o/p:
My father having 5acres
My mother having 1kg gold
I own both

3.multi-level inheritance
--> inheriting from a child class of a parent class to acquire the properties and methods of another classes
eg:
class grandfather:
    def gold(self):
        print("grandfather having 1kg gold")
        
class father(grandfather):
    def land(self):
        print("father having 5acres")

class kavs(father):
    def my(self):
        print("I own both")

all=kavs()
all.gold()
all.land()
all.my()
o/p:
grandfather having 1kg gold
father having 5acres
I own both

4.hierarchical inheritance
--> multiple child classes inherit from a single parent class
eg:
class father:
    def props(self):
        print("father having 10acres")
class son(father):
    def props1(self):
        print("I own part of his")
class daughter(father):
    def props2(self):
        print("she also owns part of his")
class mother(father):
    def props3(self):
        print("My mom also owns part of his")
print("son")
s=son()
s.props()
s.props1()
print("daughter")
d=daughter()
d.props()
d.props2()
print("mother")
m=mother()
m.props()
m.props3()
o/p:
son
father having 10acres
I own part of his
daughter
father having 10acres
she also owns part of his
mother
father having 10acres
My mom also owns part of his

5.hybrid inheritance
-->combination of two or more types of inheritance
eg:
class A:
    def some(self):
        print("Class A")
class B(A):
    def any(self):
        print("Class B")
class C(A):
    def so(self):
        print("Class C")
class D(B,C):
    def all(self):
        print("Class D")
how=D()
how.so()
o/p:
Class C

super() method
--------------
-->it is used to access methods and constructor of the parent class from the child class
class parent:
    def display(self):
        print("parent method")
class child(parent):
    def show(self):
        super().display()
        print("class method")
all=child()
all.show()
o/p:
parent method
class method

class person:
    def __init__(self,name):
        self.name=name
class stu(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def show(self):
        print(f"Name:{self.name}")
        print(f"rollno:{self.roll}")
any=stu('kavya',45)
any.show()

'''


    



































































































































































































