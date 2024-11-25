from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd
dir1 = os.path.dirname(os.path.abspath(__file__))
preprocessor_file = os.path.join(dir1, 'artifacts', 'preprocessor.joblib')
model_file = os.path.join(dir1, 'artifacts', 'model.joblib')
preprocessor = joblib.load(preprocessor_file)
model = joblib.load(model_file)

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