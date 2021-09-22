import numpy as np
x=np.arange(-5,5,0.01)
np.meshgrid(x,x)
arr=np.array([[1,2,3],[4,5,6]])
np.ones(3)
#from random import normalvariate
N=100
x=np.random.seed(1234)
x
x=np.random.normal(size=(4))
x
np.random.uniform(0,2,size=10)
x=np.random.permutation(100)
x
import matplotlib.pyplot as plt
chi=np.random.normal(size=100)
#%timeit np.random.normal(chi)
plt.bar(chi,height=100000000,width=0.8,align='center')


#Series in pandas:
import pandas as pd
from pandas import Series ,DataFrame
obj=pd.Series([4,7,8,9])
obj
obj.values
obj.index

#dataframe:
data={'year':[2001,2002,2003,2005],'state':['ohio','nevada','berlin','ohio'],'pop':[1.3,1.6,2.6,2.1]}
frame=pd.DataFrame(data)
frame
frame['year']
frame.state
frame['test']=frame.state=='ohio'
frame
del frame['test']
frame
frame.index
frame.columns

#nested dict in dict
pop={'ohio':{2001:2.5,2000:1.24,2002:3.2},
     'nevada':{2000:1.5,2003:1.34,2002:3.4}}
frame3=pd.DataFrame(pop)
frame3
frame3['ohio'][:-1]
frame3['nevada'][1:3]
frame3['nevada'][:2]

#using pandas and numpy to define a dataframe:
frame1=pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['ohio','texas','california'])
frame1
frame2=frame1.reindex(['a','b','c','d'])
frame2

state=['ohio','utah','california']
frame4=frame1.reindex(columns=state)
frame4
frame5=frame1.reindex(index=state)
frame5
frame1.drop('a',inplace=True)
frame1
frame1.drop(['a','b'])
frame1.drop(['ohio'],axis=1)
frame3.rdiv(1)
df=pd.DataFrame(np.arange(9).reshape(3,3),index=[1,2,3],columns=['a','b','c'])
df
df.div(2)
df.rdiv(1)
df.rdiv(2)

#ranking
s=pd.Series([2,1,5,2])
s.rank()
s.rank(ascending=False, method='max')
frame.rank(axis='columns')
frame








