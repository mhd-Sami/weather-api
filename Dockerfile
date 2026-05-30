# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Set environment variables
# Prevents Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose ports
# Port 5000 for api.py, Port 5001 for server.py
EXPOSE 5000 5001

# Default command - runs api.py
# Can be overridden with 'docker run IMAGE python server.py'
CMD ["python", "api.py"]
