import pandas as pd
import json
db=json.load(open('food.json'))

info=pd.DataFrame(db)
info[['id','description','group']]
info.keys()
info.info()

df=pd.DataFrame(db[0]['nutrients'])
df


db[1008]['nutrients']
db[1]['nutrients'][10]
db[1].keys()
db[0]['description']
db[0]



info.group.value_counts().head()
df

#remove duplicates:
df.duplicated().sum()
nutrients=df.drop_duplicates()
nutrients



#rename columns:
new_col={'description':'food',
         'group':'fgroup'}
info=info.rename(columns=new_col)
info.keys()
