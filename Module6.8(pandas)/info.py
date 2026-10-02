import pandas as pd
data = {
    "name" : ["rahul", "neha", "kali"],
    "age" : [20, 21, 22],
    "CGPA" : [8.5, 7.9, 8.3]
}
df = pd.DataFrame(data)
#print(df.info())
#print(df.describe())
# print(df.isnull().sum())
# df = df.dropna()
#df = df.drop_duplicates()
# df["CGPA"] = df["CGPA"].fillna(df["CGPA"].median())
# print(df)
A = df.sort_values("CGPA", ascending = True)
print(A)