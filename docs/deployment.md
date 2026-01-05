# Deployment Guide

## Prerequisites

- Server with Docker and Docker Compose
- Traefik running as reverse proxy
- GitHub repository with configured secrets

## Server Setup

### 1. Create Application Directory

```bash
ssh user@server
mkdir -p /root/apps
cd /root/apps
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Configure Environment

```bash
cp .env.example .env
nano .env
```

Set your production values:
```
APP_NAME=my-app
APP_DOMAIN=my-app.example.com
DEBUG=false
```

### 3. First Deployment

```bash
docker compose build
docker compose up -d
```

### 4. Verify

```bash
docker ps
curl http://localhost:8000/health
```

## GitHub Configuration

### 1. Add Secrets

Go to: Repository → Settings → Secrets and variables → Actions → Secrets

| Secret | Value |
|--------|-------|
| `SSH_HOST` | Your server hostname |
| `SSH_PORT` | SSH port (usually 22) |
| `SSH_USER` | SSH username |
| `SSH_KEY` | SSH private key content |

### 2. Add Variables

Go to: Repository → Settings → Secrets and variables → Actions → Variables

| Variable | Value |
|----------|-------|
| `APP_NAME` | Your app name |
| `APP_DOMAIN` | Your domain |

## Traefik Integration

The docker-compose.yml includes Traefik labels:

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.${APP_NAME}.rule=Host(`${APP_DOMAIN}`)"
  - "traefik.http.services.${APP_NAME}.loadbalancer.server.port=8000"
```

Make sure your app is on the same Docker network as Traefik:

```yaml
networks:
  web:
    external: true
```

## CI/CD Pipeline

Each template has its own isolated workflow with path filtering:

### Python (`python/**`)
On push to `python/` directory:
1. **Test** - Run pytest + ruff
2. **Release** - Bump version if feat/fix commits (semantic-release)
3. **Deploy** - Pull, build, restart on server
4. **Health Check** - Verify `/health` endpoint

### Alpine.js (`Alpine.js/**`)
On push to `Alpine.js/` directory:
1. **Validate** - HTML validation
2. **Deploy** - Pull, build, restart on server (creates .env on first deploy)
3. **Health Check** - Verify page content

## Rollback

If deployment fails:

```bash
ssh user@server
cd /root/apps/YOUR_REPO
git log --oneline -5  # Find previous working commit
git checkout COMMIT_HASH
docker compose build
docker compose up -d
```

## Monitoring

Check logs:
```bash
docker logs -f YOUR_APP_NAME
```

Check health:
```bash
curl https://YOUR_DOMAIN/health
```

## Troubleshooting

### Container not starting

```bash
docker logs YOUR_APP_NAME
```

### Network issues

```bash
docker network ls
docker network inspect web
```

### Traefik not routing

```bash
docker logs traefik
# Check labels
docker inspect YOUR_APP_NAME | grep -A 20 Labels
```
