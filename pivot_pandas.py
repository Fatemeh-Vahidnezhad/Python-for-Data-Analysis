import pandas as pd

#fetching data from github:
tips=pd.read_html('https://github.com/wesm/pydata-book/blob/2nd-edition/examples/tips.csv')
tip=tips[0]
tip.pivot_table(['total_bill','tip'],index=['smoker'])


#define df dataframe:
df=pd.DataFrame({'smoker':['yes','no','yes'],
              'tip':[1,2,3],
              'total_bill':[4,5,12]})
df


#pivot table can compute the average of columns(mean) by default:
df.pivot_table(['total_bill','tip'],index=['smoker'],margins=True)



#pivot table can compute the every fuction of columns with aggfunc:
tip.pivot_table(['total_bill'],index=['smoker','time']
,columns='day',margins=True,aggfunc='mean')


tip.pivot_table(['total_bill'],index=['smoker','time']
,columns='day',margins=True,aggfunc='min')


#define a dataframe:

df=pd.DataFrame({'nationality':['USA','Iran','Germany','England','USA','Iran','Germany','Germany'],
                 'handedness':['right','left','right','right','left','left','right','left'],
                 'feq':[43,23,56,89,54,12,23,45]})
df
df.pivot_table('feq',index=['nationality'],aggfunc='sum',columns='handedness',margins=True)
df.pivot_table('feq',index=['nationality'],aggfunc='sum',columns='handedness')


#crosstab in pivot tables:
pd.crosstab(df.nationality,df.handedness,margins=True)




