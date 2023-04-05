# Use the official Python runtime as a parent image
FROM python:3.11.0-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY webApp.py .
COPY index.html .
COPY exams.py .
COPY exam_info.pkl .

# Expose port 80 for the web application
EXPOSE 80

# Run the command to start the web application
CMD ["python", "webApp.py"]
