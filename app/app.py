import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = joblib.load("model/house_model.pkl")
df = pd.read_csv("data/house_data.csv")


# Page config
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# Custom CSS (🔥 makes it look professional)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    h1 {
        color: white;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    .result-box {
        background-color: #1e5631;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🏠 House Price Prediction App")
st.write("Enter house details below")

# Inputs
sqft = st.slider("Square Footage", 500, 5000, 1500)
bedrooms = st.slider("Bedrooms", 1, 6, 3)
bathrooms = st.slider("Bathrooms", 1, 4, 2)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict([[sqft, bedrooms, bathrooms]])

    st.markdown(f"""
        <div class="result-box">
            💰 Estimated Price: ${int(prediction[0]):,}
        </div>
    """, unsafe_allow_html=True)
    st.write(f"Model Accuracy (R²): {model.score(df[['sqft','bedrooms','bathrooms']], df['price']):.2f}")

    st.subheader("📈 Model Insights")
    st.write("This model predicts house prices based on linear relationships between features.")
    

st.subheader("📊 Price vs Square Footage")


fig, ax = plt.subplots()
ax.scatter(df["sqft"], df["price"])
ax.set_xlabel("Square Feet")
ax.set_ylabel("Price")

st.pyplot(fig)

st.subheader("📉 Predicted vs Actual Prices")

preds = model.predict(df[["sqft", "bedrooms", "bathrooms"]])

fig2, ax2 = plt.subplots()
ax2.scatter(df["price"], preds)
ax2.set_xlabel("Actual Price")
ax2.set_ylabel("Predicted Price")
ax2.plot([df["price"].min(), df["price"].max()],
         [df["price"].min(), df["price"].max()],
         color='red')

st.pyplot(fig2)