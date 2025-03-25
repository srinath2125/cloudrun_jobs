# Use an official lightweight Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint for the Cloud Run Job
CMD ["python", "main.py"]
