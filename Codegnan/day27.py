'''
Data Analysis
=============
--> This is process of inspecting,cleaning,transforming,and modeling data to discover useful insights
Types of DA
-----------

1.Descriptive Analysis
--> Summarizing data

2. Diagnostic Analysis
--> Understanding causes

3.Predictive Analysis
--> Forecasting Future outcomes

4.Prescriptive Analysis
-->Suggesting act-ins based on data

Why DA
------
-->To improve Decision making
-->Detects trends and patterns

=====Numpy(numerical python)=======

--> this python library for numerical computing.it provides support for multi-dimensional arrays and linear algebra operations,making it essential for data analysis

using numpy in DA
-----------------
--> improved performance
-->simplifies complex operations
--> easy data manipulation

import numpy as np
arr_1=np.array([[3,4,5,6],[8,5,3,2]])
print(arr_1)
print(arr_1.shape)
res=arr_1.reshape(4,2)
print(res)

import numpy as np
arr_1=np.array([23,26,87,54,34,97,55])
print(arr_1)
print(arr_1+3)
print(arr_1-5)
print(arr_1*3)
print(arr_1//3)
print(arr_1/2)
print(arr_1%9)

import numpy as np
arr_1=np.array([[1,3],[4,5]])
arr_2=np.array([[5,7],[8,9]])
print(np.dot(arr_1,arr_2))

import numpy as np
arr_1=np.array([1,3,4,5])
nrm=arr_1.view()
arr_1[0]=100
print(nrm)
print(arr_1)
deep=arr_1.copy()
arr_1[0]=200
print(deep)
print(arr_1)


=====Pandas====

--> it is a powerfull data manipulation and analysis library where it provides data structure like series and dataframe for efficient data handling.

import pandas as pd
any=pd.Series([3224,42343,12322,333232,342],index=['Earbuds','smartphone','laptop','watch','keychain'])
print(any)

Series methods
-------------
mean()
sum()
max()
min()
apply()
map()

'''
import pandas as pd
data={
    'product':['earbuds','smartphones','laptop','watch','footware'],
    'brand':['noise','oneplus','dell','titan','adidas'],
    'price':[2354,25343,56575,2342,4443],
    'stock':[23,43,232,234,655]
    }
dip=pd.DataFrame(data)
print(dip)







































