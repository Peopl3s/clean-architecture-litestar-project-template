# Using Ruff in the Antiques project

## Installation

```bash
# Install dev dependencies (including Ruff)
poetry install --no-root

# Or install only Ruff
poetry add --group dev ruff
```

## Main commands

### Linting

```bash
# Lint the entire project
poetry run ruff check src/ tests/

# Lint a specific file
poetry run ruff check src/main.py

# Lint with verbose output
poetry run ruff check src/ tests/ --verbose

# Lint only with specific rules
poetry run ruff check src/ --select E,F,W

# Ignore specific rules
poetry run ruff check src/ --ignore E501,W503
```

### Automatic fixing

```bash
# Fix all automatically fixable issues
poetry run ruff check --fix src/ tests/

# Fix only specific rules
poetry run ruff check --fix --select E,F src/

# Show what would be fixed without actually fixing
poetry run ruff check --fix --diff src/
```

### Code formatting

```bash
# Format the entire project
poetry run ruff format src/ tests/

# Check formatting without making changes
poetry run ruff format --check src/ tests/

# Show formatting diff
poetry run ruff format --diff src/
```

### Full check

```bash
# Check and fix all issues
poetry run ruff check --fix src/ tests/
poetry run ruff format src/ tests/

# Or with a single command (if configured in pyproject.toml)
poetry run ruff check --fix src/ tests/ && poetry run ruff format src/ tests/
```

## Using Makefile

```bash
# Show all available commands
make help

# Install dev dependencies
make install-dev

# Lint code
make lint

# Automatically fix issues
make lint-fix

# Format code
make format

# Run all checks
make check

# Run tests
make test

# Run tests with coverage
make test-cov

# Clean cache
make clean

# Set up dev environment
make dev-setup

# Run CI pipeline
make ci
```

## Pre-commit hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks on all files
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```
