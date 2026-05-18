'''
Sets
=====
--> collection of unique and unordered elements
--> Duplicate values are not allowed and mutable
eg:
any={1,2,2,3,4}
print(any)
--> Items are not stored in index order
--> represented in {}

Methods
-------
1. union()
--> it will give all values from required sets together in once without repetition
syntax--> set.union(another_set)
eg:
any={6,4,2,8,3,2}
an={3,44,5}
print(any | an)
print(any.union(an))
-->for n sets also in the same way we use

2. intersection()
-->to get the common elements from both sets
syntax--> set.intersection(another_set)
eg:
a={3,5,3,2,2,4,3,2,3434,3432,1,3}
b={3,44,5}
c={3,1,2,6}
print(a & b &c)
print(a.intersection(b,c))

3. difference()
--> to get the different values from the set
syntax--> set.difference(another set)
eg:
a={1,4,2,6}
b={8,3,2}
print(a - b)
print(a.difference(b))

*symmetric difference(^)

Functions
---------
1. add()
--> to add new element into set
syntax--> variable_name.add(element)
eg:
any={77.5,3,3,4,8}
any.add(84)
# any.add(64) # be in first place
print(any)

2. update()
-->to add multiple elements into set
syntax--> variable_name.update([element])
eg:
any={1,2,4,2}
any.update([43,20])
print(any)

sum(set_name),min,max,len,remove,discard etc

3.remove()
--> remove is used to delete the element but if it is not existed element then it throws error(keyerror)
syntax--> set.remove(element)

4.discard()
--> discard also removes but for not existed element it doesn't throw error
syntax--> set.discard(element)
'''

