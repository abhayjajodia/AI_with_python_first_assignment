import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv("weight-height.csv")


print(data.head())
plt.scatter(data["Height"], data["Weight"], alpha=0.5)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Scatter plot: Height vs Weight")
plt.show()

X = data["Height"].values.reshape(-1, 1)  
y = data["Weight"].values                 

model = LinearRegression()
model.fit(X, y)


rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

print("RMSE:", rmse)
print("R²:", r2)

