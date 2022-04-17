#!/usr/bin/env bash

docker-compose run --rm website-checker pytest -vs
docker-compose run --rm monitoring-writer python -m pytest -vvs