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

## 📸 Screenshots
<img width="960" height="758" alt="UI" src="https://github.com/user-attachments/assets/c83a84cc-ccce-4b30-8554-960ea6bd46ee" />
<img width="951" height="847" alt="Graph" src="https://github.com/user-attachments/assets/351f47d9-ffef-46fc-973a-33f4e6ea15aa" />
<img width="899" height="710" alt="PredictionVSactual" src="https://github.com/user-attachments/assets/f5236aaf-f6c5-4ce8-9bad-053cdad636bd" />

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
