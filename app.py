import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Concrete Strength Prediction", layout="wide")

# Load model safely
@st.cache_resource
def load_model():
    try:
        return pickle.load(open("my_model.pkl", "rb"))
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        return None

model = load_model()

st.title("🏗️ Concrete Strength Prediction App")
st.write("Enter the concrete mixture values to predict compressive strength.")

# Input fields for concrete strength dataset
col1, col2, col3 = st.columns(3)

cement = col1.number_input("Cement (kg/m³)", 0.0, 1000.0, 300.0)
slag = col1.number_input("Blast Furnace Slag (kg/m³)", 0.0, 400.0, 50.0)
flyash = col1.number_input("Fly Ash (kg/m³)", 0.0, 300.0, 30.0)

water = col2.number_input("Water (kg/m³)", 0.0, 300.0, 150.0)
sp = col2.number_input("Superplasticizer (kg/m³)", 0.0, 40.0, 5.0)
coarse = col2.number_input("Coarse Aggregate (kg/m³)", 500.0, 1200.0, 900.0)

fine = col3.number_input("Fine Aggregate (kg/m³)", 400.0, 1000.0, 780.0)
age = col3.number_input("Age (days)", 1, 365, 28)

# Prepare input data
input_data = np.array([[cement, slag, flyash, water, sp, coarse, fine, age]])

# Predict button
if model is not None and st.button("Predict Strength"):
    prediction = model.predict(input_data)
    st.success(f"### 🔮 Predicted Compressive Strength: **{prediction[0]:.2f} MPa**")
