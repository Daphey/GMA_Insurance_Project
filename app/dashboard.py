import streamlit as st
import requests


st.sidebar.image("https://www.freeiconspng.com/uploads/insurance-icon-png-24.png", width=100)
st.sidebar.title("Navigation")
st.sidebar.info("This model predicts claim payouts based on FNOL (First Notice of Loss) data.")


API_URL = "https://gma-insurance-project.onrender.com/predict"

st.set_page_config(page_title="FNOL Claim Predictor", layout="wide")

st.title("Insurance Claim Amount Predictor")
st.markdown("Enter the First Notice of Loss (FNOL) details to estimate the claim cost.")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    st.header("Driver & Vehicle Info")
    age = st.number_input("Age of Driver", min_value=17, max_value=100, value=30)
    v_age = st.number_input("Vehicle Age", min_value=0, max_value=50, value=5)
    experience = st.slider("Driving Experience (Years)", 0, 50, 10)
    mileage = st.number_input("Annual Mileage", value=10000.0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    occupation = st.text_input("Occupation", "Manager")
    region = st.selectbox("Region", ["Urban", "Rural", "Suburban"])

with col2:
    st.header("Incident Details")
    claim_type = st.selectbox("Claim Type", ["Material Damage", "Injury", "Theft"])
    severity = st.select_slider("Severity Band", options=["Low", "Medium", "High"])
    fnol_days = st.number_input("Days to FNOL", min_value=0, value=1)
    est_amount = st.number_input("Initial Estimated Amount", value=500.0)
    fraud = st.checkbox("Suspected Fraud Flag")
    litigation = st.checkbox("Litigation Flag")

# The Prediction Button
if st.button("Predict Claim Amount", type="primary"):
    # Map inputs to match your FastAPI Pydantic model exactly
    payload = {
        "Age_of_Driver": age,
        "Vehicle_Age": v_age,
        "Region": region,
        "Annual_Mileage": mileage,
        "Severity_Band": severity,
        "days_to_fnol": fnol_days,
        "Fraud_Flag": int(fraud),
        "Accident_Settlement_days": 30, # Defaulting hidden fields
        "Status": "Open",
        "Estimated_Claim_Amount": est_amount,
        "Driving_Experience_Years": experience,
        "ThirdParty_Role": "None",
        "Vehicle_Type": "Sedan",
        "driver_risk_score": 50.0,
        "Gender": gender,
        "TP_Injury_Severity": "None",
        "Claim_Type": claim_type,
        "Litigation_Flag": int(litigation),
        "vehicle_risk": 1,
        "Occupation": occupation,
        "Claim_Complexity": "Low"
    }

    try:
        # Send data to your FastAPI URL
        response = requests.post(API_URL, json=payload)
        

        if response.status_code == 200:
            prediction = response.json()
            st.success(f"### Predicted Claim Amount: ${prediction['predicted_claim_amount']:,.2f}")
        else:
            st.error(f"Error: {response.get('error')}")
    except Exception as e:
        st.error(f"Could not connect to API, Is your FastAPI terminal still running?: {e}")


# py -m streamlit run
# py -m streamlit run C:\Users\HP\Desktop\Dafe\DS_Projects\FNOL_Insurance\dashboard.py
# docker build -t gma-claims .
# docker run -p 8000:8000 gma-claims
# dir

