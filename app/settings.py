import os

DEBUG = int(os.getenv("DEBUG", "0"))

DATABASE_URL = os.getenv("DATABASE_URL")

SENTRY_DSN = os.getenv("SENTRY_DSN")
SENTRY_ENVIRONMENT = os.getenv("SENTRY_ENVIRONMENT", "development")
