import pandas as pd
data={
    "Name":["Ali","None","Sara"],
    "Marks":[90,None,80]
}
df=pd.DataFrame(data)
print(df.isnull())
print(df.isnull().sum())
print(df.fillna(0))
df["Marks"]=df["Marks"].fillna(0)
print(df)
marks=df["Marks"].mean()
print(marks)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)
print(df.drop_duplicates())

import pandas as pd
data={
    "Name":["Ali","sara","Ali",None],
    "Age":["20","21","20","22"],
    "Marks":[90,None,90,85]
}
df=pd.DataFrame(data)
print("original data:")
print(df)
print(df.isnull().sum())
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
print(df.drop_duplicates())
df["Age"]=df["Age"].astype(int)
print(df)

import pandas as pd
data = {
    "Name":["Ali","Sara",None,"Ahmed"],
    "Marks":[90,None,80,70]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull().sum())
print(df["Name"].isnull().sum())
print(df["Marks"].fillna(0))
df["Marks"] = df["Marks"].fillna(0)
print(df)
mean_marks=df["Marks"].mean()
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
print(df)
df=df.dropna()
print(df)
print(df.duplicated())
print(df.drop_duplicates())
print(df.dtypes)
df["Age"]=df["Age"].astype(int)
peint(df.dtypes)