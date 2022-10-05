import pandas as pd

print("hello world!")
print(pd.__version__)

df = pd.read_excel('./サンプルデータ.xlsx', skiprows=1)
print(df)
print('***********************')

for row in df.itertuples():
    print(row[1], row[2])
# print(df.loc[1])
