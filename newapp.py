from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd
import requests
import gdown
import os
import tempfile
# Function to download model from Google Drive
# def fetch_model_from_drive(file_url, save_path):
#     response = requests.get(file_url, stream=True)
#     with open(save_path, "wb") as file:
#         for chunk in response.iter_content(chunk_size=1024):
#             if chunk:
#                 file.write(chunk)
#     print(f"Model downloaded to {save_path}")
#     return save_path
preprocessor_url = "https://drive.google.com/file/d/1kCoMZSin1SX2njQqJKi71JNdHmcvoACp/view?usp=sharing"
model_url = "https://drive.google.com/file/d/1m-cUq-pqXy3-z4i9MwrrqrpG3KeAXO6t/view?usp=drive_link"  # Replace with your model file ID
with tempfile.TemporaryDirectory() as tmp_dir:
    print(f"Temporary directory created: {tmp_dir}")

    # File paths inside the temporary directory
    preprocessor_file = os.path.join(tmp_dir, "preprocessor.joblib")
    model_file = os.path.join(tmp_dir, "model.joblib")

    # Download the files
    gdown.download(preprocessor_url, preprocessor_file, quiet=False)
    gdown.download(model_url, model_file, quiet=False)
    print("Files downloaded successfully!")

    # Verify file existence
    if os.path.exists(preprocessor_file) and os.path.exists(model_file):
        print("Files exist in the temporary directory.")

        # Load the files
        try:
            preprocessor = joblib.load(preprocessor_file)
            print("Preprocessor loaded successfully!")
            model = joblib.load(model_file)
            print("Model loaded successfully!")
        except Exception as e:
            print(f"Error loading files: {e}")
    else:
        print("One or both files are missing.")
# Temporary paths for the models
# temp_dir = tempfile.gettempdir()
# preprocessor_path = os.path.join(temp_dir, "preprocessor.joblib")
# model_path = os.path.join(temp_dir, "model.joblib")
# # preprocessor_path = os.path.join(t, "preprocessor.joblib")  # Use /tmp for ephemeral storage in serverless
# # model_path = os.path.join("\tmp", "model.joblib")

# # Download and load models
# preprocessor_file = fetch_model_from_drive(preprocessor_url, preprocessor_path)
# model_file = fetch_model_from_drive(model_url, model_path)

# # Load models
# preprocessor = joblib.load(preprocessor_file)
# model = joblib.load(model_file)
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
# @app.post("/")
# async def create_item(data: Data):
#     try:
#         return {"message": "Data received successfully"}
#     except ValueError as e:
#         raise HTTPException(status_code=422, detail=str(e))
    

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