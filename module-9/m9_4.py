from sklearn.preprocessing import LabelEncoder

data = ["cse", "ece", "ise", "cse"]

encoder = LabelEncoder()
encoded = encoder.fit_transform(data)
print(data)
print(encoded)