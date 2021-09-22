#line plot:
#line plots for series:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s=pd.Series([1,2,3,4,3,1,3,4,5,2],index=range(10))
s
s.plot()
#the frequency of values by bar chart in series:
s.value_counts().plot.bar()



df=pd.DataFrame({'a':[1,2,3,4,3,1,3,4,5,2],'b':[1,2,3,4,3,1,3,4,5,2]},index=range(10))
df
df.plot()
#the frequency of values by bar chart in series:
df.plot.bar()

#line plot for dataframes:
df=pd.DataFrame([[1,2],[3,4],[6,7]],columns=['A','B'],
                index=np.arange(0,30,10))
df
df.plot()   #df.plot.line() is similar to df.plot()
plt.ylim(-1,8)


#bar plot with one column:
fig , axis=plt.subplots(2,1)
df=pd.DataFrame(np.random.rand(16),index=list('abcdefghijklmnop'))
df
df.plot.bar(ax=axis[0],color='g',alpha=0.5)
plt.ylim(-1,2)
df.plot.barh(ax=axis[1],color='k',alpha=0.5)


#bar plot with some some columns:
df1=pd.DataFrame(np.random.rand(5,3).cumsum(0),columns=['A','B','C']
,index=[1,2,3,4,5])
df1
df1.plot.bar()
df1.plot.barh()




#bar plot with some column by stacked:
df1=pd.DataFrame(np.random.rand(5,3).cumsum(0),columns=['A','B','C']
,index=[1,2,3,4,5])
df1
df1.plot.bar(stacked='True',alpha=0.5)
df1.plot.barh()

#fetching data from github website:
tables=pd.read_html('https://github.com/wesm/pydata-book/blob/2nd-edition/examples/tips.csv')
len(tables)
ftable=tables[0]
ftable
#The frequency of one column with respect to the other column:
df=pd.crosstab(ftable['day'],ftable['size'])
df
df1=df.loc[:,2:5]
df1
#normalize dataframe:
df1.sum(1)
dfp=df1.div(df1.sum(1),axis=0)
dfp.plot.bar()


#seaborn pakage:
ftable
import seaborn as sns
sns.barplot(x=ftable['tip'],y=ftable['day'],data=ftable,orient='h')

sns.barplot(x=ftable['tip'],y=ftable['day'],data=ftable,orient='h',hue='time')
sns.set(style='darkgrid')


#histogram and density plot in seaborn:
ftable['tip'].plot.hist(bins=50)
ftable['tip'].plot.density()

#both histogram and density in a plot:
s1=np.random.normal(0,1,200)
s1
s2=np.random.normal(10,2,200)
s2
s=pd.Series(np.concatenate([s1,s2]))
s
sns.distplot(s,bins=100,color='g')


#scatter or point plots and regression line in seaborn:
ftable
sns.regplot('total_bill','size',data=ftable)
plt.title('the relation between size and total_bill',fontsize='medium')


#pairs plot or scatter plot matrix:
ftable
data=ftable[['total_bill','size','tip']]
data
sns.pairplot(data,plot_kws={'alpha':0.2})


#grids and categorical data in seaborn:

ftable
import seaborn as sb
sb.factorplot(x='day',y='total_bill',hue='time',col='smoker',
               data=ftable,kind='bar')


sb.factorplot(x='day',y='total_bill',row='time',col='smoker',
               data=ftable,kind='bar')


#box plot in seaborn:
sb.factorplot(x='day',y='total_bill',row='time',col='smoker',
               data=ftable,kind='box')


sb.factorplot(x='day',y='total_bill',data=ftable,kind='box')




















