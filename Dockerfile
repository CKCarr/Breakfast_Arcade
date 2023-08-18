# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy only the required files into the container
COPY . /app
COPY app.py requirements.txt /app/
COPY api /app/api/
COPY static /app/static/
COPY templates /app/templates/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv  # Install python-dotenv package

# Expose the port that your Flask app will listen on
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python3", "app.py"]
