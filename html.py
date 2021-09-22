import pandas as pd
tables=pd.read_html('https://github.com/wesm/pydata-book/blob/2nd-edition/examples/tips.csv')
len(tables)
ftable=tables[0]
ftable
#the frequency of data in a column:
df=pd.crosstab(ftable['day'],ftable['size'])
df
