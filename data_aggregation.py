#learn groupby before reading this file:
#quantile function:
import pandas as pd
df=pd.DataFrame([[1,2,3],[1,3,5]],columns=['A','B','c'])
df
df.quantile(0,axis=1)
df.quantile(0.25,axis=1)
df.quantile(0.5,axis=1)
df.quantile(0.75,axis=1)
df.quantile(1,axis=1)
#fetching data from github website:
tables=pd.read_html('https://github.com/wesm/pydata-book/blob/2nd-edition/examples/tips.csv')
ftable=tables[0]
ftable
#grouping the table:
ftable['total_bill'].groupby(ftable['size']).mean()
grouped=ftable['total_bill'].groupby([ftable['time'],ftable['smoker'],ftable['day']])

#describle() fuction for grouped data in the table:
grouped.describe()


#aggregation fuction or agg() is similar to discribe():
grouped.agg(['mean','std'])

#define a fuction and using agg():
def fuct(arr):
    return arr.max()-arr.min()
grouped.agg(fuct)

#ensure that the above code is right:
grouped.agg([fuct,'max','min'])

#agg for two columns:
grouped.agg([('size','mean'),('tip','min')])

#sorting values in grouped dataframe:
def funct(ftable,n=5,column='tip'):
    return ftable.sort_values(by=column)[-n:]
funct(ftable)

grouped=ftable.groupby([ftable['smoker'],ftable['day']]).apply(funct,n=10,column='total_bill')
grouped





#quantile and bucket analysis:
import numpy as np
df=pd.DataFrame({'data1':np.random.randn(10),'data2':np.random.randn(10)})

#cut() function for making bins:
quartile=pd.cut(df.data1,4)
quartile

#groupby data by defined quartile:
grouped=df[['data2']].groupby(quartile).mean()
grouped


#apply() function:
def fuct(df):
    return {'min':df.min(),'max':df.max(),'mean':df.mean()}
fuct(df)

grouped=df[['data2']].groupby(quartile).apply(fuct)


#qcut() function for making bins:
#qcut() returns equal values in each bin
quartile=pd.qcut(df.data1,10)
grouped=df[['data2']].groupby(quartile).apply(fuct)
grouped
