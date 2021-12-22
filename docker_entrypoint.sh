#!/bin/sh

echo "Waiting for database..."

while ! nc -z web-db 5432; do
  sleep 1
done

echo "PostgreSQL successfully started"

exec "$@"