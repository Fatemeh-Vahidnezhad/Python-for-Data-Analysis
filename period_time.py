import pandas as pd
import numpy as np
p=pd.period_range('2020/01/01','2020/06/30',freq='M')
p
p=pd.period_range('2020/01/01','2020/06/30',freq='D')
p
p=pd.period_range('2020/01/01','2022/06/30',freq='Y')
p
p=pd.date_range('2020/01/01',periods=182,freq='D')
p

p=pd.period_range(2020,2025,freq='A-DEC')
df=pd.Series(np.arange(6),index=p)
df
df.asfreq('M',how='start')
df.asfreq('B',how='end')


p=pd.period_range('2020Q2','2021Q4',freq='M')
df=pd.Series(np.arange(len(p)),index=p)
df
df.asfreq('y',how='start')


data=pd.period_range('2020/01/01',periods=30,freq='B')
df=pd.Series(np.arange(len(data)),index=data)
df.to_period('M')


#pd.PeriodIndex
#making index with two columns:
year=[2001,2002,2003,2004]
quater=['Q1','Q2','Q3','Q4']
index=pd.PeriodIndex(year,quater,freq='Q-DEC')
index


tables=pd.read_html('https://github.com/wesm/pydata-book/blob/2nd-edition/examples/macrodata.csv')
data=tables[0]
data
index=pd.PeriodIndex(year=data.year,quarter=data.quarter,freq='Q-DEC')
index



#resampling:
data_index=pd.date_range('2020/01/01',freq='D',periods=100)
df=pd.Series(np.arange(len(data_index)),index=data_index)
df
df2=df.resample('M',kind='period').sum()
df2

df2=df.resample('M').sum()
df2



#cover the values between dates:
data_index=pd.date_range('2020/01/01',freq='W-WED',periods=5)
df=pd.Series(np.arange(len(data_index)),index=data_index)
df
df.resample('D').asfreq()
df.resample('B').asfreq()

df.resample('D').ffill()

df.resample('D').ffill(limit=3)




index=pd.DatetimeIndex(['2020/01','2021/02','2022/03'])
df=pd.DataFrame(np.arange(len(index)),index=index)
df



from pandas_datareader import data
goog=data.DataReader('GOOG',start='2004',end='2016',data_source='yahoo')
goog.head(5)
goog=goog['Close']
import matplotlib.pyplot as plt
goog.plot()
goog.plot(style='-')

resamp=goog.resample('BA').sum()
resamp
import seaborn 
seaborn.set()
fig,ax=plt.subplots(1,1)
goog=data.DataReader('GOOG',start='2004',end='2006',data_source='yahoo')
ax.plot(goog)
ax.legend(['resample','input'])
ax.resample(goog,'BA').mean().plot(style='--')












