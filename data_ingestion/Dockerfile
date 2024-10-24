# Use MySQL as the base image
FROM python:3.12.7

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Python script for data ingestion
COPY ./src /src
WORKDIR /src

CMD ["python", "main.py"]