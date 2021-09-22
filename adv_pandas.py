import pandas as pd
df=pd.Series(['apple','orange','apple']*2)
df
pd.unique(df)
#count of values:
pd.value_counts(df)


#take method:
dim=pd.Series(['apple','orange'])
values=pd.Series([0,1,0,0,0,0,1,1,0])
dim.take(values)

#computation with categoricals:
import numpy as np
draws=np.random.randn(1000)
draws[:5]
bins=pd.qcut(draws,4,labels=['Q1','Q2','Q3','Q4'])
bins
bins.codes
pd.Series(draws).groupby(bins).agg(['min','max','mean'])
s=pd.Series(draws)
cat_s=s.astype('category')
cat_s
cat_s.value_counts()




df=pd.DataFrame({'key':['a','b','c']*4,'value':np.arange(12)})
df.groupby('key').mean()
transform=lambda x: x.mean()
df.groupby('key').apply(transform)

df.groupby('key').transform(lambda x: x.mean())
df
df.groupby('key').transform('mean')

df.groupby('key').transform(lambda x: x*2)

df.groupby('key').transform(lambda x: x.rank(ascending=False))



#normalize data:
def normalize(x):
    return (x-x.mean())/x.std()
df.groupby('key').transform(normalize)
df.groupby('key').apply(normalize)
df
data=df.groupby('key').apply(normalize)


#grouped time resampling:
time=pd.date_range('2020-01-01',periods=15,freq='T')
time
df=pd.DataFrame({'time':time,'values':np.arange(len(time))})
df
#groupby time index:
df.set_index('time').resample('5min').mean()



df=pd.DataFrame({'time':time,
                'values':np.arange(len(time)),
                'key':(['a','b','c','d','e']*3)})
df
df.set_index('time').groupby(['key',time]).mean()
df.set_index('time').groupby('key').resample('10min').mean()
pd.TimeGrouper('5min')













