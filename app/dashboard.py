# import streamlit as st
# import requests


# st.sidebar.image("https://www.freeiconspng.com/uploads/insurance-icon-png-24.png", width=100)
# st.sidebar.title("Navigation")
# st.sidebar.info("This model predicts claim payouts based on FNOL (First Notice of Loss) data.")


# API_URL = "https://gma-insurance-project.onrender.com/predict"

# st.set_page_config(page_title="FNOL Claim Predictor", layout="wide")

# st.title("Insurance Claim Amount Predictor")
# st.markdown("Enter the First Notice of Loss (FNOL) details to estimate the claim cost.")

# Create two columns for a cleaner layout
# col1, col2 = st.columns(2)

# with col1:
#     st.header("Driver & Vehicle Info")
#     age = st.number_input("Age of Driver", min_value=17, max_value=100, value=30)
#     v_age = st.number_input("Vehicle Age", min_value=0, max_value=50, value=5)
#     experience = st.slider("Driving Experience (Years)", 0, 50, 10)
#     mileage = st.number_input("Annual Mileage", value=10000.0)
#     gender = st.selectbox("Gender", ["Male", "Female", "Other"])
#     occupation = st.text_input("Occupation", "Manager")
#     region = st.selectbox("Region", ["Urban", "Rural", "Suburban"])

# with col2:
#     st.header("Incident Details")
#     claim_type = st.selectbox("Claim Type", ["Material Damage", "Injury", "Theft"])
#     severity = st.select_slider("Severity Band", options=["Low", "Medium", "High"])
#     fnol_days = st.number_input("Days to FNOL", min_value=0, value=1)
#     est_amount = st.number_input("Initial Estimated Amount", value=500.0)
#     fraud = st.checkbox("Suspected Fraud Flag")
#     litigation = st.checkbox("Litigation Flag")

# The Prediction Button
#if st.button("Predict Claim Amount", type="primary"):
    # Map inputs to match your FastAPI Pydantic model exactly
    # payload = {
    #     "Age_of_Driver": age,
    #     "Vehicle_Age": v_age,
    #     "Region": region,
    #     "Annual_Mileage": mileage,
    #     "Severity_Band": severity,
    #     "days_to_fnol": fnol_days,
    #     "Fraud_Flag": int(fraud),
    #     "Accident_Settlement_days": 30, # Defaulting hidden fields
    #     "Status": "Open",
    #     "Estimated_Claim_Amount": est_amount,
    #     "Driving_Experience_Years": experience,
    #     "ThirdParty_Role": "None",
    #     "Vehicle_Type": "Sedan",
    #     "driver_risk_score": 50.0,
    #     "Gender": gender,
    #     "TP_Injury_Severity": "None",
    #     "Claim_Type": claim_type,
    #     "Litigation_Flag": int(litigation),
    #     "vehicle_risk": 1,
    #     "Occupation": occupation,
    #     "Claim_Complexity": "Low"
    # }

    # try:
        # Send data to your FastAPI URL
    #     response = requests.post(API_URL, json=payload)
        

    #     if response.status_code == 200:
    #         prediction = response.json()
    #         st.success(f"### Predicted Claim Amount: ${prediction['predicted_claim_amount']:,.2f}")
    #     else:
    #         st.error(f"Error: {response.get('error')}")
    # except Exception as e:
    #     st.error(f"Could not connect to API, Is your FastAPI terminal still running?: {e}")


# py -m streamlit run
# py -m streamlit run C:\Users\HP\Desktop\Dafe\DS_Projects\FNOL_Insurance\app\dashboard.py
# docker build -t gma-claims .
# docker run -p 8000:8000 gma-claims
# dir



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
        "Fraud_Flag": bool(fraud),  # Changed from int() to bool()
        "Accident_Settlement_days": 30,  # Defaulting hidden fields
        "Status": "Open",
        "Estimated_Claim_Amount": est_amount,
        "Driving_Experience_Years": experience,
        "ThirdParty_Role": "None",
        "Vehicle_Type": "Sedan",
        "driver_risk_score": 50.0,
        "Gender": gender,
        "TP_Injury_Severity": "None",
        "Claim_Type": claim_type,
        "Litigation_Flag": bool(litigation),  # Changed from int() to bool()
        "vehicle_risk": True,  # Changed from 1 to True
        "Occupation": occupation,
        "Claim_Complexity": "Low"
    }

    try:
        # Send data to your FastAPI URL
        response = requests.post(API_URL, json=payload)
        
        # Debug: Show response info
        st.write(f"Status Code: {response.status_code}")
        st.write(f"Response Text: {response.text[:200]}...")

        if response.status_code == 200:
            # Parse the JSON response
            prediction = response.json()
            
            # Check if prediction contains expected key
            if 'predicted_claim_amount' in prediction:
                st.success(f"### Predicted Claim Amount: ${prediction['predicted_claim_amount']:,.2f}")
            elif 'error' in prediction:
                st.error(f"API Error: {prediction['error']}")
            else:
                st.warning(f"Unexpected response format: {prediction}")
        else:
            # Try to get error message from response
            try:
                error_data = response.json()
                st.error(f"API Error {response.status_code}: {error_data.get('detail', error_data.get('error', 'Unknown error'))}")
            except:
                st.error(f"API Error {response.status_code}: {response.text}")
                
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to API. Please check if your FastAPI service is running.")
    except Exception as e:
        st.error(f"Connection error: {str(e)}")

# Add a debug section
with st.expander("Debug Information"):
    st.write("API URL:", API_URL)
    st.write("Payload structure:", {
        "Age_of_Driver": "int",
        "Vehicle_Age": "int",
        "Region": "str",
        "Annual_Mileage": "float",
        "Severity_Band": "str",
        "days_to_fnol": "int",
        "Fraud_Flag": "bool",
        "Accident_Settlement_days": "int",
        "Status": "str",
        "Estimated_Claim_Amount": "float",
        "Driving_Experience_Years": "int",
        "ThirdParty_Role": "str",
        "Vehicle_Type": "str",
        "driver_risk_score": "float",
        "Gender": "str",
        "TP_Injury_Severity": "str",
        "Claim_Type": "str",
        "Litigation_Flag": "bool",
        "vehicle_risk": "bool",
        "Occupation": "str",
        "Claim_Complexity": "str"
    })