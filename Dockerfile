# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables for the script
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for MongoDB tools and GCP
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    && wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | gpg --dearmor > /usr/share/keyrings/mongodb-archive-keyring.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/mongodb-archive-keyring.gpg] https://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list \
    && apt-get update \
    && apt-get install -y mongodb-org-tools \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and .env file into the container
COPY . /app/
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/gcp-key.json"

# Run the Python script (adjust if the file name is different)
CMD ["python", "backup.py"]
