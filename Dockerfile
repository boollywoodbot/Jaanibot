# Base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Set environment variable to avoid Python buffering issues
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python3", "run.py"]
