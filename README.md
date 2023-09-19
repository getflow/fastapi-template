# FastAPI template

FastAPI template with asyncpg, sqlmodel and alembic

# Run

Use `uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload` in development
And `gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000` in production