FROM python:3.14-alpine3.21

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir poetry

# Copy dependency files
COPY pyproject.toml poetry.lock* ./

# Install dependencies (no dev deps, no venv, no project install)
RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-root --no-interaction --no-ansi

# Copy application
COPY app ./app
COPY VERSION ./

EXPOSE 8000

# Health check (use 127.0.0.1 instead of localhost for IPv4)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -q --spider http://127.0.0.1:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
