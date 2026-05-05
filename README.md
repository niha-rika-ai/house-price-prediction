# 🏠 House Price Prediction using Linear Regression

## 📌 Overview
This project predicts house prices based on:
- Square Footage
- Number of Bedrooms
- Number of Bathrooms

It uses a Linear Regression model and provides an interactive web interface using Streamlit.

---

## 🚀 Features
- 📊 Large synthetic dataset (120+ entries)
- 🧠 Linear Regression model
- 📈 Model evaluation (R², MAE, MSE)
- 📉 Predicted vs Actual visualization
- 🌐 Interactive Streamlit web app
- 🎨 Styled UI for better user experience

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## 📊 Results
- Model Accuracy (R²): ~0.95
- Strong linear relationship between features and price

---

## ▶️ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Generate dataset
python src/generate_data.py

# Train model
python src/train_model.py

# Run app
python -m streamlit run app/app.py