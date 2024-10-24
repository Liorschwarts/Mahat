# Stage 2: Serve React app with FastAPI
FROM python:3.12.7

WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

# Copy the built React app from the previous stage
COPY --from=build /app/build ./static

# Copy the FastAPI server file
COPY backend/src/server.py .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]