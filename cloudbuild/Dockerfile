# Use an official lightweight Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies (update as per your project requirements)
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port (update based on your app's requirement)
EXPOSE 8080

# Command to run the application (modify for your framework)
CMD ["python", "app.py"]
