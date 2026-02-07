from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# 1. Load your saved model/pipeline
# Replace 'your_model.joblib' with your actual filename
model = joblib.load("final_reserving_pipeline.pkl") 

# 2. Define the data structure (matching your insurance columns)
class ClaimData(BaseModel):
    Age_of_Driver: int
    Vehicle_Age: int
    Region: str
    Annual_Mileage: float
    Severity_Band: str
    days_to_fnol: int
    Fraud_Flag: bool
    Accident_Settlement_days: int
    Status: str
    Estimated_Claim_Amount: float
    Driving_Experience_Years: int
    ThirdParty_Role: str
    Vehicle_Type: str
    driver_risk_score: float
    Gender: str
    TP_Injury_Severity: str
    Claim_Type: str
    Litigation_Flag: bool
    vehicle_risk: bool
    Occupation: str
    Claim_Complexity: str
    # Add your other important features here!



# API Build 

@app.get("/")
def home():
    return {"message": "Insurance Claim Prediction API is Running"}

@app.post("/predict")
def predict(data: ClaimData):
    try:
        # 1. Convert Pydantic object to dict, then to DataFrame
        input_df = pd.DataFrame([data.model_dump()]) 
        
        # 2. Make sure the order of columns matches exactly what you trained on
        # If your model used 10 features, input_df must have those same 10 columns
        
        prediction = model.predict(input_df)
        
        # 3. If it's a log-prediction, reverse it
        final_val = float(np.expm1(prediction[0]))
        
        return {"predicted_claim_amount": round(final_val, 2)}
    
    except Exception as e:
        # This will print the error to your terminal so you can see it!
        print(f"ERROR DURING PREDICTION: {e}")
        return {"error": str(e)}



# py -m uvicorn app.main:app --reload