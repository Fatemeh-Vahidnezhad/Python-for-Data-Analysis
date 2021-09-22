from datetime import datetime as dt
now=dt.now()
now
now.year,now.month, now.day

#subtract:
delta=dt(2020,2,7)-dt(1985,10,25,12,12,12)
delta.days
delta/365

from datetime import timedelta
dt(2009,1,2)-timedelta(2)
dt(2009,1,2)+2*timedelta(2)

from datetime import time
time(8,12,12)

#converting between string and datetime:
stamp=dt(2020,2,7,15,25,12)
stamp
str(stamp)


# %I:hour (12)
# %H:hour (24)
# %w: weekday as integer[0(sunday)6]
# %W: week number of a year[00,53]
# %F:shortcut for %Y-%m-%d
# %D:shortcut for %m/%d/%y
# %B:full month name
# %c: full date and time
# %b:abbreviated month name
# %a:abbreviated weekday name
# %A:full weekday name
# %p: locale equivalent of AM or PM
# %x:locale approperiate formatted date
#%X:locale approperiate time



#dt.strftime function:
stamp.strftime('%y-%m-%d')
stamp.strftime('%Y-%m-%d %H-%M-%S')
stamp.strftime('%Y-%m-%d %I-%M-%S  %w  %W %B %b %a %p %X %x')
stamp.strftime('%D')
stamp.strftime('%F')



#dt.strptime function:
value='2020-12-02'
dt.strptime(value,'%Y-%m-%d')

#a list of string datetime:
datestr=['2020/3/4','2019/09/7','2018/9/12']
[dt.strptime(x,'%Y/%m/%d') for x in datestr]

#or:
datestr=['2020/3/4','2019/09/7','2018/9/12']
for x in datestr:
    print(dt.strptime(x,'%Y/%m/%d'))


#parse:
from dateutil.parser import parse
parse('2020/02/07')
parse('2020-02-07')
parse('march 07,2020 12:45 AM')


#pandas and datetime:
from datetime import datetime
import numpy as np
import pandas as pd
dates=[datetime(2020,1,1),datetime(2020,2,1),
       datetime(2020,3,1),datetime(2020,4,1)]
ts=pd.Series(np.random.randn(4),index=dates)
ts
ts.index
ts+ts[::2]
ts[::2]

#date.range() function:
ts2=pd.Series(np.random.randn(400),
              index=pd.date_range('2020/01/01',periods=400))
ts2['2021']
ts2['2021/02']
ts2['2020/02':'2020/03']


ts3=pd.Series(np.random.randn(400),
              index=pd.date_range('2020/01/01',periods=400,freq='W-WED'))

ts3

ts4=pd.DataFrame(np.random.randn(400,4),
                 columns=['A','B','C','D'],
              index=pd.date_range('2020/01/01',periods=400,freq='W-WED'))
ts4

#using freq in date_range() function:
index=pd.date_range('2020/01/01','2020/01/20',freq='w-wed')
index
#D:day
#H:hour
index=pd.date_range('2020/01/01','2020/01/20',freq='W')
index
index=pd.date_range('2020/01/01','2020/01/20',freq='4h')
index
index=pd.date_range('2020/01/01','2020/01/20',freq='4h30min')
index
#WOM-3FRI:week of month,third friday in every month
index=pd.date_range('2020/01/01',periods=1000,freq='WOM-3FRI')
index

#M:last day of month
index=pd.date_range('2020/01/01',periods=1000,freq='M')
index

#B:business day
index=pd.date_range('2020/01/01','2020/01/20',freq='B')
index

#groupby:
import datetime
dates=[datetime(2020,1,1),datetime(2020,2,1),datetime(2020,2,1)
       ,datetime(2020,3,1),datetime(2020,4,1)]
ts=pd.Series(np.arange(5),index=dates)
ts.groupby(level=0).mean()



dates=pd.DatetimeIndex(['2020/09/01','2020/09/02',
                        '2020/09/03','2020/09/03','2020/09/05'])
ts=pd.Series(np.arange(5),index=dates)
ts.groupby(level=0).mean()

#unigque index:
ts.index._is_unique

t3=ts.resample('D')  #????
t3



#shifting(leading or lagging) data:
#common use of shifting for determine the percentage of changes in comparison to last month:
ts
#shift values:
ts1=ts.shift(1)
#change index time:
ts.shift(1,freq='D')
ts/ts.shift(1) -1
import matplotlib.pyplot as plt
fig,ax=plt.subplots(2,1)
dates=[datetime(2020,1,1),datetime(2020,2,1),datetime(2020,2,1)
       ,datetime(2020,3,1),datetime(2020,4,1)]
ts=pd.Series(np.arange(5),index=dates)
ts.plot(ax=ax[0])
ts.shift(2).plot(ax=ax[0])




#shifting date by offsets:

from pandas.tseries.offsets import Day,MonthEnd
now=datetime(2020,3,7)
now
now+3*Day()
now+MonthEnd()
now+MonthEnd(2)
MonthEnd().rollforward(now)
MonthEnd().rollback(now)

import pandas as pd
import numpy as np
data=pd.Series(np.arange(90),index=pd.date_range('2020/01/01',periods=90,freq='D'))
data
data.groupby(MonthEnd().rollforward).mean()
data.mean()
data['2020/02/29']
data['2020/03/30']
data['2020/01/31']




data=pd.read_csv('Fremont_Bridge_Bicycle_Counter.csv')
data.head(5)
data.keys()
data.columns=['Date','Total','East','West']
data['Total']=data.eval('West+East')
data['Total']
data['West']
data['East']
data.dropna().describe()
data.isna().sum()


#The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
x='print(55)'
eval(x)



%matplotlib inline
import seaborn 
seaborn.set()
data.plot()
data
data.info()
date=pd.period_range(data['Date'],freq='M')
data.set_index(date)
data.groupby(data.index.time).mean()
weekly= data.resample('M',kind='period').sum()
weekly.plot(style=['--','::','-'])







