import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the dataset
data = pd.read_csv("50_Startups.csv")

# 2. Quick look at columns
print("Columns:", data.columns.tolist())

# 3. Pick features and target
X = data[['R&D Spend', 'Marketing Spend']]  # most important features
y = data['Profit']

# 4. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# 5. Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Make predictions
y_pred = model.predict(X_test)

# 7. Evaluate the model
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"R² score: {r2:.4f}")

# 8. Plot results
plt.figure(figsize=(6,5))
plt.scatter(X_test['R&D Spend'], y_test, color='blue', label='Actual')
plt.scatter(X_test['R&D Spend'], y_pred, color='red', label='Predicted')
plt.xlabel("R&D Spend")
plt.ylabel("Profit")
plt.title("Actual vs Predicted Profit")
plt.legend()
plt.show()