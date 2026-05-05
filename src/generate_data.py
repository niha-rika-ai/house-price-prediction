import pandas as pd
import numpy as np
import os

np.random.seed(42)

n = 120

sqft = np.random.randint(500, 4000, n)
bedrooms = np.random.randint(1, 6, n)
bathrooms = np.random.randint(1, 4, n)

price = (sqft * 50) + (bedrooms * 10000) + (bathrooms * 7000) + np.random.randint(-20000, 20000, n)

df = pd.DataFrame({
    "sqft": sqft,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "price": price
})

# ✅ Create data folder if not exists
os.makedirs("data", exist_ok=True)

df.to_csv("data/house_data.csv", index=False)

print("Dataset created successfully!")