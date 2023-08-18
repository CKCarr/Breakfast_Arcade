# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install -r requirements.txt

# Copy the rest of your project into the container
COPY . .

# Expose the port that your Flask app will listen on
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python3", "app.py"]
