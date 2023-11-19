# Use the official Airflow image as a base
FROM puckel/docker-airflow:latest

# Copy the requirements.txt file into the container
COPY requirements.txt /requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Set the default command for the container
CMD ["airflow", "webserver"]
