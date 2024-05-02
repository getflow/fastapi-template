import sentry_sdk
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.routers.api import api_router
from app.settings import SENTRY_DSN, SENTRY_ENVIRONMENT

sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
    environment=SENTRY_ENVIRONMENT,
) if SENTRY_DSN else None

app = FastAPI(title="FastAPI template", version="0.1.0")

app.include_router(router=api_router, prefix="")

# adds prometheus metrics route
Instrumentator().instrument(app).expose(
    app, endpoint="/metrics", include_in_schema=False
)
