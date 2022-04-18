FROM python:3.10.2-slim-bullseye as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup"

ENV PATH="$POETRY_HOME/bin:$PATH"

FROM python-base as builder-base
RUN apt-get update && apt-get -y install --no-install-recommends curl netcat build-essential && apt-get clean

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
RUN poetry config virtualenvs.create false

# Copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN bash -c "poetry install --no-root"

# Install packages
RUN mkdir -p /opt/app/src/sitechecker /opt/app/src/checkerapi
COPY sitechecker /opt/app/src/sitechecker
WORKDIR /opt/app/src/sitechecker
RUN bash -c "pip install -e ."

COPY checkerapi/src/checkerapi /opt/app/src/checkerapi
WORKDIR /opt/app/src
