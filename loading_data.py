#current working direcotry:
import os
os.getcwd()

#automobile
import pandas as pd
names=['a','b','c','d','message']
read=pd.read_csv('test.csv',sep=',',names=names,index_col=['message'],header=None)
read

read1=pd.read_table('test1.txt',index_col=['key1','key2'])
read1
read1.T


import sys
read1.to_csv(sys.stdout,sep='|')


#read html
import pandas as pd
table=pd.read_html('FDIC_ Failed Bank List.html',encoding='utf-8')

len(table)
table=table[0]
table.head()

last_col=table['Closing Date']
time=pd.to_datetime(last_col)


count_month=time.dt.month.value_counts()
count_month.sort_values()


count_year=time.dt.year.value_counts()
count_year.sort_values()


#read excel files
f=pd.ExcelFile('test3.xlsx')
#test is the name of sheet in test3
frame=pd.read_excel(f,'test')
frame

#write pandas data in excel
#first creater a writer:
writer=pd.ExcelWriter('example_test.xlsx')
frame.to_excel(writer,'sheet1')
writer.save()

#read data from mysql
#first connect to mysql:

import mysql.connector 
db=mysql.connector.connect(host='localhost',user='root',
                         database='college',password='Fv@55966175')
cursor=db.cursor()
execute=cursor.execute("select * from class")
rows=cursor.fetchall()
print(rows)
db.commit()

#convert the list of tuple to dataframe:
col_name=['id_class','name_class']
classes=pd.DataFrame(rows,columns=col_name)
classes















