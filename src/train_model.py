import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset
df = pd.read_csv("data/house_data.csv")

# Features & target
X = df[["sqft", "bedrooms", "bathrooms"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

preds = model.predict(X)
mae = mean_absolute_error(y, preds)
mse = mean_squared_error(y, preds)

# Accuracy
print("Model trained successfully!")
print("Model Score (R²):", model.score(X, y))
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/house_model.pkl")
