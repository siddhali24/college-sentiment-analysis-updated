# Use Python 3.10 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=sentiment.settings

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Change to the Django project directory
WORKDIR /app/sentiment

# Run Django commands
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# Expose port 7860 (required for Hugging Face Spaces)
EXPOSE 7860

# Start the application with gunicorn
CMD ["bash", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn sentiment.wsgi:application --bind 0.0.0.0:7860 --workers 1 --timeout 120"]