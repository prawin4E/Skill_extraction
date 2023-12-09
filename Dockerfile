# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the entire project directory to the working directory
COPY . .

RUN apt -y update && apt install -y libgl1-mesa-glx

RUN pip install --upgrade pip

# Install the dependencies specified in setup.py
RUN pip install .

# Install the spacy model
RUN python -m spacy download en_core_web_lg

# Expose the FastAPI URL
EXPOSE 8000

# Set the command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
