#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z backend-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

#/opt/app/install_packages.sh

# Evaluating passed command:
exec "$@"
