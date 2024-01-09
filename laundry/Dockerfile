# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY req.txt /app/
RUN pip install --no-cache-dir -r req.txt

# Copy project
COPY . /app/

# Copy entrypoint script into the image
COPY ./entrypoint.sh /app/entrypoint.sh

# Make the script executable
RUN chmod +x /app/entrypoint.sh

# Run the entrypoint script when the container starts
ENTRYPOINT ["/app/entrypoint.sh"]
