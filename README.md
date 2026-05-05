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
<img width="969" height="741" alt="Screenshot 2026-05-05 212541" src="https://github.com/user-attachments/assets/a2479ec2-a8f2-4732-aaeb-4dfeff29ba7b" />
<img width="933" height="843" alt="Screenshot 2026-05-05 212552" src="https://github.com/user-attachments/assets/f9514a01-cc75-40fd-a52d-e35322e2c3f1" />
<img width="914" height="723" alt="Screenshot 2026-05-05 212600" src="https://github.com/user-attachments/assets/f8ef446a-e4b9-4b7c-bcf6-aeaccc2c462d" />

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
