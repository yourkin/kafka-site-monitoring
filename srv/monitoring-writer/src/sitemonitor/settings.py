import os

try:
    DATABASE_URL = os.environ["DATABASE_URL"]
except KeyError:
    raise EnvironmentError("DATABASE_URL not set")

MONITORING_TABLE = "monitoring"
