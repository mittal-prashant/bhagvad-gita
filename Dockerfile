# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update --fix-missing && apt-get install -y python3-dev build-essential && apt-get install wget -y

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Download the model into the 'models' folder
RUN mkdir /app/models
RUN wget -O /app/models/llama-2-7b-chat.ggmlv3.q8_0.bin https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin

# Copy the rest of your application code into the container at /app
COPY . /app/

# Run your Python ingestion script
RUN python ingest.py

# Expose port 5000
EXPOSE 5000

# Define the command to run your application when the container starts
CMD ["python", "app.py"]
