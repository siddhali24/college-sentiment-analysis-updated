#!/bin/bash

# Build script for Hugging Face Spaces deployment
echo "Building Django application for Hugging Face Spaces..."

# Navigate to Django project directory
cd sentiment

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"