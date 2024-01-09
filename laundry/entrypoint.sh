#!/bin/bash

# Wait for the database container
# (Optional: Use a script like wait-for-it.sh if you're using a database in another container)

# Run migrations
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

# Start Gunicorn or run Django development server
# gunicorn Amstorhealth.wsgi:application -w 2 -b :8007
# OR
python manage.py runserver 0.0.0.0:8011

# Note: Replace `myproject` with your actual project name
