import pandas as pd
import numpy as np
df= pd.DataFrame({'category':['a','a','a','a','b','b','b','b'],
                  'data':[20,17,12,19,16,18,6,7],
                  'weight':[9,4,5,7,6,2,4,8]})
df

#groupby by category:
df.groupby(df['category']).mean()

#weighted average in numpy:
#how to compute by calculators:
#first: each member of data*weight --> (1*4)+(2*5)+(3*6)+(4*7)=60
#second:sum up all weights with together --> 4+5+6+7=22
#third: devide first to second --> 60/22=2.7
data=[1,2,3,4]
np.average(data,weights=[4,5,6,7],axis=0)


#the weighted average in the dataframe in each category:
avg=lambda g: np.average(g['data'],weights=g['weight'])
df.groupby(df['category']).apply(avg)
#weighted average without category in the dataframe:
np.average(df['data'],weights=df['weight'],axis=0)


#corrwith in numpy:
df1=pd.DataFrame({'A':[1,2,3],'B':[1,2,3]})
df2=pd.DataFrame({'A':[3,2,3],'B':[4,2,3]})
df1
df2
df1.corrwith(df2,axis=0)

df1.corrwith(df2,axis=1)




