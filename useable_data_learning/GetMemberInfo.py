import pandas as pd
filename='memberInfo.csv'
df=pd.read_csv(filename)
print(df)
newdf01=df.set_index(keys=['id'])
print(newdf01)
newdf02=df.set_index(keys=['id'],drop=False)
print(newdf02)