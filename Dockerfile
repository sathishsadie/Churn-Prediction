# FROM  python:3.10-slim
# WORKDIR /app
# COPY newapp.py /app/app.py
# COPY requirements.txt /app/requirements.txt
# COPY dev-requirements.txt /app/dev-requirements.txt
# COPY artifacts /app/artifacts
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt
# RUN pip install --no-cache-dir --default-timeout=100 -r dev-requirements.txt
# EXPOSE 8501
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY newapp.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY dev-requirements.txt /app/dev-requirements.txt
COPY artifacts /app/artifacts

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt
RUN pip install --no-cache-dir --default-timeout=100 -r dev-requirements.txt

# Expose the API port (default for FastAPI)
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


