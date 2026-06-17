'''
Matplotlib:
===========
--> it is a library in python for data visualization,allowing users to create a a variety of plots..

Basic structure of matplotlib:
------------------------------
1.figure
2.axes
3.axis
4.grid
5.title
6.legend

import matplotlib.pyplot as plt
sales=['A','B','C']
values=[25,30,45]
plt.bar(sales,values,color='pink',edgecolor='blue')
plt.xlabel('Sales')
plt.ylabel('Values')
plt.title('BMW Sales Bar plot')
plt.show()

import matplotlib.pyplot as plt
sales=['A','B','C']
values=[25,30,45]
plt.plot(sales,values,color='black')
plt.xlabel('Sales')
plt.ylabel('Values')
plt.title('BMW Sales line plot')
plt.show()

import matplotlib.pyplot as plt
sales=['A','B','C','D','E','F']
values=[25,30,45,27,35,40]
plt.scatter(sales,values,color='black')
plt.xlabel('Sales')
plt.ylabel('Values')
plt.title('BMW Sales scatter plot')
plt.show()

import matplotlib.pyplot as plt
values=[11,24,45,32,30]
plt.hist(values,bins=10,color='red',edgecolor='black')
plt.xlabel('Sales')
plt.ylabel('Values')
plt.title('BMW Sales hist plot')
plt.show()



import matplotlib.pyplot as plt
sales=['grapes','guava','apple','banana','dragon fruit','strawberry']
values=[5,22,31,10,35,42]
plt.pie(values, labels=sales,colors= ['purple','green','red','yellow','pink','orange'],autopct='%1.1f%%',startangle=20)
plt.legend(sales)
plt.title('fruits plot')
plt.show()


import matplotlib.pyplot as plt
sales=['A','B','C']
values=[25,30,45]
plt.plot(sales,values,linestyle='-.',color='yellow',marker='h',markerfacecolor='blue')
plt.xlabel('Sales')
plt.ylabel('Values')
plt.title('BMW Sales line plot')
plt.show()

'''


























