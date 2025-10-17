# Docker Setup for Antiques project

This document describes how to set up and use Docker for the Antiques application.

{% if cookiecutter.add_docker != "y" %}
> Docker support was not enabled for this project when it was generated.
>
> See the non-Docker run instructions in the main README.
{% else %}

## Docker Commands

### Building images

```bash
# Production image
make docker-build

# Development image
make docker-build-dev

# Testing image
make docker-build-test
```

### Starting services

```bash
# Start all services (production)
make docker-up

# Start development environment
make docker-up-dev

# Stop all services
make docker-down
```

### Database operations

```bash
# Run all database migrations
make docker-migrate
```

{% if cookiecutter.use_database == "postgresql" %}
```bash
# Connect to PostgreSQL
docker-compose exec postgres psql -U antiques_user -d antiques
```
{% elif cookiecutter.use_database == "mysql" %}
```bash
# Connect to MySQL
docker-compose exec mysql mysql -u antiques_user -p antiques
```
{% elif cookiecutter.use_database == "sqlite" %}
```bash
# Connect to SQLite if needed
docker-compose exec sqlite sqlite3 /data/{{ cookiecutter.database_name }}.db
```
{% endif %}

### Testing

```bash
# Run tests in Docker
make docker-test

# View test coverage reports
docker-compose --profile test run --rm test
```

### Debugging

```bash
# View logs
make docker-logs

# Logs for the application only
make docker-logs-app

# Open a shell in the container
make docker-shell
```

## Docker Compose Profiles

### production (default)
- app (production)
{% if cookiecutter.use_database == "postgresql" %}
- postgres
{% elif cookiecutter.use_database == "mysql" %}
- mysql
{% elif cookiecutter.use_database == "sqlite" %}
- sqlite
{% endif %}
{% if cookiecutter.use_cache in ["redis", "keydb", "tarantool", "dragonfly"] %}
- {{ cookiecutter.use_cache }}
{% endif %}

### dev
- app-dev (with hot reload)
{% if cookiecutter.use_database == "postgresql" %}
- postgres (with exposed ports)
{% elif cookiecutter.use_database == "mysql" %}
- mysql (with exposed ports)
{% elif cookiecutter.use_database == "sqlite" %}
- sqlite (with exposed ports)
{% endif %}
{% if cookiecutter.use_cache in ["redis", "keydb", "tarantool", "dragonfly"] %}
- {{ cookiecutter.use_cache }} (with exposed ports)
{% endif %}

### migrate
- migrate (run migrations)

### test
- test (run tests)

### dev-tools
- adminer (web interface for DB)

## Environment Variables

### Required
{% if cookiecutter.use_database == "postgresql" %}
- DATABASE_URL - PostgreSQL connection URL
{% elif cookiecutter.use_database == "mysql" %}
- DATABASE_URL - MySQL connection URL
{% elif cookiecutter.use_database == "sqlite" %}
- DATABASE_URL - SQLite DB path
{% endif %}
{% if cookiecutter.use_cache in ["redis", "keydb", "tarantool", "dragonfly"] %}
- {{ cookiecutter.use_cache | upper }}_URL - {{ cookiecutter.use_cache | capitalize }} connection URL
{% endif %}

### Опциональные
- `ENVIRONMENT` - environment (production/development/testing)
- `LOG_LEVEL` - logging level
- `API_HOST` - API host
- `API_PORT` - API port
- `API_WORKERS` - number of worker processes

## Volumes

### Named Volumes
{% if cookiecutter.use_database == "postgresql" %}
- postgres_data - PostgreSQL data
{% elif cookiecutter.use_database == "mysql" %}
- mysql_data - MySQL data
{% elif cookiecutter.use_database == "sqlite" %}
- sqlite_data - SQLite DB file
{% endif %}
{% if cookiecutter.use_cache in ["redis", "keydb", "tarantool", "dragonfly"] %}
- {{ cookiecutter.use_cache }}_data - cache data
{% endif %}
- app_logs - application logs
- test_reports - test reports

### Bind Mounts (development)
- `./src:/app/src` - source code
- `./tests:/app/tests` - tests
- `./alembic:/app/alembic` - migrations

## Network

All services are connected to the `antiques-network` for isolation.

## Health Checks

Все сервисы имеют health checks:
- **app**: HTTP request to /api/docs
{% if cookiecutter.use_database == "postgresql" %}
- **postgres**: pg_isready
{% elif cookiecutter.use_database == "mysql" %}
- **mysql**: mysqladmin ping
{% elif cookiecutter.use_database == "sqlite" %}
- **sqlite**: ensure DB file exists
{% endif %}
{% if cookiecutter.use_cache in ["redis", "keydb", "tarantool", "dragonfly"] %}
- **{{ cookiecutter.use_cache }}**: {{ cookiecutter.use_cache }}-cli ping
{% endif %}

## Monitoring

### Logs
```bash
# All services
docker-compose logs -f

# Application only
docker-compose logs -f app
```
{% endif %}
