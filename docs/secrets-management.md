# Secrets Management Best Practices

## Overview

This document describes best practices for managing secrets in microservices deployed with Docker and Traefik.

## Recommended Approach

| Method | Where | Use Case |
|--------|-------|----------|
| `.env` file | On server (not in git) | Production secrets |
| GitHub Secrets | GitHub repository | CI/CD deployment |
| `pydantic-settings` | In application | Environment validation |

## Why NOT Plain Environment Variables?

Plain environment variables in `docker-compose.yml` are:
- Visible in `docker inspect`
- May leak in logs
- Stored in shell history

**Better approach:** Use `env_file: .env` with `.env` in `.gitignore`

## Implementation

### 1. Application Configuration

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "my-app"
    debug: bool = False
    secret_key: str  # Required - must be in .env

    class Config:
        env_file = ".env"
```

### 2. Docker Compose

```yaml
services:
  app:
    env_file:
      - .env  # Not checked into git
```

### 3. .gitignore

```gitignore
.env
*.env
!.env.example
```

### 4. Server Setup

```bash
# On server, create .env from example
cp .env.example .env
# Edit with production values
nano .env
```

## GitHub Secrets

For CI/CD, use GitHub Secrets (Settings → Secrets → Actions):

| Secret | Purpose |
|--------|---------|
| `SSH_HOST` | Server hostname |
| `SSH_PORT` | SSH port |
| `SSH_USER` | SSH username |
| `SSH_KEY` | Private SSH key |

## Future Alternatives

For larger deployments, consider:

1. **HashiCorp Vault** - Enterprise secret management
2. **Docker Swarm Secrets** - Built into Docker Swarm
3. **SOPS** - Encrypted secrets in git
4. **AWS Secrets Manager** - Cloud-native solution

## Security Checklist

- [ ] `.env` is in `.gitignore`
- [ ] No secrets in `docker-compose.yml`
- [ ] No secrets in Dockerfile
- [ ] GitHub Secrets for CI/CD
- [ ] Regular secret rotation
- [ ] Minimal permissions (least privilege)
