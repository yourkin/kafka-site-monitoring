#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z backend-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"


# You can put other setup logic here

# Evaluating passed command:
exec "$@"
