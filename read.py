import pandas as pd
from datetime import datetime, timedelta, timezone
df=pd.read_csv(r"send.csv")
print("df:",df)
print(datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S (UTC+8)"))
