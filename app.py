import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load the Pickle Model
# -----------------------------
model = pickle.load(open("my_model.pkl", "rb"))

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="ML Model Prediction App", layout="wide")

st.title("💡 Machine Learning Prediction App")
st.write("This app uses your trained ML model stored in **my_model.pkl**.")

st.sidebar.header("Enter Input Features")
st.sidebar.write("Provide values below to get prediction")

# -----------------------------------
# ⚠️ IMPORTANT: Change inputs as per your model's features
# -----------------------------------
# Example: assuming your model needs 4 input features
# Replace these with correct feature names & count

f1 = st.sidebar.number_input("Feature 1", 0.0, 100.0, 10.0)
f2 = st.sidebar.number_input("Feature 2", 0.0, 100.0, 20.0)
f3 = st.sidebar.number_input("Feature 3", 0.0, 100.0, 30.0)
f4 = st.sidebar.number_input("Feature 4", 0.0, 100.0, 40.0)

# Collect inputs into array
input_data = np.array([[f1, f2, f3, f4]])

# -----------------------------------
# Prediction Button
# -----------------------------------
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"### 🔮 Prediction: **{prediction[0]}**")
