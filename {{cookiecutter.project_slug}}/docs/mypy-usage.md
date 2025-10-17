# Using MyPy in the Antiques project

## Installation

```bash
# Install dev dependencies (including MyPy)
poetry install --no-root

# Or install only MyPy
poetry add --group dev mypy
```

## Main commands

### Type checking

```bash
# Check the entire project
poetry run mypy src/

# Check a specific file
poetry run mypy src/main.py

# Check with detailed error codes
poetry run mypy src/ --show-error-codes

# Check with error context
poetry run mypy src/ --show-error-context

# Check only specific modules
poetry run mypy src/application/ src/domain/
```

### Using Makefile

```bash
# Show all available commands
make help

# Run type checking
make type-check

# Run all checks (lint + format + type check)
make check

# Run CI pipeline
make ci
```

## MyPy configuration

The main MyPy configuration is located in `pyproject.toml` under the `[tool.mypy]` section.

### Core settings

- **python_version**: Python 3.12
- **strict**: false (soft checking by default)
- **ignore_missing_imports**: true (ignore missing imports)
- **warn_return_any**: true (warn on returning Any)
- **no_implicit_optional**: true (require explicit Optional)

### Per-module settings

```toml
# More softer rules for tests and examples
[[tool.mypy.overrides]]
module = [
    "tests.*",
    "examples.*",
]
disallow_untyped_defs = false
disallow_incomplete_defs = false
check_untyped_defs = false

# Ignore missing imports for external libraries
[[tool.mypy.overrides]]
module = [
    "faststream.*",
    "granian.*",
    "structlog.*",
]
ignore_missing_imports = true
```

## Pre-commit integration

MyPy is automatically run on commit via pre-commit hooks:

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks on all files
pre-commit run --all-files

# Run only mypy
pre-commit run mypy
```
