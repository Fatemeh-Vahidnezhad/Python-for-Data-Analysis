import pandas as pd
column_name=['name','gender','births']
data=pd.read_csv('baby_name2.txt',sep='::',names=column_name)
data
data.groupby('gender').births.sum()


#gathering data from some files which are divided based on year:
years=range(1881,1884)
peices=[]
for year in years:
    path='baby_%d.txt' % year
    df=pd.read_csv(path,sep='::',names=['name','gender','births'])
    df['year']=year
    peices.append(df)
data=pd.concat(peices,ignore_index=True)
data

#pivot table or groupby a dataframe:
total_birth=data.pivot_table(['births'],columns='gender',index='year',aggfunc='sum')
#or
data.groupby(['year','gender']).births.sum().unstack()

#plot:
total_birth.plot(title='total birth by gender and year')


#define a function for computing the percentage of every name:

def prop(x):
    x['prop']=x.births/x.births.sum()
    return x
data=data.groupby(['year','gender']).apply(prop)
data


#define a function to find 1000 top names for each year/gender combination:
def top(data):
    return data.sort_values(by='births',ascending=False)[:1000]
data.groupby(['year','gender']).apply(top)   
top_1000=data.groupby('name').apply(top)  #1000 top names for every gender 
top_1000

#analyzing name trend by a plot:
total_births=top_1000.pivot_table('births',index='year',
                                  columns='name',aggfunc='sum')
total_births.info()
subset=total_births[['Aaron','Abe','Zora']]
subset.plot(subplots=True,grid=False,figsize=(12,10),title='number of birth per year')
subset.plot()

#choose boys of 1882:
boys=data[data.gender=='M']
boys_1882=boys[boys.year==1882]
boys_1882


#finding diversity in names around years:
prop_cumsum=boys_1882.sort_values(by='prop',ascending=False).prop.cumsum()
prop_cumsum.values.searchsorted(0.5) #50 percent of names are devided between 15 names.


df_M=data[data.gender=='M']
df=df_M[df_M.year==1883]
df_cumsum=df.sort_values(by='prop',ascending=False).prop.cumsum()
diversity=df_cumsum.values.searchsorted(0.5)+1 # (+1): because index starts from zero


#defind a function to compute diversity for all years:
def cumsum(df):
    df_cumsum=df.sort_values(by='prop',ascending=False).prop.cumsum()
    return df_cumsum.values.searchsorted(0.5)+1
diversity=data.groupby(['year','gender']).apply(cumsum).unstack()

# result:diversity among girls are much more than boys.

diversity.plot(title='the number of popular names in top 50%',figsize=(12,10))




#extract last letter from names:
fun=lambda x: x[len(x)-1:]
x='Fatemeh'
fun(x)
len(x)
#last letter on data:
last_letter=data.name.map(fun)
data['letter']=data.name.map(fun)
data
table=data.pivot_table('births',columns=['gender','year'],aggfunc='sum',index=last_letter)
table
table.sum()
#the proportion of letters in each year and gender:
letter_prop=table/table.sum()
letter_prop


#create a subtable:
subtable=table.reindex(columns=[1882,1883],level='year')
subtable.head()


letter_prop['M']
#plot for each gender:
import matplotlib.pyplot as plt
fig, axis=plt.subplots(2,1,figsize=(12,10))
letter_prop['M'].plot.bar(ax=axis[0],title='Male')    
letter_prop['F'].plot.bar(ax=axis[1],title='Female')    


#plot for special columns:
ens_letter=letter_prop['M'].loc[['e','n','s']]
ens_letter.T.plot()








