# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY log_generator.py .

# Install any necessary dependencies (if any)
# In this case, we don't have additional dependencies

# Set the log file path as an environment variable
ENV LOG_FILE_PATH=/usr/share/logstash/temp/inlog.log

# Command to run the Python script
CMD ["python", "log_generator.py"]
