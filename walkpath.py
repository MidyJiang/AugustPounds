import os

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.abspath(os.path.join(root, file))
            print(file_path)

# 调用函数，传入要遍历的目录路径
list_files(os.path.abspath(""))


import pandas as pd
df=pd.read_csv(r"Formal Art/send.csv",encoding='utf16')
print(df)
