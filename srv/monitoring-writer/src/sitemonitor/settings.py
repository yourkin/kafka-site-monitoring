import os

try:
    DATABASE_URL = os.environ["DATABASE_URL"]
except KeyError:
    raise EnvironmentError("DATABASE_URL not set")

try:
    TEST_DB_URL = os.environ["TEST_DB_URL"]
except KeyError:
    raise EnvironmentError("TEST_DB_URL not set")

MONITORING_TABLE = "monitoring"
