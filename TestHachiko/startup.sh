#!/bin/sh

echo "Waiting for PostgreSQL to start..."
/app/wait-for-it.sh db 5432 --timeout=30 --strict -- echo "PostgreSQL is up - executing command"

echo "Applying database migrations..."
python manage.py migrate
set -x
echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000