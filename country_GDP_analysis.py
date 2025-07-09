import pandas as pd
df=pd.read_csv(r"C:\Users\Lenovo\Desktop\gc_tasks\MEDIUM\data.csv")
print(df)
print(id(df))
print(len(df))
print(df.columns)
print(len(df.columns))
print(df.isnull())
print(df.isna())#similar to the is null and it returns false because there are no missing values
print(df.isnull().sum())
print(df.head())
print(df.tail())
print(df.info())
