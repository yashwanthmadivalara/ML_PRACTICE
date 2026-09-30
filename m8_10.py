import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "hours": [2,3,4,5,6],
    "marks":[50,55,65,72,85],
    "age":[18, 18, 19, 20, 21]
})# type: ignore

correlation = df.corr()
sns.heatmap(correlation, annot = True)
plt.title("correlation heatmap")
plt.show()