#merging datasets with a key column:

#1.merging common data:merging two dataframe to one dataframe by the common -->
#element in the key column:
import pandas as pd
df1=pd.DataFrame({'data1':range(4),'key':['b','b','a','c']})
df1
df2=pd.DataFrame({'data2':range(2),'key':['a','b']})
df2
df3=pd.merge(df1,df2,on='key')
df3
df3=pd.merge(df1,df2)
df3

#2.merging all data:merging two dataframe to one dataframe by all -->
#elements in the key column:
pd.merge(df1,df2,how='outer')


#3.merging left data:merging two dataframe to one dataframe by the all -->
#elements in the key of left dataframe:
pd.merge(df1,df2,how='left')



#4.merging right data:merging two dataframe to one dataframe by the all -->
#elements in the key of right dataframe:
pd.merge(df1,df2,how='right')


  
#merging series among common column will be done only.
df1=pd.Series(range(7))
df1
df1.name='test'
df1
df2=pd.Series(range(3))
df2.name='test'
df3=pd.merge(df1,df2)
df3

#merging data with index as a key for merging:
df1=pd.DataFrame([[1,2],[3,4],[5,6]],index=['a','c','e'],
                 columns=['ohio','nevada'])
df2=pd.DataFrame([[7,8],[3,4],[5,6]],index=['a','c','d'],
                 columns=['misisipi','beyroot'])
pd.merge(df1,df2,right_index=True,left_index=True,how='outer')
df1
df2
df1.join(df2,how='outer')



df1=pd.DataFrame([[1,2,'a'],[3,4,'c'],[5,6,'e']],
                 columns=['ohio','nevada','key'])
df2=pd.DataFrame([[7,8,'a','f'],[3,4,'c','m'],[5,6,'d','n']],
                 columns=['misisipi','beyroot','key','key2'],index=[45,46,47])
df1
df2
#pd.merge(df1,df2,right_index=True,left_index=True,how='inner')
pd.merge(df1,df2,how='outer')
df3=pd.DataFrame([[1,2,'s'],[6,4,'m'],[8,9,'n']],
                 columns=['hend','tehran','key2'],index=[22,44,88])
df3
data=pd.merge(pd.merge(df1,df2,how='outer'),df3,how='outer')
data
df3.dtypes


#right_on and left_on in merge function:
df1=pd.DataFrame({'employee':['bob','esi','mike'],
                  'salary':[2000,3400,6700]})

df2=pd.DataFrame({'name':['mike','jane','bob'],
                  'dept':['qm','IT','noc']})
pd.merge(df1,df2,right_on='name',left_on='employee').drop('name',axis=1)



#left_on and right_index in merge function and vs:
df1=pd.DataFrame({'employee':['bob','esi','mike'],
                  'salary':[2000,3400,6700]})
index=['mike','jane','bob']
df2=pd.DataFrame({'dept':['qm','IT','noc'],
                  'data':[2008,2009,2012]},index=index)
df1
df2
pd.merge(df1,df2,right_index=True,left_on='employee')



#pd.concat(df1,df2)
#data=pd.concat(pd.concat(df1,df2),df3)

#concatenating dataset:
#adding a dataset to the second dataset to the end of rows of columns
df1=pd.DataFrame([[1,2,3],[2,4,5]],index=[1,2])
df2=pd.DataFrame([[4,5,6,6],[44,6,17,8]])
df1
df2
pd.concat([df1,df2])
pd.concat([df1,df2],axis=1,ignore_index=False)
pd.concat([df1,df2],axis=1,ignore_index=True)

pd.concat([df1,df2],axis=0,ignore_index=False)
pd.concat([df1,df2],axis=0,ignore_index=True)




pd.concat([df1,df2],axis=1,join='inner')

pd.concat([df1,df2],axis=1,keys=['first_series','second_series'])



#combining datasets:
#coverage NaN elements with special numbers:
import numpy as np
df1=pd.DataFrame({'a':[1,np.nan,5,3],
                  'b':range(4),
                  'c':[np.nan,3,5,np.nan]})
df1
df2=pd.DataFrame({'a':[0,0,0,0],
                  'b':[0,0,0,0],
                  'c':[0,0,0,0]})
df2
df1.combine_first(df2)




#melting datasets:
#pivoting 'wide' to 'long' format:
df=pd.DataFrame({'key':['foo','bar','baz'],
                 'A':[1,2,3],
                 'B':[4,5,6],
                 'C':[7,8,9]})
df
pd.melt(df,['key'])
#make a pivot on the dataset:
pd.melt(df,['key']).pivot('key','variable','value')



#fetching data:
import os
os.getcwd()
pop=pd.read_csv('state-population.csv')
pop.head(5)
area=pd.read_csv('state-areas.csv')
area.keys()
area.head(5)
abrev=pd.read_csv('state-abbrevs.csv')
abrev.head(5)

merged=pd.merge(pop,abrev,left_on='state/region',right_on='abbreviation').drop('abbreviation',1)

#find null cells:
merged.isnull().any()
merged['population'].isnull().sum()
merged.head(5)

final=pd.merge(merged,area,on='state')
final.head(5)
final.isnull().any()

#query from data:
final.query("year==2012 & ages=='total'").head(5)

#density:
final['density']=final['population']/final['area (sq. mi)']
final.sort_values(by='density',ascending=False)

density.tail()


#iterating:
for name,group in final.groupby('state'):
    print (name)
    print(group)


final.groupby('year').aggregate({'area (sq. mi)':'mean','population':'mean'}).sort_values(by='population')

col=['year','month','day','gender','births']
data=pd.read_csv('births.csv',sep='::',header=None,names=col)
data=data[1:]
data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
data.info()
data.births=data.births.astype(object).astype(int)
data.pivot_table('births',index='year',columns='gender',aggfunc='sum').plot()
plt.ylabel('test')

