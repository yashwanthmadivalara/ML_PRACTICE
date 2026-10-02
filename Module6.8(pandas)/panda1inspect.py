import pandas as pd
data = {
    "name" : ["rahul", "neha", "aman"],
    "age" : [20, 21, 22],
    "CGPA" : [8.5, 7.9, 9.0]
}
df = pd.DataFrame(data)
print(df.head()) #to display first few rows 

print(df.shape)
print(df.columns)

#selecting a column

print(df["CGPA"])
print(df[["name", "CGPA"]])
