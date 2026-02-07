# 1. Use an official Python image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your code and the model file
COPY ./app ./app
COPY .models/final_reserving_pipeline.pkl .

# 5. Expose the port FastAPI runs on
EXPOSE 8000

# 6. Command to run the API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]