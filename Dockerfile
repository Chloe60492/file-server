# Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Copy dependency file
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy application source code
COPY app/ ./app

# Expose port
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--port", "8000", "--reload"]
