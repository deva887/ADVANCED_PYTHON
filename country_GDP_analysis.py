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
print(df.describe())#gives the numeric information only==descriptive statistics
print(df['CountryName'])#to get specific attribute data
df_cat=df[['CountryName','CountryCode','IncomeGroup']]
print(df_cat)
print(len(df.columns))
print(df_cat.describe())
print(len(df_cat.columns))
df_num=df[['BirthRate','InternetUsers']]
print(df_num)
print(df.info())
print(df_cat.info())
print(df_num.info())
print(df.describe())
print(df.describe().transpose())
print(df.describe().T)
#renaming
df.columns=['a','b','c','d','e']
print(df)
df.columns = ['countryName','CountryCode','BirthRate','InternetUsers','IncomeGroup']
print(df)
#subset
print(df[['CountryCode','BirthRate','InternetUsers']][4:8])
df['NewColumn']=df.BirthRate * df.InternetUsers
print(df)
print(len(df.columns))
df=df.drop('NewColumn',axis=1)
Filter_1 = df.InternetUsers<2
Filter_2 = df.BirthRate>40
print(df[Filter_1 & Filter_2])