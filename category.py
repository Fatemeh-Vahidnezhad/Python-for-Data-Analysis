#add a column with category name:
import pandas as pd
import numpy as np

df=pd.DataFrame({'a':[11,22,63,74,55],
                 'b':np.arange(5)})
df['category']=['a','b','b','b','a']
df

#make dummies instead of category in the data set:
dummies=pd.get_dummies(df.category,prefix='category')
new_df=df.drop('category',axis=1).join(dummies)
new_df

