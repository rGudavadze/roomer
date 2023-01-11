#!/bin/sh
set -e

# Check postgres service availability.
echo "Check postgres readiness"
python ~/check_service.py --service-name postgres --ip "${DATABASE_HOST}" --port "${DATABASE_PORT}"

echo "Apply database migrations"
python manage.py migrate --noinput

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Running app with gunicorn"
gunicorn --user roomer --bind 0.0.0.0:8000  core.wsgi

exec "$@"
