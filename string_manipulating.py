#string manipulation:
#split function:convert a string to list of strings
val='a,b ,c,d '
val.split(',')

#strip fucntion:trim whitespaces around strings
val.strip() #remove trim in the first and last charactor only:
#remove trim from every charactor in the list:(first way)
list1=[]
for i in val.split(','):
    item=i.strip()
    list1.append(item)
    print(list1)
    
#removing trim from every charactor in the list:(second way)
char=[x.strip() for x in val.split(',')]
char
    
#join function: convert list to string with special delimiter:
'|'.join(char)

#find function:
val.find('b')

#replace fuction:
val.replace(',',' ')

#upper and lower and title fuctions:
val.upper()
val.title()


#capitalize:first way
data=['hassan','zahra','hossein','fatemeh']
data2=[s.capitalize() for s in data]
data2

#capitalize:second way
data=['hassan vahidnezhad  ','fatemeh zahra hosseini',None,'hossein lotfi','fatemeh bagheri']
import pandas as pd
names=pd.Series(data)
names.str.capitalize()
names.str.lower()
names.str.len()
names.str.strip()
names.str.split()
names.str.get(0)
#extract last name from a list:
names.str.split().str.get(-1)
#extract first name from a list:
names.str.split().str.get(0)
#contain string:
names.str.contains('fatemeh').sum()

#dummies:
data3=pd.DataFrame({'name':data,
                    'info':['B|C|E','A|B','A|C|B','D|A|B','B|D']})
data3
data3['info'].str.get_dummies('|')










