# Stage 1: Build stage
FROM python:3.10.12 AS builder

WORKDIR /RathodConstructions

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create a Python virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:${PATH}"

RUN /venv/bin/pip install --upgrade pip setuptools

# Copy requirements and install Python dependencies within the virtual environment
COPY requirements.txt /RathodConstructions/
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt gunicorn

# Stage 2: Production stage
FROM python:3.10.12-slim

WORKDIR /RathodConstructions

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy installed dependencies from the builder stage
COPY --from=builder /venv /venv

# Copy the Django application code
COPY . /RathodConstructions/

# Set the PATH environment variable to include the virtual environment's binaries
ENV PATH="/venv/bin:${PATH}"

# Expose the port used by the application
ARG PORT
EXPOSE $PORT

ENV DJANGO_SETTINGS_MODULE=RathodConstructions.settings

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "RathodConstructions.wsgi:application"]

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "RathodConstructions.asgi:application"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "--timeout", "600", "RathodConstructions.asgi:application"]
