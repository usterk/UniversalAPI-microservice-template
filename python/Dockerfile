# --- Builder Stage ---
FROM python:3.14-alpine3.21 AS builder

WORKDIR /build

# Install poetry
RUN pip install --no-cache-dir poetry

# Copy dependency files
COPY pyproject.toml poetry.lock* ./

# Install dependencies into .venv in current directory
RUN poetry config virtualenvs.in-project true && \
    poetry install --only main --no-root --no-interaction --no-ansi

# --- Final Stage ---
FROM python:3.14-alpine3.21

# Create a non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Copy virtualenv from builder (it's in /build/.venv)
COPY --from=builder /build/.venv /app/.venv
# Ensure the app uses the virtualenv
ENV PATH="/app/.venv/bin:$PATH"

# Copy application files (with ownership change)
COPY --chown=appuser:appgroup app ./app
COPY --chown=appuser:appgroup VERSION ./

# Switch to non-root user
USER appuser

EXPOSE 8000

# Health check (wget is available in alpine)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget -q --spider http://127.0.0.1:8000/health || exit 1

# Start with proxy headers support for Traefik
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips", "*"]
