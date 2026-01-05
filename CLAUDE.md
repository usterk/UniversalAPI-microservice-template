# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Microservice template repository with examples:
- **Python/FastAPI** (`python/`) - IP Info API backend with semantic-release
- **Alpine.js** (`Alpine.js/`) - Lightweight frontend demo (~25KB)

## Development Commands (Python)

```bash
cd python

# Install dependencies
poetry install --no-root

# Run tests
poetry run pytest -v

# Run single test file
poetry run pytest tests/test_health.py -v

# Run linter
poetry run ruff check .

# Run locally
poetry run uvicorn app.main:app --reload

# Run with Docker (development)
docker compose -f docker-compose.dev.yml up --build

# Build production image
docker build -t ip-info-api .
```

## Development Commands (Alpine.js)

```bash
cd Alpine.js

# Run with Docker
docker compose up --build

# Or serve locally
cd src && python -m http.server 8080
```

## CI/CD Pipeline

### Python (`python/`)
1. **PRs to main**: `test.yml` runs ruff + pytest
2. **Push to `python/**`**: `release.yml` runs test → semantic-release → deploy
3. Deploy only triggers when semantic-release creates a new version

### Alpine.js (`Alpine.js/`)
1. **Push to `Alpine.js/**`**: `alpine-release.yml` runs HTML validation → deploy
2. Deploys on every push (no semantic-release)

## Conventional Commits

Version bumps are automatic based on commit prefixes:
- `feat:` → minor version (0.X.0)
- `fix:` → patch version (0.0.X)
- `docs:`, `chore:`, `style:`, `refactor:`, `test:` → no version bump

## Key Configuration

| File | Purpose |
|------|---------|
| `python/pyproject.toml` | Poetry deps + semantic-release config |
| `python/docker-compose.yml` | Python production with Traefik |
| `Alpine.js/docker-compose.yml` | Alpine.js production with Traefik |
| `.github/workflows/release.yml` | Python CI/CD (paths: python/**) |
| `.github/workflows/alpine-release.yml` | Alpine.js CI/CD (paths: Alpine.js/**) |

## GitHub Variables for Deployment

Configure in repo Settings → Variables:
- `APP_NAME` - container/router name
- `APP_DOMAIN` - domain for Traefik routing
- `APP_PATH_PREFIX` - URL path prefix (e.g., `/example`)

## Docker Notes

- Multi-stage build: builder (poetry install) → final (alpine + venv)
- Uses `python -m uvicorn` to avoid shebang path issues from copied venv
- Health check uses `127.0.0.1` (not `localhost`) to avoid IPv6 issues
- Resource limits: 256M memory limit, 64M reservation
