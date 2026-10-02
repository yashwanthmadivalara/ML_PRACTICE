import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.DataFrame({
    "Hours":[1,2,3,4,5,6,7,8],
    "Marks":[35,42,50,55,65,70,78,85]
})

x = data[["Hours"]]
y = data["Marks"]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(x_train,y_train)

prediction = model.predict(x_test)

mae = mean_absolute_error(y_test,prediction)
mse = mean_squared_error(y_test,prediction)
r2 = r2_score(y_test, prediction)

print("coefficent:",model.coef_)
print("intersept:",model.intercept_)
print("MAE: ",mae)
print("MSE: ",mse)
print("R^2:",r2)