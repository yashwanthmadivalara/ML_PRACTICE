# from sklearn.preprocessing import OneHotEncoder
import pandas as pd

data = pd.DataFrame({
    "dept": ["cse", "ece", "ise", "cse"]
})
encoded= pd.get_dummies(data,columns=["dept"])
print(data)
print(encoded) 