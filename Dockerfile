# Use official slim Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install required system packages including git
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY . .

# Install uv and use it to install dependencies system-wide
RUN pip install uv && \
    uv pip install --system -r requirements.txt && \
    uv pip install --system git+https://github.com/ageitgey/face_recognition_models

# Expose FastAPI default port
EXPOSE 8000

# Start FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
