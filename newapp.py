from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd
from huggingface_hub import hf_hub_download
import joblib

# Download files
preprocessor_path = hf_hub_download(repo_id="sadie26032005/churn_prediction", filename="preprocessor.joblib")
model_path = hf_hub_download(repo_id="sadie26032005/churn_prediction", filename="model.joblib")

# Load the models
preprocessor = joblib.load(preprocessor_path)
model = joblib.load(model_path)

print("Model and preprocessor loaded successfully!")

app = FastAPI()
class Data(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

def predict_churn(data:dict)-> int:
    input_df = pd.DataFrame([data])
    input_df.columns = [i.lower() for i in input_df.columns]
    preprocessed_data = preprocessor.transform(input_df)
    predictions = model.predict(preprocessed_data)
    return predictions[0]
    

@app.post("/")
async def predict(inputdata:Data):
    try: 
        print('11',inputdata)
        input_dict = inputdata.dict()
        print('22',input_dict)
        prediction = predict_churn(input_dict)
        print(prediction)
        if(prediction==1):
            return {"prediction":"Churn"}
        else:
            return {"prediction":"Not Churn"}
    except Exception as e:
        raise "Error Occured ."