import pandas as pd
students={
    "Name":["Fatima","Ali","Rabi"],
    "Marks":[70,65,90],
    "Age":[19,18,21]
}
df=pd.DataFrame(students)
print(df)
print(df['Name'])
print(df[["Age","Marks"]])
print(df.head(2))
print(df.tail(1))
print(df.info())
print(df.describe())
print(df.iloc[2])
print(df.loc[1])
print(df.iloc[:3])
print(df.iloc[:,2])

import pandas as pd
sales={
    "Months":["january","february","March","April","May"],
    "Sales":[1000,2000,3000,4000,6000]
}
df=pd.DataFrame(sales)
print(df)
print(df.head(3))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.loc[2])
print(df.iloc[4])
print(df.iloc[1:3,0:2])
