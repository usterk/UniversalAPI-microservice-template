# Alpine.js Frontend Demo

Lightweight frontend example using Alpine.js + Pico CSS that demonstrates integration with the IP Info API.

## Features

- Alpine.js (~15KB) for reactivity
- Pico CSS (~10KB) for classless styling with dark mode
- nginx:alpine (~8MB) as web server
- Traefik integration
- GitHub Actions deployment

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Demo dashboard showing IP info and headers |

Uses the IP Info API at `/example/*` for data.

## Quick Start

### Local Development

```bash
# Run with Docker
docker compose up --build

# Or serve directly (requires local web server)
cd src && python -m http.server 8080
```

### Production Deployment

1. Configure GitHub Secrets (SSH_HOST, SSH_PORT, SSH_USER, SSH_KEY)
2. Push changes to `Alpine.js/` directory
3. GitHub Actions deploys automatically

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `universalapi-demo` | Container name |
| `APP_DOMAIN` | - | Domain for Traefik routing |

## Stack

| Component | Technology | Size |
|-----------|------------|------|
| JS Framework | Alpine.js | ~15KB |
| CSS | Pico CSS | ~10KB |
| Server | nginx:alpine | ~8MB RAM |

## Docker

```bash
# Build
docker build -t universalapi-demo .

# Run
docker run -p 80:80 universalapi-demo
```

## License

MIT
