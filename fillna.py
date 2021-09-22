import numpy as np
import pandas as pd
state=['ohaio','washengton','dubi','tehran','beyroot','canada']
data=pd.Series(np.random.randn(6),index=state)
data[[2,4]]=np.nan
data
data.mean()
data.sum()
np.nansum(data)
data.dropna()
data.fillna(data.mean())
data.fillna(0)
#forward-fill
data.fillna(method='ffill')
#back-fill
data.fillna(method='bfill')



#dataframe:
df=pd.DataFrame({'A':np.arange(3),'B':np.random.randn(3)})
df.mean()
df['C']=np.nan
#forward-fill
df.fillna(method='ffill',axis=1)
#back-fill
df.fillna(method='bfill',axis=1)




#devide cities to two parts of east and west and groupby data by them:
parts=['east']*3+['west']*3
parts
data.groupby(parts).mean()


#filling the missing values with two special numbers:
values={'west':0,'east':1}
fill_data=lambda x: x.fillna(values[x.name])
data.groupby(parts).apply(fill_data)



#determine null data in a column:
tables=pd.read_html('https://github.com/wesm/pydata-book/blob/2nd-edition/datasets/titanic/train.csv')
data=tables[0]
data.isnull().sum()


#input values on null cells:
values=data['Age'].median()
values
data['Age'].fillna(values)
