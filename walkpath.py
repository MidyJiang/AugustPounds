import os

for a,b,c in os.walk(os.path.abspath('')):
    print(c)
