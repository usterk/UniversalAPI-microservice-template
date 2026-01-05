# Python FastAPI Microservice Template

IP Info API example using FastAPI with automatic CI/CD, semantic versioning, and Traefik integration.

## Features

- FastAPI with async support
- Automatic semantic versioning
- GitHub Actions CI/CD
- Docker + Traefik integration
- Health endpoint with version
- Unit and E2E tests with pytest
- Pydantic settings for configuration

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API info and available endpoints |
| `/health` | GET | Health check with version info |
| `/ip` | GET | Client IP information |
| `/headers` | GET | All request headers |

## Quick Start

### Local Development

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Run locally
poetry run uvicorn app.main:app --reload

# Or with Docker
docker compose -f docker-compose.dev.yml up --build
```

### Production Deployment

1. Copy to new repo
2. Configure GitHub Secrets and Variables
3. Push to `main`

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `ip-info-api` | Application name |
| `APP_DOMAIN` | - | Domain (e.g., `universalapi.bieda.it`) |
| `APP_PATH_PREFIX` | `/` | URL path prefix (e.g., `/example`) |
| `DEBUG` | `false` | Debug mode |

### GitHub Secrets

| Secret | Description |
|--------|-------------|
| `SSH_HOST` | Server hostname |
| `SSH_PORT` | SSH port |
| `SSH_USER` | SSH username |
| `SSH_KEY` | SSH private key |

### GitHub Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `APP_NAME` | Application name (used in deployment) | `ip-info-api` |
| `APP_DOMAIN` | Domain for routing | `universalapi.bieda.it` |
| `APP_PATH_PREFIX` | URL path prefix | `/example` |

With `APP_DOMAIN=universalapi.bieda.it` and `APP_PATH_PREFIX=/example`:
- `https://universalapi.bieda.it/example/health`
- `https://universalapi.bieda.it/example/ip`

## Project Structure

```
python/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI application
│   ├── config.py       # Pydantic settings
│   └── version.py      # Version loader
├── tests/
│   ├── conftest.py     # Pytest fixtures
│   ├── test_health.py  # Unit tests
│   └── test_e2e.py     # E2E tests
├── .github/workflows/
│   ├── test.yml        # PR tests
│   └── release.yml     # Release & deploy
├── Dockerfile
├── docker-compose.yml      # Production (Traefik)
├── docker-compose.dev.yml  # Development
├── pyproject.toml
├── VERSION
└── .env.example
```

## Versioning

Version is managed automatically using [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release):

- `feat:` commits bump minor version (0.X.0)
- `fix:` commits bump patch version (0.0.X)
- Breaking changes (`BREAKING CHANGE:` in footer) bump major version (X.0.0)

## Testing

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=app

# Run specific test file
poetry run pytest tests/test_health.py -v
```

## Docker

```bash
# Build
docker build -t ip-info-api .

# Run
docker run -p 8000:8000 ip-info-api

# With Traefik (production)
docker compose up -d
```

## License

MIT
