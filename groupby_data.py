#groupby a column:
import pandas as pd
tables=pd.read_html('https://github.com/wesm/pydata-book/blob/2nd-edition/examples/tips.csv')
ftable=tables[0]
ftable
group_day=ftable['tip'].groupby(ftable['day']).mean()
group_day



#groupby more than one column:
group_day_time1=ftable['total_bill'].groupby([ftable['day'],ftable['time']]).mean()
group_day_time1.unstack()


group_day_time2=ftable['total_bill'].groupby([ftable['day'],ftable['time']]).size()
group_day_time2.unstack()
group_day_time2

#showing size and mean in one dataframe by concatenation:
df=pd.concat([group_day_time1,group_day_time2],axis=1)
df

#iterating over groups:
for name , group in ftable.groupby(ftable['time']):
    print(name)
    print(group)


for name , group in ftable['tatal_bill'].groupby(ftable['time']):
    print(name)
    print(group)



for (k1,k2) , group in ftable['total_bill'].groupby([ftable['time'],ftable['smoker']]):
    print((k1,k2))
    print(group.mean())



# pieces of data:
pieces=dict(list(ftable.groupby(['time'])))
pieces['Dinner']

ftable.dtypes

grouped=ftable.groupby(ftable.dtypes,axis=1)
grouped

for dtyped ,group in grouped:
    print(dtyped)
    print(group)




#select a column or subset of columns:
    
#the follow way for writing the code has a column name in the output:
df2=ftable.groupby('time')[['total_bill']].mean()
df2
#it is better:
df3=ftable[['total_bill']].groupby(ftable['time']).mean()
df3

#the follow way does not have column name:
df3=ftable['total_bill'].groupby(ftable['time']).mean()
df3
df2=ftable.groupby('time')['total_bill'].size()
df2




#grouping with series and dicts:

#to add special columns with together by defining a dict:
import numpy as np
people=pd.DataFrame(np.random.randn(4,4),index=['john','stive','mike','artoor'],
                    columns=['a','b','c','d'])
people
mapping={'a':'red','b':'green','c':'red','d':'pink'}
people_g=people.groupby(mapping, axis=1)
people_g.sum()#first and third columns will add together 


#converting a dict to a series:
S=pd.Series(mapping)
S
#count of every row:
people_g2=people.groupby(S,axis=1)
people_g2.count()


#len function: compute the length of a string
people.groupby(len).sum()
people
#????
key_list=['one','one','one','two']
people.groupby([len,key_list]).sum()

















