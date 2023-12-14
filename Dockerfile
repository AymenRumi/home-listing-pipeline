# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Update and install necessary packages
RUN apt-get update -y && \
    apt-get install -y \
    wget \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxrender1 \
    libxext6 \
    libatk1.0-0 \
    libasound2 \
    libgbm1

# Download and install Chromium
RUN apt-get install -y chromium

# Download and install ChromeDriver for Chromium
RUN wget -q https://chromedriver.storage.googleapis.com/$(wget -q https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O -)/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    rm chromedriver_linux64.zip

# Install any needed packages specified in requirements.txt
COPY .env /app/
RUN pip install remax_pipeline

# Copy the current directory contents into the container at /app
COPY script.py /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run Celery worker
CMD ["python","script.py"]