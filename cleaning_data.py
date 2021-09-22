#rename:

#replace:

#removing duplicated data

#using map function:


#filtering missing data

#filling in missing data


#devide continuous data to categorical data:
ages=[22,27,19,27,34,54,18,65,27,38,43,52,73,69,65,55,44]
bin=[18,28,38,48,58,68,78]
import pandas as pd
x=pd.cut(ages,bin)
x
#frequency of every bin:
pd.value_counts(x)
group_name=['youth','youthadult','middleage','senior']
x1=pd.cut(ages,bin,labels=group_name)

import numpy as np
data=np.random.rand(20)
label=['x','y','z','b']
#the number of labels should equal with the number of bins
x=pd.cut(data,4,precision=2,labels=label)
pd.value_counts(x)

#qcut function:the frequency of every bin is equal with others.
x=pd.qcut(data,4,precision=2)
pd.value_counts(x)

#detecting & filtering outliers:
data=pd.DataFrame(np.random.randn(1000).reshape(-1,5))
data
data.describe()
#determine outlier in the special column:
col=data[0]
col[np.abs(data[0])>3]
#determine outlier in the all columns:
data[(np.abs(data)>3).any(1)]
np.sign(data)

data[(np.abs(data)>3)]=np.sign(data)*3


#change the order of rows in dataframe:
df=pd.DataFrame(np.arange(9).reshape(3,3))
df
sampler=np.random.permutation(3)
sampler
df.take(sampler)

#random sample from data:
#when replace is True: it means that we can choose data more than
#the number of rows. In the other word, they allow to repeat choices.
df.sample(n=4,replace=True)
df
#when replace is false, we only can choose less than row's number.
df.sample(n=3,replace=False)

#dummy variables:????
df=pd.DataFrame({'key':['a','b','c','d','e','f'],
                 'data1':range(6)})
df
pd.get_dummies(df['key'])
pd.get_dummies(df['data1'])



#
import pandas as pd
data={'david':'david@gmail.com','mahmood':'mahmood12@gmail.com',
      'Arash':'abasi@yahoo.com','wes':np.nan}
df=pd.DataFrame(data,index=[1,2,3])
df
df2=pd.Series(data)
df2
df2.isnull()
df2.str.contains('gmail')

