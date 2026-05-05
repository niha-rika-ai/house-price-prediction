import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/house_data.csv")

# 1. Sqft vs Price
plt.figure()
plt.scatter(df["sqft"], df["price"])
plt.xlabel("Square Feet")
plt.ylabel("Price")
plt.title("Price vs Square Footage")
plt.savefig("sqft_vs_price.png")

# 2. Bedrooms vs Price
plt.figure()
plt.scatter(df["bedrooms"], df["price"])
plt.title("Bedrooms vs Price")
plt.savefig("bedrooms_vs_price.png")

# 3. Bathrooms vs Price
plt.figure()
plt.scatter(df["bathrooms"], df["price"])
plt.title("Bathrooms vs Price")
plt.savefig("bathrooms_vs_price.png")

print("Graphs saved successfully!")
