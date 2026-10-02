from sklearn.preprocessing import StandardScaler
import pandas as pd
x = pd.DataFrame({
    "Age": [20, 21, 22, 23, 24],
    "Salary": [30000, 40000, 50000,60000, 70000]
})
scler = StandardScaler()
x_scaled = scler.fit_transform(x)
print(x_scaled)