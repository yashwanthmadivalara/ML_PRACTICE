from sklearn.preprocessing import MinMaxScaler

x = [[40],[60],[80],[100]]

scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)