# CHANGELOG


## v0.1.0 (2026-01-05)

### Bug Fixes

- Add --no-root to poetry install in Dockerfile
  ([`b54b581`](https://github.com/usterk/UniversalAPI-microservice-template/commit/b54b5814cb0ff2eafb873a302b75e1fd34bb23f1))

Poetry 2.x requires --no-root to skip installing the project itself

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

- Add --no-root to poetry install in workflows
  ([`8450781`](https://github.com/usterk/UniversalAPI-microservice-template/commit/84507819d90160dc691eee38d6fa7511bddbe881))

Poetry 2.x tries to install the project package by default

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

- Add entrypoints label for Traefik router
  ([`98d56ba`](https://github.com/usterk/UniversalAPI-microservice-template/commit/98d56ba31e45e6da3dbf34c5747f2573e3782c9a))

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

- Change build_command from false to empty string
  ([`068b801`](https://github.com/usterk/UniversalAPI-microservice-template/commit/068b801b637d149988d179ea9d656c9c34c420ce))

semantic-release v9 requires string for build_command

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

- Move workflows to root .github directory
  ([`85eb2c5`](https://github.com/usterk/UniversalAPI-microservice-template/commit/85eb2c539e0b12cca6d872e75456258a04921902))

GitHub Actions requires workflows at repo root .github/workflows/ Updated working directories to use
  python/ subdirectory

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

- Remove invalid version_variable config
  ([`31fbaa0`](https://github.com/usterk/UniversalAPI-microservice-template/commit/31fbaa00d2bee4a72a556abcac12102e68af939c))

Use only version_toml for semantic-release v9

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

- Use 127.0.0.1 instead of localhost in health check
  ([`cc980e1`](https://github.com/usterk/UniversalAPI-microservice-template/commit/cc980e1dd9aa14193afb58647d7f081a4ee33fe9))

localhost may resolve to IPv6 (::1) in Alpine, but uvicorn only listens on IPv4

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

### Features

- Add path prefix support for URL routing
  ([`16f60e5`](https://github.com/usterk/UniversalAPI-microservice-template/commit/16f60e530e9c12f1273d80afcec448fda8466983))

- Add APP_PATH_PREFIX variable for Traefik routing (e.g., /example) - Add stripprefix middleware to
  handle path prefixes - Update GitHub Actions workflow with path prefix support - Update
  documentation with new variables

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

- Initial microservice template with Python/FastAPI example
  ([`3b482b4`](https://github.com/usterk/UniversalAPI-microservice-template/commit/3b482b4e331cf172c13172e6eec62d789970dd6d))

- IP Info API with /health, /ip, /headers endpoints - Docker + Traefik integration - GitHub Actions
  CI/CD with semantic versioning - Unit and E2E tests with pytest - Documentation for secrets
  management and deployment

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
