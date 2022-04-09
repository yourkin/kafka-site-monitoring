#!/usr/bin/env bash

docker-compose run --rm website-checker pytest
docker-compose run --rm database-writer pytest