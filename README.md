# UniversalAPI Microservice Template

Universal API microservice templates for various languages with CI/CD, semantic versioning, and Traefik integration.

## Available Templates

| Language | Status | Description |
|----------|--------|-------------|
| [Python (FastAPI)](./python/) | Ready | IP Info API example with FastAPI |
| Go | Coming soon | - |
| Node.js | Coming soon | - |

## Features

- Semantic versioning (automatic version bumps based on commits)
- GitHub Actions CI/CD pipeline
- Docker + Traefik integration
- Health endpoint with version info
- Unit and E2E tests
- Environment-based configuration

## Quick Start

1. Fork/clone this repository
2. Copy the template you want (e.g., `python/`)
3. Configure GitHub Secrets and Variables
4. Push to `main` to trigger deployment

## GitHub Configuration

### Secrets (per repository)

| Secret | Description | Example |
|--------|-------------|---------|
| `SSH_HOST` | Server hostname | `server.example.com` |
| `SSH_PORT` | SSH port | `22` |
| `SSH_USER` | SSH username | `root` |
| `SSH_KEY` | SSH private key | `-----BEGIN...` |

### Variables (per repository)

| Variable | Description | Example |
|----------|-------------|---------|
| `APP_NAME` | Application name | `ip-info-api` |
| `APP_DOMAIN` | Application domain | `ip.example.com` |

## Conventional Commits

This template uses [Conventional Commits](https://www.conventionalcommits.org/) for automatic versioning:

| Prefix | Version bump | Example |
|--------|--------------|---------|
| `feat:` | Minor (0.X.0) | `feat: add new endpoint` |
| `fix:` | Patch (0.0.X) | `fix: handle null values` |
| `docs:` | No bump | `docs: update readme` |
| `chore:` | No bump | `chore: update deps` |

## Documentation

- [Secrets Management](./docs/secrets-management.md)
- [Deployment Guide](./docs/deployment.md)

## License

MIT
