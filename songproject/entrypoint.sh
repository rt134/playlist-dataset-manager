#!/bin/sh

set -e

echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Importing songs (If not present already)...."
python import_songs.py

if [ "$RUN_TEST" = "true" ]; then
    echo "Running test cases...."
    python manage.py test
fi

echo "Starting the server..."
exec python manage.py runserver 0.0.0.0:8000
