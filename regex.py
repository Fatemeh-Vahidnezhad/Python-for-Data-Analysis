#learning regex:

#.:everything
#\d:digit
#\w:word
#\s:white space
#\t:tab
#\n:header of every line
#*:from zero to infinite number
#+:from one to infinite number
#():make a group
#g<1>: first group, g<2>: the second group
#[a b c]: a or b or c
#[^ a b c]: everything except a , b, c
#^: the start of line: ex: ^1 ---> all lines which are started with 1
#ex: ^\d --> start with number
#ex: [^\d] ---> do not start with number
#{n,m}: at least n and maximum m, ex: a{4,8} ---> the number of a more than 4 and less than 8
#{n}:exactly n element: for example: a{4} --->  the number of a should be 4
#$:the final of a line: ex:.*$ --->everything with any number until the final of the line
#?: do not be greedy=lazy, find first charactor not last chractor
# .*\@:everything with any number until @
#example:mahmood@gmail.com
#answer: @(.*)\.    it means that: from @ everything until .


#search function:
import re
str="Salam Fatemeh, salam hassan, Salam hossein, salam everybody"
result=re.search(r'salam',str)
result.end()
result.span()
result.start()
#if the string is an email or not:
email='fatemeh.vahidnezhad@gmail.com'
email2='fatemeh.vahidnezhadgmail.com'

is_email=re.search(r'.+\@.+\..{3}',email)
print(is_email)

#the none output means that, it is not an email.
is_email=re.search(r'.+\@.+\..{3}',email2)
if is_email==None:
    print('it is not an email.')


#findall fucntion:
str=" The price of potato is 25$ for 1 kilo."
reg=re.findall(r'\d+',str)
price,kilo=reg[0],reg[1]
print('The price of potato for {} kilo is {} $.'.format(kilo,price))

#when we use () in the findall fuction, the result will be selected with digit.
str2='''The price of potato is 25$ for 1 kilo for yesterday.
 The price of potato is 23$ for 1 kilo for today.
 The price of potato is 27$ for 1 kilo for tomorrow.'''
result=re.findall(r'The price of potato is (\d+)\$ for (\d+) kilo for (.*)\.',str2)
result
list1=[]
for price,kilo,day in result:
    print(price,kilo,day)


#sub fuction: for replce sth with other thing
str='salam fatemeh, salam Maryam, Salam hossein.'
re.sub(r'[Ss]alam (\w+)\,','Hi \g<1>',str)  

str='''The price of potato is 25$ for 1 kilo for today.
The price of potato is 28$ for 5 kilo for tomorow.
The price of potato is 21$ for 1 kilo for last week. '''

result=re.sub(r'The price of potato is (\d+)\$ for (\d+) kilo for (.*)\.','\g<3>,\g<1>,\g<2>',str)  
print(result)


#using pandas & regex:

dict={'Arash':'arash@gmail.com','Hamed':'hamed@yahoo.com','Ali':'ali@gmail.com'}
import pandas as pd
df=pd.Series(dict)
df
result=df.str.findall(r'(.+)\@(.+)\.(.+\w{2,3})')
result

for item in result:
    print(item)










