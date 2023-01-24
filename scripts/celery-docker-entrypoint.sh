#!/bin/sh
set -e

echo "Running celery app"
celery -A roomer worker --loglevel=INFO --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler -l info

exec "$@"
