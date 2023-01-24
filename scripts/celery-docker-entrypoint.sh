#!/bin/sh
set -e

# Check postgres service availability.
echo "Check postgres readiness"
python ~/check_service.py --service-name postgres --ip "${DATABASE_HOST}" --port "${DATABASE_PORT}"

echo "Running celery app"
celery -A roomer worker --loglevel=INFO --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler -l info

exec "$@"
