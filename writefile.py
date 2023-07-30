import csv
import random
import pandas as pd
# 生成随机数
r = [random.randint(1, 7) for _ in range(10)]  # 生成10个范围在1到100之间的随机数
df=pd.DataFrame({"C":r})
df.to_csv(r"data_boc\SEND.csv")
