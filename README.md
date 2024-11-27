# **Customer Churn Prediction System**

This project predicts whether a customer will churn based on various features like customer details and usage behavior. The model is deployed as a REST API using **FastAPI**, and you can make predictions through a web interface or API endpoint.

## Steps to Get Started

### Step 1: Clone the Repository

Clone the repository using the following command:

```bash
git clone https://github.com/sathishsadie/Churn-Prediction.git
```

### Step 2: Change Directory

Navigate to the cloned repository directory:

```bash
cd customer-churn-prediction
```

### Step 3: Install Requirements

Install the necessary dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If you have development dependencies, you can install them with:

```bash
pip install -r dev-requirements.txt
```


### Step 4: Run the FastAPI App Locally

To run the FastAPI application locally, use the following steps:


```bash
uvicorn newapp:app --reload
```

Your API will be accessible at `http://127.0.0.1:8000`. You can test the prediction functionality using **Swagger UI** available at `http://127.0.0.1:8000/docs`.

### Step 5: Make Predictions Using the API

Once the server is running, you can make a POST request to the `/` endpoint to get churn predictions. Example request:

#### Request:
```json
{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "Yes",
    "StreamingTV": "No",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.5,
    "TotalCharges": 980.6
}
```

#### Response:
```json
{
    "prediction": "Not Churn"
}
```

## Deployed FastAPI Web App

The **Customer Churn Prediction System** has been deployed and is live on **Render**. You can access the deployed API [here](https://churn-prediction-b0og.onrender.com/).

## Continuous Integration & Deployment (CI/CD)

This project uses **GitHub Actions** for CI/CD. The following steps are part of the workflow:

1. **Test job**: Runs tests using `pytest` to ensure code quality.
2. **Deploy job**: Deploys the FastAPI app to **Render** after the tests pass.

### GitHub Actions Workflow

The CI/CD pipeline is defined in `.github/workflows/ci-cd.yml`. The workflow automates the process of testing and deploying the app to **Render**.

### GitHub Secrets

To securely interact with **Render**'s API, the **Render API Key** is stored as a GitHub secret. To add this secret:

1. Go to **Settings** > **Secrets** > **Actions** in your GitHub repository.
2. Add a new secret with the name `RENDER_API_KEY` and the value of your **Render API Key**.

