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
RUN apt-get update && apt-get -y install --no-install-recommends curl netcat build-essential libpq5 && apt-get clean

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
RUN poetry config virtualenvs.create false

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN bash -c "poetry install --no-root"

# Add App
RUN mkdir -p /opt/app/src
COPY src/ /opt/app/src
WORKDIR /opt/app/src

# Make entrypoint.sh runnable
COPY entrypoint.sh /opt/app/
RUN chmod +x /opt/app/entrypoint.sh

# Run entrypoint.sh to wait on the database to be available
ENTRYPOINT ["/opt/app/entrypoint.sh"]