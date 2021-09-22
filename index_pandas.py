#hierarchical indexign in series:
import pandas as pd
import numpy as np
df=pd.Series(np.random.randn(6),index=[['a','b','c','d','e','f'],[1,1,2,2,3,3]])
df
df.index
df['b']
df['b',1]
#converting series to dataframe:
df.unstack()

#inverse operation of unstack:
df.unstack().stack()

#hierarchical indexign in dataframes:
frame=pd.DataFrame(np.arange(12).reshape(4,3),index=[['a','a','b','b'],[1,2,1,2]],
                   columns=[['x','x','z'],['red','green','pink']])

frame.index.names=['key1','key2']
frame.columns.names=['city','color']
frame
frame['x']

#reordering index or sorting values:
frame.swaplevel('key1','key2')

#reordering based on key1
frame.sort_index(level=1)
frame
frame.swaplevel(0,1).sort_index(level=0)

#summary statistics by level
frame.sum(level='key1')
frame.sum(level='city',axis=1)

#change columns to index in dataframes:
df=pd.DataFrame({'a':range(7),
                 'b':range(7,0,-1),
                 'c':['one','one','one','two','two','two','two'],
                 'd':[0,1,2,0,1,2,3]})
df
df2=df.set_index(['c','d'])
df2
df2.swaplevel('c','d')
df3=df.set_index(['c','d'],drop=False)
df3
#opposite set_index is reset_index:
df2.reset_index()


#multiply indexed series from tuples:
index=[('a',2009),('b',2010),('c',2009),('a',2010),('c',2011)]
index
pop=pd.Series([12,34,56,78,44],index=index)
pop
new_index=pd.MultiIndex.from_tuples(index)
new_index

pop=pd.Series([12,34,56,78,44],index=new_index)
pop
pop.unstack()
pop.unstack().T
pop.reset_index()


#multiply indexed series from array:
index_array=[['a','v','a','c','v'],[9,0,9,7,0]]
index=pd.MultiIndex.from_arrays(index_array)
pop=pd.Series([12,34,56,78,44],index=index)
pop

pop
new_index=pd.MultiIndex.from_arrays(index_array)
pop.reindex(index=new_index)




#multiply indexed series from product:
index_product=[['a','c','b'],[1,2]]
index=pd.MultiIndex.from_product(index_product)
pop=pd.Series([12,34,56,78,44,56],index=index)
pop.sort_index()



#level in index:
index=[[2003,2004],[1,2]]
index=pd.MultiIndex.from_product(index,names=['year','num'])
columns=[['bob','gue','sue'],['HR','Temp']]
columns=pd.MultiIndex.from_product(columns,names=['name','dept'])
health_data=pd.DataFrame(np.arange(24).reshape(4,6),columns=columns,index=index)
health_data

health_data.mean(level='year')

health_data.mean(level='dept',axis=1)




















