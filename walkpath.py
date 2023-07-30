import os

for a,b,c in os.walk(os.path.abspath('')):
    print(c)


import pandas as pd
df=pd.read_csv("send.csv")
print(df)
