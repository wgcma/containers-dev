# Use a lightweight Python base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your script into the container
COPY host-info.py .

# Run the script when the container starts
CMD ["python", "host-info.py"]
