#fetching data:
import os
os.getcwd()
import pandas as pd
import numpy as np
mnames=['movie_id','title','genre']
movies=pd.read_table('moives1.csv',header=None,sep='::',names=mnames)
movies['title']
movies['movie_id'].astype(str)
movies['genre']
movies['movie_id']
movies.dtypes

rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_csv('ratings.csv',sep='::',names=rnames,header=None)
ratings['movie_id']
ratings.describe()
ratings.dtypes

unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('users.csv',sep='::',names=unames,header=None)
users



#merging 3 dataset:
rat_user=pd.merge(ratings,users,how='outer')
data=pd.merge(rat_user,movies,how='outer')
#pivot data
piv_data=data.pivot_table(['rating'],index=['title'],columns='gender',aggfunc='mean')


#the number of titles:
title_numb=data.groupby(data['title']).size()
#choose up to 300:
up_300=title_numb.index[title_numb>=300]
up_300
#pivot up to 300:
piv_data_300=piv_data.loc[up_300]
piv_data_300
#sort data:????
piv_data_300.sort_values("M")

#add a column to the pivot table:???
piv_data_300['diff']=piv_data_300['F']-piv_data_300['M']

#remove values in a age column which age==1:
data.groupby(['age']).size()
data=data[data.age!=1]
data.groupby(['age']).size()






