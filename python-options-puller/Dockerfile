# Use a lightweight Python image
FROM python:3.11-slim

# Install system dependencies for numpy/pandas
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and constants
COPY app.py .
COPY options_constants.py .

# Run the script when the container starts
CMD ["python", "app.py"]
