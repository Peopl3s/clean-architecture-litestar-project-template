<div align="center">

# 🚀 {{ cookiecutter.project_name }}

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Litestar](https://img.shields.io/badge/Litestar-2.18.0+-green.svg)](https://litestar.dev/)
{% if cookiecutter.use_database == "postgresql" %}[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-blue.svg)](https://www.postgresql.org/){% endif %}
{% if cookiecutter.use_database == "sqlite" %}[![SQLite](https://img.shields.io/badge/SQLite-3+-blue.svg)](https://www.sqlite.org/){% endif %}
{% if cookiecutter.use_database == "mysql" %}[![MySQL](https://img.shields.io/badge/MySQL-8+-blue.svg)](https://www.mysql.com/){% endif %}
{% if cookiecutter.use_cache == "redis" %}[![Redis](https://img.shields.io/badge/Redis-7+-red.svg)](https://redis.io/){% endif %}
{% if cookiecutter.use_cache == "keydb" %}[![KeyDB](https://img.shields.io/badge/KeyDB-6+-red.svg)](https://keydb.dev/){% endif %}
{% if cookiecutter.use_cache == "tarantool" %}[![Tarantool](https://img.shields.io/badge/Tarantool-2+-red.svg)](https://www.tarantool.io/){% endif %}
{% if cookiecutter.use_cache == "dragonfly" %}[![Dragonfly](https://img.shields.io/badge/Dragonfly-1+-red.svg)](https://dragonflydb.io/){% endif %}
{% if cookiecutter.add_docker == "y" %}[![Docker](https://img.shields.io/badge/Docker-24+-blue.svg)](https://www.docker.com/){% endif %}

**{{ cookiecutter.project_description }}**

</div>

---

## 🔄 Project Restructuring

### 🎯 Overview

This project has been restructured to follow Python best practices for package organization and distribution. The restructuring transforms the project from a simple `src/` layout to a proper distributable package structure that aligns with modern Python packaging standards.

### 📁 Structure Changes

**Before (Simple Layout):**
```
{{cookiecutter.project_slug}}/
├── src/
│   ├── main.py
│   ├── application/
│   ├── config/
│   ├── domain/
│   ├── infrastructures/
│   └── presentation/
```

**After (Distributable Package Layout):**
```
{{cookiecutter.project_slug}}/
├── src/
│   └── {{cookiecutter.project_slug}}/  # Main package
│       ├── __init__.py
│       ├── main.py
│       ├── application/
│       ├── config/
│       ├── domain/
│       ├── infrastructures/
│       └── presentation/
```

### ✅ Benefits of New Structure

1. **📦 Distribution Ready**: The package can be easily installed via `pip install -e .` and distributed to PyPI
2. **🚀 Multiple Run Methods**: Application can be run in several ways:
   - `python -m {{cookiecutter.project_slug}}.main` (module execution)
   - `{{cookiecutter.project_slug}}` (entry point script after installation)
   - Direct import as a library
3. **🔒 No Name Conflicts**: Package name prevents conflicts with built-in or third-party modules
4. **📈 Predictable Imports**: All imports use consistent package structure
5. **🛠️ Development Friendly**: Supports editable installs for development
6. **📊 Better Tooling Integration**: Improved integration with linters, type checkers, and testing tools

### 🔄 Import Changes

**Before:**
```python
from src.application.use_cases.get_artifact import ProcessArtifactUseCase
from src.domain.entities.artifact import ArtifactEntity
```

**After:**
```python
from {{cookiecutter.project_slug}}.application.use_cases.get_artifact import ProcessArtifactUseCase
from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity
```

### 🚀 Running the Application

**New ways to run the application:**

```bash
# Method 1: Module execution (recommended for development)
poetry run python -m {{cookiecutter.project_slug}}.main

# Method 2: Entry point script (after installation)
poetry install  # Install the package
{{cookiecutter.project_slug}}  # Run using entry point

# Method 3: Direct execution (if main.py has shebang)
./src/{{cookiecutter.project_slug}}/main.py
```

### 🛠️ Development Commands Updated

All development commands have been updated to work with the new package structure:

```bash
# Code quality checks now target the package
make lint        # Checks src/{{cookiecutter.project_slug}}/
make format      # Formats src/{{cookiecutter.project_slug}}/
make type-check  # Type checks src/{{cookiecutter.project_slug}}/

# Testing with updated coverage paths
make test-cov    # Coverage for src/{{cookiecutter.project_slug}}/
```

### 📦 Installation and Distribution

The project can now be easily installed and distributed:

```bash
# Development installation
pip install -e .

# Build distribution
python -m build

# Upload to PyPI (when ready)
twine upload dist/*
```

This restructuring ensures the project follows modern Python packaging standards while maintaining the clean architecture principles and making the codebase more maintainable and distributable.

---

## 📖 Project Description

**{{ cookiecutter.project_name }}** is an elegant and scalable web application developed for {{ cookiecutter.project_description.lower() }}. The system is built using modern architectural patterns and cutting-edge technologies, ensuring high performance, reliability, and ease of operation.

### 🎯 Key Features

- 🏗️ **Clean Architecture** with clear separation of concerns
- ⚡ **High Performance** thanks to asynchronous request processing
{% if cookiecutter.use_cache == "redis" %}- 🧠 **Intelligent Caching** with Redis for performance optimization{% endif %}
{% if cookiecutter.use_cache == "keydb" %}- 🧠 **Intelligent Caching** with KeyDB for performance optimization{% endif %}
{% if cookiecutter.use_cache == "tarantool" %}- 🧠 **Intelligent Caching** with Tarantool for performance optimization{% endif %}
{% if cookiecutter.use_cache == "dragonfly" %}- 🧠 **Intelligent Caching** with Dragonfly for performance optimization{% endif %}
{% if cookiecutter.use_database == "postgresql" %}- 🗄️ **Reliable Data Storage** in PostgreSQL with transaction support{% endif %}
{% if cookiecutter.use_database == "sqlite" %}- 🗄️ **Lightweight Data Storage** in SQLite{% endif %}
{% if cookiecutter.use_database == "mysql" %}- 🗄️ **Reliable Data Storage** in MySQL with transaction support{% endif %}
{% if cookiecutter.add_docker == "y" %}- 🐳 **Containerization** with Docker for easy deployment and scaling{% endif %}
- 📊 **Automatic API Documentation** with Swagger UI and ReDoc
- 🔒 **Strict Data Validation** using dataclasses with custom validation (Pydantic-free in application layer)
- 🔄 **Clean DTO Architecture** with separation between application and infrastructure layers
{% if cookiecutter.add_tests == "y" %}- 🧪 **Comprehensive Testing** with pytest and high code coverage{% endif %}

---

## 🛠️ Technology Stack

### 🎨 Backend
- **Language**: Python 3.12+ with modern features
- **Framework**: Litestar 2.18.0 for high-performance APIs
- **ORM**: SQLAlchemy 2.0 with async support
- **Validation**: Custom validation in dataclasses (application layer) + Pydantic (infrastructure layer)
- **DI Container**: Dishka for dependency management

{% if cookiecutter.use_database == "postgresql" %}
### 🗄️ Database
- **Primary DBMS**: PostgreSQL 16+ with asyncpg
- **Migrations**: Alembic for database schema management
{% endif %}
{% if cookiecutter.use_database == "sqlite" %}
### 🗄️ Database
- **Primary DBMS**: SQLite 3+ with aiosqlite
- **Migrations**: Alembic for database schema management
{% endif %}
{% if cookiecutter.use_database == "mysql" %}
### 🗄️ Database
- **Primary DBMS**: MySQL 8+ with aiomysql
- **Migrations**: Alembic for database schema management
{% endif %}

{% if cookiecutter.use_cache == "redis" %}
### 🧠 Caching
- **Caching**: Redis 7+ for performance optimization
{% endif %}
{% if cookiecutter.use_cache == "keydb" %}
### 🧠 Caching
- **Caching**: KeyDB 6+ for performance optimization
{% endif %}
{% if cookiecutter.use_cache == "tarantool" %}
### 🧠 Caching
- **Caching**: Tarantool 2+ for performance optimization
{% endif %}
{% if cookiecutter.use_cache == "dragonfly" %}
### 🧠 Caching
- **Caching**: Dragonfly 1+ for performance optimization
{% endif %}

{% if cookiecutter.add_docker == "y" %}
### 🐳 Infrastructure
- **Containerization**: Docker and Docker Compose
- **Web Server**: Uvicorn with HTTP/2 support
- **Asynchronous**: Full async/await support
{% endif %}

{% if cookiecutter.add_tests == "y" %}
### 🧪 Development and Testing
- **Testing**: pytest with async test support
- **Linting**: ruff for fast code checking
- **Typing**: mypy for static type checking
- **Formatting**: automatic code formatting
{% if cookiecutter.add_precommit == "y" %}- **Pre-commit**: hooks for code quality control{% endif %}
{% endif %}

---

## 🏁 Quick Start

### 📋 Prerequisites

- Python 3.12+
{% if cookiecutter.add_docker == "y" %}- Docker and Docker Compose{% endif %}
- Poetry (recommended) or pip

### 🚀 Installation and Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
```

#### 2. Install Dependencies
```bash
# Recommended way with Poetry
poetry install

# Alternative way with pip
pip install -e .
```

#### 3. Set Up Environment
```bash
cp .env.template .env
# Edit the .env file with your settings
```

#### 4. Run with Docker (Recommended)
```bash
# Complete development environment setup
make dev-setup-docker

# Start the application
make docker-up-dev
```

{% if cookiecutter.add_docker == "y" %}
#### 5. Local Run
```bash
# Start dependencies
{% if cookiecutter.use_database == "postgresql" %}docker-compose up -d postgres{% endif %}{% if cookiecutter.use_database == "mysql" %}docker-compose up -d mysql{% endif %}{% if cookiecutter.use_database == "sqlite" %}docker-compose up -d sqlite-init{% endif %}{% if cookiecutter.use_cache == "redis" %} redis{% endif %}{% if cookiecutter.use_cache == "keydb" %} keydb{% endif %}{% if cookiecutter.use_cache == "tarantool" %} tarantool{% endif %}{% if cookiecutter.use_cache == "dragonfly" %} dragonfly{% endif %}

# Apply migrations
make migrate

# Start the application (new package structure)
poetry run python -m {{cookiecutter.project_slug}}.main

# Alternative: run using the entry point script after installation
{{cookiecutter.project_slug}}
```
{% endif %}

---

## 📚 API Documentation

Once the application is running, documentation is available at the following addresses:

### 🎯 Swagger UI
```
http://localhost:8000/api/docs
```
Interactive documentation with API testing capabilities directly in the browser.

### 📖 ReDoc
```
http://localhost:8000/api/redoc
```
Styled documentation with three-panel navigation.

### 📄 OpenAPI Schema
```
http://localhost:8000/api/openapi.json
```
API specification in OpenAPI 3.0 format.

---

## 🏗️ Project Architecture

The application follows **Clean Architecture** principles, ensuring clear separation of concerns, layer independence, and testability. The architecture is built around business logic that is isolated from external dependencies such as databases, frameworks, and other infrastructure components.

### 📐 General Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                       │
│                   (Presentation Layer)                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐│
│  │   REST API      │  │      CLI        │  │   GraphQL?      ││
│  │  (Litestar)     │  │                 │  │                 ││
│  └─────────────────┘  └─────────────────┘  └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                        │
│                     (Application Layer)                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐│
│  │    Use Cases    │  │      DTOs       │  │   Interfaces    ││
│  │ (Business Rules)│  │  (Data Transfer) │  │    (Ports)      ││
│  │                 │  │   Objects)       │  │                 ││
│  └─────────────────┘  └─────────────────┘  └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DOMAIN LAYER                           │
│                   (Domain Layer)                           │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐│
│  │    Entities     │  │  Value Objects  │  │   Services      ││
│  │   (Entities)    │  │(Value Objects)  │  │ (Domain         ││
│  │                 │  │                 │  │   Services)     ││
│  └─────────────────┘  └─────────────────┘  └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  INFRASTRUCTURE LAYER                       │
│                (Infrastructure Layer)                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐│
│  │   Databases     │  │      Cache      │  │ Message Brokers││
│  │ (PostgreSQL,    │  │    (Redis)      │  │                 ││
│  │   SQLAlchemy)   │  │                 │  │                 ││
│  └─────────────────┘  └─────────────────┘  └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

### 📁 Project Structure

Below is a detailed directory tree reflecting the architectural structure with the new distributable package layout:

```
.
├── 📁 src/                          # Source code root
│   └── 📁 {{cookiecutter.project_slug}}/  # Main application package
│       ├── 📁 domain/               # Domain layer (business logic)
│       │   ├── 📁 entities/         # Domain entities
│       │   │   └── artifact.py      # "Artifact" entity
│       │   ├── 📁 services/         # Domain services
│       │   ├── 📁 value_objects/    # Value objects
│       │   │   ├── era.py           # "Era" value object
│       │   │   └── material.py      # "Material" value object
│       │   ├── exceptions.py        # Domain exceptions
│       │   └── __init__.py
│       │
│       ├── 📁 application/          # Application layer
│       │   ├── 📁 dtos/             # Data Transfer Objects
│       │   │   └── artifact.py      # DTO for "Artifact"
│       │   ├── 📁 interfaces/      # Interfaces (ports)
│       │   │   ├── cache.py         # Caching interface
│       │   │   ├── http_clients.py  # HTTP client interfaces
│       │   │   ├── mappers.py       # Mapper interfaces
│       │   │   ├── message_broker.py # Message broker interfaces
│       │   │   └── repositories.py # Repository interfaces
│       │   │   └── uow.py          # Unit of Work interfaces
│       │   ├── 📁 use_cases/       # Use cases (interactors)
│       │   │   └── get_artifact.py # "Get Artifact" use case
│       │   ├── exceptions.py        # Application exceptions
│       │   ├── mappers.py           # Data mappers
│       │   └── __init__.py
│       │
│       ├── 📁 presentation/        # Presentation layer
│       │   ├── 📁 api/             # API
│       │   │   └── 📁 rest/        # REST API
│       │   │       ├── 📁 v1/      # API version v1
│       │   │       │   ├── 📁 controllers/ # Controllers
│       │   │       │   │   └── artifact_controller.py
│       │   │       │   ├── exceptions.py   # API exception handlers
│       │   │       │   └── routers.py      # Router
│       │   │       └── middlewares.py   # Middleware layers
│       │   └── 📁 cli/            # CLI interface
│       │   └── __init__.py
│       │
│       ├── 📁 infrastructures/     # Infrastructure layer
│       │   ├── 📁 broker/          # Message broker
│       │   │   └── publisher.py    # Message publisher
│       │   ├── 📁 cache/           # Caching
│       │   │   └── redis_client.py # Redis client
│       │   ├── 📁 db/              # Database operations
│       │   │   ├── 📁 models/      # ORM models
│       │   │   │   └── artifact.py # "Artifact" model
│       │   │   ├── 📁 repositories/ # Repositories
│       │   │   │   └── artifact.py # "Artifact" repository
│       │   │   ├── 📁 migrations/  # Database migrations
│       │   │   │   └── versions/   # Migration files
│       │   │   │   └── env.py      # Alembic environment
│       │   │   │   └── script.py.mako # Migration template
│       │   │   ├── uow.py          # SQLAlchemy Unit of Work
│       │   │   ├── exceptions.py   # Database exceptions
│       │   │   ├── session.py      # Database session management
│       │   │   └── __init__.py
│       │   ├── 📁 http/            # HTTP clients
│       │   │   └── clients.py      # HTTP client implementations
│       │   ├── 📁 mappers/         # Infrastructure mappers
│       │   │   └── artifact.py     # Mapper for DTO conversion
│       │   └── __init__.py
│       │
│       ├── 📁 config/             # Configuration
│       │   ├── 📁 ioc/            # Dependency Injection
│       │   │   ├── di.py          # DI container setup
│       │   │   └── providers.py   # Dependency providers
│       │   ├── base.py            # Base configuration
│       │   ├── logging.py         # Logging configuration
│       │   └── __init__.py
│       │
│       └── main.py                # Application entry point
│
├── 📁 tests/                        # Test suite
│   ├── 📁 test_application/         # Application layer tests
│   │   └── 📁 test_use_cases/       # Use case tests
│   ├── 📁 test_domain/              # Domain layer tests
│   │   ├── 📁 test_entities/        # Entity tests
│   │   └── 📁 test_value_objects/   # Value object tests
│   ├── 📁 test_infrastructure/      # Infrastructure layer tests
│   │   ├── 📁 test_cache/           # Caching tests
│   │   └── 📁 test_db/              # Database tests
│   │       ├── 📁 test_models/      # ORM model tests
│   │       └── 📁 test_repositories/ # Repository tests
│   ├── 📁 test_presentation/        # Presentation layer tests
│   │   └── 📁 test_api/             # API tests
│   │       └── 📁 test_controllers/ # Controller tests
│   ├── 📁 test_integration/         # Integration tests
│   ├── conftest.py                  # pytest fixtures
│   └── __init__.py
│
├── 📁 docs/                         # Documentation
│   ├── caching.md                   # Caching documentation
│   ├── docker.md                    # Docker documentation
│   ├── environment.md               # Environment setup
│   ├── migrations.md                # Migration guide
│   ├── mypy-usage.md                # MyPy usage
│   └── ruff-usage.md                # Ruff usage
│
├── 📁 scripts/                      # Utility scripts
│   ├── init-db.sql                  # Database initialization script
│   ├── migrate.sh                   # Migration script
│   └── setup-env.sh                 # Environment setup script
│
├── .dockerignore                    # Docker exclusions
├── .git-commit-template             # Commit template
├── .gitignore                       # Git exclusions
├── .pre-commit-config.yaml          # Pre-commit configuration
├── .python-version                  # Python version
├── alembic.ini                      # Alembic configuration
├── docker-compose.yml               # Docker Compose
├── docker-compose.override.yml      # Docker Compose override
├── Dockerfile                       # Dockerfile
├── env.template                     # Environment template
├── LICENSE                          # License
├── Makefile                         # Makefile with commands
├── pyproject.toml                   # Project configuration and dependencies
├── README.md                        # Project documentation
└── poetry.lock                      # Poetry dependency lock file
```

### 🎯 Domain Layer

**Purpose**: The core of the application, containing business logic and domain entities. This layer does not depend on other layers or external technologies.

**Key Components**:
- **`entities/`**: Main business model entities (e.g., `Artifact`).
  - Define the structure and behavior of key objects.
  - Contain business rules and validation.
  - Example: `src/domain/entities/artifact.py`
- **`value_objects/`**: Value objects representing immutable data types.
  - Encapsulate logic related to specific values (e.g., `Era`, `Material`).
  - Provide strong typing and validation.
  - Examples: `src/domain/value_objects/era.py`, `src/domain/value_objects/material.py`
- **`services/`**: Domain services implementing complex business logic that doesn't belong to a single entity.
  - Coordinate interaction between multiple entities or value objects.
- **`exceptions.py`**: Domain-specific exceptions.

**Principles**:
- **Independence**: Completely isolated from frameworks, databases, and UI.
- **Purity**: Contains only business logic, without technical details.

### 📋 Application Layer

**Purpose**: Orchestrates the domain layer to perform specific application tasks (use cases). Defines interfaces for infrastructure interaction.

**Key Components**:
- **`use_cases/`**: Use cases (or interactors).
  - Implement specific system usage scenarios (e.g., `GetArtifact`).
  - Coordinate data flow between entities and infrastructure.
  - Example: `src/application/use_cases/get_artifact.py`
- **`dtos/`**: Data Transfer Objects.
  - Used for data transfer between layers, especially in APIs.
  - **Pydantic-free DTOs** using plain dataclasses with validation in `__post_init__` methods.
  - Example: `src/application/dtos/artifact.py`
- **`interfaces/`**: Interfaces (ports) that define contracts for infrastructure implementations.
  - `repositories.py`: Defines interfaces for data access (e.g., `ArtifactRepository`).
  - `cache.py`: Defines interfaces for caching.
  - `message_broker.py`: Defines interfaces for working with message brokers.
  - `http_clients.py`: Defines interfaces for external HTTP calls.
- **`mappers.py`**: Objects for transforming data between domain entities and DTOs.
- **`exceptions.py`**: Application-level exceptions.

**Principles**:
- **Orchestration**: Contains no business logic, only manages its execution.
- **Dependencies**: Depends only on the domain layer and abstractions (interfaces) from the infrastructure layer.

### 🌐 Presentation Layer

**Purpose**: Responsible for interaction with the external world: handling HTTP requests, displaying data, CLI interfaces.

**Key Components**:
- **`api/`**: REST API implementation.
  - `rest/v1/controllers/`: Controllers that handle incoming HTTP requests. They call corresponding use cases from the application layer.
    - Example: `src/presentation/api/rest/v1/controllers/artifact_controller.py`
  - `rest/v1/routers.py`: Defines API routes (endpoints).
  - `rest/v1/exceptions.py`: Exception handlers for HTTP responses.
  - `rest/middlewares.py`: Middleware layers for request processing (logging, authentication, etc.).
- **`cli/`**: Command-line interface for application management (if applicable).

**Principles**:
- **Thinness**: Contains minimal logic, mostly delegating tasks to the application layer.
- **Adaptation**: Transforms data from a client-friendly format (JSON) to DTOs for the application layer.

### 🔧 Infrastructure Layer

**Purpose**: Contains specific technology implementations: databases, caches, external APIs, etc. This layer implements interfaces defined in the application layer.

**Key Components**:
- **`db/`**: Database operations.
  - `models/`: ORM models (SQLAlchemy) representing database tables.
    - Example: `src/infrastructures/db/models/artifact.py`
  - `repositories/`: Repository implementations for data access. They implement interfaces from `application/interfaces/repositories.py`.
    - Example: `src/infrastructures/db/repositories/artifact.py`
  - `session.py`: Database session management.
  - `exceptions.py`: Database-specific exceptions.
- **`cache/`**: Caching implementation.
  - `redis_client.py`: Specific caching implementation using Redis, implementing the `application/interfaces/cache.py` interface.
- **`http/`**: HTTP clients for interacting with external services.
  - `clients.py`: Client implementations implementing `application/interfaces/http_clients.py` using dictionary serialization for external communication.
- **`broker/`**: Working with message brokers (RabbitMQ, Kafka, etc.).
  - `publisher.py`: Message publishing implementation using dictionary serialization.
- **`mappers/`**: Infrastructure mappers for converting between application DTOs and dictionaries for external API communication.
  - `artifact.py`: Mapper for DTO ↔ dictionary conversion and JSON serialization.

**Principles**:
- **Implementation**: Contains "dirty" work for interacting with external systems.
- **Dependency**: Depends on the application layer (implements its interfaces) and may depend on the domain layer (e.g., for data mapping).

### ⚙️ Config Layer

**Purpose**: Manages application configuration and dependencies (Dependency Injection).

**Key Components**:
- **`ioc/` (Inversion of Control)**: Dependency container.
  - `di.py`: DI container setup and assembly (using the `dishka` library).
  - `providers.py`: Dependency providers that "tell" the container how to create class instances (e.g., which `ArtifactRepository` implementation to use).
- **Configuration Modules**: Modular configuration system with separate settings for different domains:
  - `app.py`: Core application settings (app name, environment, debug mode, etc.)
  - `database.py`: Database configuration (PostgreSQL connection settings, URL generation)
  - `redis.py`: Redis cache configuration (connection, TTL, prefixes)
  - `external_apis.py`: External API settings (museum API, catalog API, timeouts)
  - `broker.py`: Message broker configuration (Kafka/RabbitMQ settings, retry policies)
  - `cors.py`: CORS configuration (allowed origins, methods, headers)
  - `settings.py`: Main settings facade that combines all configuration modules
  - `base.py`: Backward compatibility wrapper that re-exports the new Settings
- **`logging.py`**: Logging system configuration.

### 🔄 Data Flow in Application (Example: GET /api/v1/artifacts/{id})

1. **Presentation Layer**: Request arrives at `ArtifactController`.
2. **Controller** calls the corresponding **Use Case** from the **Application Layer**, passing it a DTO with request data.
3. **Use Case**:
   a. Requests the required `ArtifactRepository` implementation from the **DI container** (interface from Application Layer, implementation from Infrastructure Layer).
   b. Calls the `get_by_id()` method on the repository.
4. **Repository (Infrastructure Layer)**:
   a. Executes a query to **PostgreSQL** using **SQLAlchemy**.
   b. Transforms the query result (ORM model) into a domain `Artifact` entity (Domain Layer).
   c. Returns the entity to the Use Case.
5. **Use Case**:
   a. Executes additional business logic (if required).
   b. Transforms the domain `Artifact` entity into an `ArtifactDTO` (Application Layer).
   c. Returns the DTO to the **Controller**.
6. **Controller (Presentation Layer)**:
   a. Serializes the `ArtifactDTO` to JSON.
   b. Sends the HTTP response to the client.

### 🔄 Architecture Principles

1.  **Dependency Rule**:
    - Source code dependencies can only point inward.
    - Inner layers (Domain) should know nothing about outer layers (Infrastructure, Presentation).
    - Dependencies are implemented through abstractions (interfaces) defined in inner layers.

2.  **Single Responsibility Principle**:
    - Each module, class, function has one and only one reason to change.

3.  **Open/Closed Principle**:
    - Software entities (classes, modules, functions) should be open for extension but closed for modification.
    - For example, to add a new data storage method (e.g., MongoDB), we create a new repository implementation in the Infrastructure Layer without changing code in the Application or Domain layers.

4.  **Inversion of Control**:
    - Dependency management is transferred to an external container (DI container).
    - Components don't create their dependencies themselves but receive them "from outside".

5.  **Testability**:
    - Thanks to interfaces and DI, all components are easily unit testable by replacing real dependencies with mocks and stubs.

---

## 🧩 Identity Map

### 📋 What is Identity Map?

**Identity Map** is a design pattern that ensures each object is loaded from the database only once during the entire lifecycle of an operation (e.g., a single HTTP request). When data is requested again, the existing object instance is returned instead of creating a new one. This ensures:

- **Data Consistency**: All parts of the application work with the same object instance
- **Performance**: Reduces the number of database queries
- **Memory Efficiency**: Prevents creation of duplicate objects
- **Integrity**: Changes made in one place are visible throughout the application

### 🏗️ Current Implementation in the Project

The current project architecture implements a basic version of Identity Map through a combination of patterns:

#### 1. **Use Case Level Caching**

```python
# src/application/use_cases/get_artifact.py
async def execute(self, inventory_id: str | UUID) -> ArtifactDTO:
    inventory_id_str = str(inventory_id) if isinstance(inventory_id, UUID) else inventory_id

    # 1. Check cache (first level Identity Map)
    cached_artifact: ArtifactDTO | None = await self.cache_client.get(inventory_id_str)
    if cached_artifact:
        return ArtifactDTO.model_validate(cached_artifact)

    # 2. Check repository (second level)
    artifact_entity: ArtifactEntity | None = await self.repository.get_by_inventory_id(inventory_id_str)
    if artifact_entity:
        artifact_dto = self.artifact_mapper.to_dto(artifact_entity)
        # Save to cache for future requests
        await self.cache_client.set(inventory_id_str, artifact_dto.model_dump_json())
        return artifact_dto
```

#### 2. **Caching Interface**

```python
# src/application/interfaces/cache.py
class CacheProtocol(Protocol):
    async def get(self, key: str) -> Any | None: ...
    async def set(self, key: str, value: Any, ttl: int | None = None) -> bool: ...
    async def delete(self, key: str) -> bool: ...
    async def exists(self, key: str) -> bool: ...
    async def clear(self, pattern: str) -> int: ...
```

#### 3. **Redis Caching Implementation**

```python
# src/infrastructures/cache/redis_client.py
@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RedisCacheClient(CacheProtocol):
    client: Redis
    ttl: int | None = None

    async def get(self, key: str) -> Any | None:
        try:
            value = await self.client.get(key)
            if value is None:
                return None
            return json.loads(value)
        except (ConnectionError, redis.exceptions.RedisError) as e:
            logger.error("Redis get operation failed", extra={"key": key, "error": str(e)})
            return None
```

### 🔄 How Identity Map Works in Current Architecture

#### **Data Flow for Artifact Request:**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   HTTP Request  │    │   Use Case      │    │   Cache Layer   │
│   (Controller)  │───▶│   (GetArtifact) │───▶│   (Redis)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │                        │
                              │ YES                    │ HIT
                              │◀────────────────────────┘
                              │
                              │ NO
                              ▼
                       ┌─────────────────┐
                       │  Repository     │
                       │  (PostgreSQL)   │
                       └─────────────────┘
                              │
                              │ FOUND
                              │◀────────────────────────┐
                              │                        │
                              │ NOT FOUND              │
                              ▼                        │
                       ┌─────────────────┐           │
                       │ External API    │           │
                       │ (Museum API)    │           │
                       └─────────────────┘           │
                              │                        │
                              │◀────────────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Cache Store   │
                       │   (Save to Redis)│
                       └─────────────────┘
```

#### **Key Features of Current Implementation:**

1. **Two-level Caching**:
   - **First level**: Redis cache for fast data access
   - **Second level**: Database as source of truth

2. **End-to-end Identification**:
   - Using `inventory_id` as a unique key
   - Guarantee that within a single request, an object will be loaded only once

3. **Automatic Invalidation**:
   - Cache is updated automatically when changes are saved
   - TTL support for data expiration

### 🚀 Enhanced Identity Map Implementation

For a more complete pattern implementation, the following components can be added:

#### 1. **Identity Map Manager**

```python
# src/application/interfaces/identity_map.py
from typing import Protocol, TypeVar, Generic, Any
from uuid import UUID

T = TypeVar('T')

class IdentityMapProtocol(Protocol[T]):
    async def get(self, entity_id: str | UUID) -> T | None: ...
    async def add(self, entity_id: str | UUID, entity: T) -> None: ...
    async def remove(self, entity_id: str | UUID) -> None: ...
    async def clear(self) -> None: ...
    async def contains(self, entity_id: str | UUID) -> bool: ...
    async def get_all(self) -> dict[str | UUID, T]: ...
```

#### 2. **Identity Map Implementation**

```python
# src/infrastructures/cache/identity_map.py
from dataclasses import dataclass, field
from typing import Dict, Any, final
from uuid import UUID

from src.application.interfaces.identity_map import IdentityMapProtocol

@final
@dataclass(frozen=True, slots=True, kw_only=True)
class InMemoryIdentityMap(IdentityMapProtocol[Any]):
    _map: Dict[str | UUID, Any] = field(default_factory=dict)

    async def get(self, entity_id: str | UUID) -> Any | None:
        return self._map.get(entity_id)

    async def add(self, entity_id: str | UUID, entity: Any) -> None:
        self._map[entity_id] = entity

    async def remove(self, entity_id: str | UUID) -> None:
        self._map.pop(entity_id, None)

    async def clear(self) -> None:
        self._map.clear()

    async def contains(self, entity_id: str | UUID) -> bool:
        return entity_id in self._map

    async def get_all(self) -> dict[str | UUID, Any]:
        return self._map.copy()
```

#### 3. **Repository with Identity Map Support**

```python
# src/infrastructures/db/repositories/artifact_with_identity_map.py
from dataclasses import dataclass
from typing import final
from uuid import UUID

from src.application.interfaces.identity_map import IdentityMapProtocol
from src.application.interfaces.repositories import ArtifactRepositoryProtocol
from src.domain.entities.artifact import ArtifactEntity

@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ArtifactRepositoryWithIdentityMap(ArtifactRepositoryProtocol):
    base_repository: ArtifactRepositoryProtocol
    identity_map: IdentityMapProtocol[ArtifactEntity]

    async def get_by_inventory_id(self, inventory_id: str | UUID) -> ArtifactEntity | None:
        # 1. Check Identity Map
        cached_entity = await self.identity_map.get(inventory_id)
        if cached_entity is not None:
            return cached_entity

        # 2. If not in Identity Map, load from database
        entity = await self.base_repository.get_by_inventory_id(inventory_id)

        # 3. Save to Identity Map for future requests
        if entity is not None:
            await self.identity_map.add(inventory_id, entity)

        return entity

    async def save(self, artifact: ArtifactEntity) -> None:
        # 1. Save to database
        await self.base_repository.save(artifact)

        # 2. Update Identity Map
        await self.identity_map.add(artifact.inventory_id, artifact)
```

#### 4. **Use Case with Identity Map Support**

```python
# src/application/use_cases/get_artifact_with_identity_map.py
from dataclasses import dataclass
from typing import TYPE_CHECKING
from uuid import UUID

from src.application.interfaces.cache import CacheProtocol
from src.application.interfaces.identity_map import IdentityMapProtocol
from src.application.interfaces.repositories import ArtifactRepositoryProtocol

if TYPE_CHECKING:
    from src.domain.entities.artifact import ArtifactEntity

@dataclass(frozen=True, slots=True, kw_only=True)
class ProcessArtifactUseCaseWithIdentityMap:
    repository: ArtifactRepositoryProtocol  # Already with Identity Map
    cache_client: CacheProtocol
    request_identity_map: IdentityMapProtocol[ArtifactEntity]  # For single request

    async def execute(self, inventory_id: str | UUID) -> ArtifactEntity:
        inventory_id_str = str(inventory_id) if isinstance(inventory_id, UUID) else inventory_id

        # 1. Check request-level Identity Map
        request_cached = await self.request_identity_map.get(inventory_id_str)
        if request_cached is not None:
            return request_cached

        # 2. Check Redis cache
        redis_cached = await self.cache_client.get(inventory_id_str)
        if redis_cached is not None:
            entity = self._deserialize_to_entity(redis_cached)
            await self.request_identity_map.add(inventory_id_str, entity)
            return entity

        # 3. Load from repository (with Identity Map support)
        entity = await self.repository.get_by_inventory_id(inventory_id_str)
        if entity is not None:
            await self.request_identity_map.add(inventory_id_str, entity)
            await self.cache_client.set(inventory_id_str, self._serialize_entity(entity))
            return entity

        raise ValueError(f"Artifact with inventory_id {inventory_id_str} not found")
```

### 🎯 Benefits of Enhanced Implementation

#### **1. Multi-level Identification**

```
┌─────────────────────────────────────────────────────────────┐
│                    Request Scope                            │
│              (Identity Map for single request)             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐│
│  │   HTTP Request  │  │   Use Case 1    │  │   Use Case 2    ││
│  │                 │  │                 │  │                 ││
│  │  ┌───────────┐  │  │  ┌───────────┐  │  │  ┌───────────┐  ││
│  │  │ Identity  │  │  │  │ Identity  │  │  │  │ Identity  │  ││
│  │  │   Map     │  │  │  │   Map     │  │  │  │   Map     │  ││
│  │  └───────────┘  │  │  └───────────┘  │  │  └───────────┘  ││
│  └─────────────────┘  └─────────────────┘  └─────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Scope                        │
│                 (Redis cache for entire app)               │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                    Redis Cache                         ││
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐      ││
│  │  │  Artifact 1 │ │  Artifact 2 │ │  Artifact 3 │      ││
│  │  └─────────────┘ └─────────────┘ └─────────────┘      ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Persistence Scope                        │
│                 (Database as source of truth)              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                   PostgreSQL                           ││
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐      ││
│  │  │  Artifact 1 │ │  Artifact 2 │ │  Artifact 3 │      ││
│  │  └─────────────┘ └─────────────┘ └─────────────┘      ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

#### **2. Consistency Guarantees**

- **Within single request**: All components work with the same object instance
- **Between requests**: Redis ensures application-level consistency
- **On save**: All cache levels are updated atomically

#### **3. Performance**

- **Reduced DB queries**: Data is loaded only once
- **Fast memory access**: In-memory Identity Map is faster than Redis
- **Optimal resource usage**: No object duplication

### 🎯 Usage Recommendations

#### **When to Use Identity Map:**

1. **Frequent requests for same data**
2. **Complex business operations**: When multiple Use Cases work with the same entities
3. **Consistency requirements**: When it's important that all parts of the application see the same data
4. **High DB load**: When you need to minimize database queries

#### **When to Be Careful:**

1. **Large data volumes**: Identity Map consumes memory, need to monitor size
2. **Long operations**: During long operations, data in Identity Map may become stale
3. **Distributed systems**: In microservice architecture, need to consider consistency between services

#### **Best Practices:**

1. **Limit lifetime**: Use request-scoped Identity Map for automatic cleanup
2. **Add monitoring**: Track hit rate and memory usage
3. **Combine with other patterns**: Use with Unit of Work and Repository
4. **Test thoroughly**: Ensure the pattern works correctly in all scenarios

---

## 🚀 Potential Architecture Improvements

### 🔄 Unit of Work

**What is it?**
**Unit of Work (UoW)** is a design pattern that tracks a list of business objects changed during a transaction and coordinates writing changes and solving concurrency problems. Essentially, it's a "to-do list" for the database that ensures all operations within a single business transaction are executed as a single unit.

**How it could be implemented in the project:**

1.  **`UnitOfWorkProtocol` Interface**:
    - Defined in `src/application/interfaces/uow.py`.
    - Would contain methods for managing repositories and transactions:
        ```python
        from typing import Protocol

        class UnitOfWorkProtocol(Protocol):
            artifacts: ArtifactRepositoryProtocol

            async def __aenter__(self): ...

            async def __aexit__(self, exc_type, exc_val, exc_tb): ...

            async def commit(self): ...

            async def rollback(self): ...
        ```

2.  **`SqlAlchemyUnitOfWork` Implementation**:
    - Would be located in `src/infrastructures/db/uow.py`.
    - Would manage SQLAlchemy session and provide access to repositories:
        ```python

        @dataclass(frozen=True, slots=True, kw_only=True)
        class SqlAlchemyUnitOfWork(UnitOfWorkProtocol):
            session: AsyncSession
            artifact_repository: ArtifactRepositorySQLAlchemy

            async def __aenter__(self):
                self.artifacts = self.artifact_repository
                return self

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                if exc_type is None:
                    await self.commit()
                else:
                    await self.rollback()
                await self.session.close()

            async def commit(self):
                await self.session.commit()

            async def rollback(self):
                await self.session.rollback()
        ```

3.  **Usage in Use Cases**:
    - Use cases would receive `UnitOfWorkProtocol` via DI and use it as a context manager:
        ```python
        # src/application/use_cases/create_artifact.py
        @dataclass(frozen=True, slots=True, kw_only=True)
        class CreateArtifact:
            uow: UnitOfWorkProtocol

            async def execute(self, data: CreateArtifactDTO) -> ArtifactEntity:
                # Logic for creating Artifact entity from DTO
                new_artifact = Artifact(...)
                async with self.uow:
                    self.uow.artifacts.add(new_artifact)
                    # Can perform operations with other repositories in the same transaction
                    # self.uow.another_repo.do_something()
                    await self.uow.commit() # Explicit commit (or implicit on async with exit)
                return new_artifact
        ```

**Benefits of UoW Implementation:**
- **Atomicity**: Ensures that multiple database operations (e.g., updating an artifact and logging this action) are executed in a single transaction.
- **Consistency**: Prevents saving partially changed data.
- **Logic Simplification**: Use case doesn't need to manually manage sessions and transactions, it just works with repositories within UoW.

### 🧩 Aggregates

**What is it?**
**Aggregate** is a pattern from Domain-Driven Design (DDD) representing a cluster of related entity objects and value objects that are treated as a single unit. Each aggregate has a root (Aggregate Root) — an entity that is the single entry point for accessing any object inside the aggregate. The aggregate root is responsible for ensuring the integrity and invariants of the entire aggregate.

**How it could be implemented in the project:**

1.  **Aggregate Definition**:
    - Suppose we have an `Artifact` entity and a related `RestorationRecord` entity. `Artifact` could be the aggregate root, and `RestorationRecord` could be part of this aggregate.
    - `Artifact` (root) would manage the lifecycle of `RestorationRecord`.

2.  **Aggregate Structure in Code**:
    - **Aggregate Root (`Artifact`)**:
        ```python
        # src/domain/entities/artifact.py
        from dataclasses import dataclass, field
        from typing import List
        from .restoration_record import RestorationRecord # Assuming this entity exists

        @dataclass
        class Artifact:
            id: int
            name: str
            # ... other fields
            restoration_history: List[RestorationRecord] = field(default_factory=list)

            def add_restoration_record(self, record: RestorationRecord):
                """Method for adding restoration record with invariant checks."""
                # Example invariant: cannot add a future restoration record
                if record.date > datetime.now():
                    raise ValueError("Restoration date cannot be in the future")
                self.restoration_history.append(record)

            # ... other methods managing aggregate state
        ```
    - **Aggregate Part (`RestorationRecord`)**:
        ```python
        # src/domain/entities/restoration_record.py
        from dataclasses import dataclass
        from datetime import date

        @dataclass
        class RestorationRecord:
            id: int
            artifact_id: int # Foreign key, but accessible through root within aggregate
            description: str
            date: date
            # ... other fields
        ```
    - **Important**: External code should not directly modify `restoration_history` or create `RestorationRecord` without `Artifact` involvement. All operations go through the root.

3.  **Repository for Aggregate**:
    - Repository is created only for the aggregate root (`ArtifactRepository`).
    - It is responsible for loading and saving the entire aggregate as a whole:
        ```python
        # src/infrastructures/db/repositories/artifact.py
        async def get_by_id(self, artifact_id: int) -> Artifact | None:
            # Logic for loading Artifact from DB
            # And subsequent loading of all related RestorationRecord
            # and assembling the aggregate object
            pass
        ```

4.  **Usage in Use Cases**:
    - Use case works with the aggregate through its root:
        ```python
        # src/application/use_cases/add_restoration_record.py
        @dataclass(frozen=True, slots=True, kw_only=True)
        class AddRestorationRecord:
            uow: UnitOfWorkProtocol

            async def execute(self, artifact_id: int, data: AddRestorationRecordDTO):
                async with self.uow:
                    artifact = await self.uow.artifacts.get_by_id(artifact_id)
                    if not artifact:
                        raise ValueError("Artifact not found")

                    new_record = RestorationRecord(
                        id=None, # Will be generated by DB
                        artifact_id=artifact_id,
                        description=data.description,
                        date=data.date
                    )
                    # All logic and validation is encapsulated in the aggregate root
                    artifact.add_restoration_record(new_record)

                    # Repository saves the entire aggregate
                    await self.uow.artifacts.update(artifact)
                    await self.uow.commit()
        ```

**Benefits of Aggregate Implementation:**
- **Business Logic Encapsulation**: Complex rules and invariants related to a group of objects are in one place (in the aggregate root).
- **Data Integrity Guarantee**: Aggregate root ensures that its parts are always in a consistent state.
- **Domain Model Simplification**: Clear aggregate boundaries make the model more understandable and manageable.
- **Transaction Consistency**: Aggregate Root is a natural transaction boundary (often in conjunction with Unit of Work).

---

## 🛠️ Development Commands

### 🧹 Code Quality
```bash
# Code checking (new package structure)
make lint                    # Check code style in src/{{cookiecutter.project_slug}}/
make lint-fix               # Auto-fix issues in src/{{cookiecutter.project_slug}}/
make format                 # Format code in src/{{cookiecutter.project_slug}}/
make type-check             # Type checking in src/{{cookiecutter.project_slug}}/
make check                  # Run all checks on src/{{cookiecutter.project_slug}}/
```

### 🧪 Testing
```bash
# Run tests (new package structure)
make test                   # Basic test run with updated imports
make test-cov               # Run tests with coverage on src/{{cookiecutter.project_slug}}/
make docker-test            # Run in Docker environment
```

### 🗄️ Database Operations
```bash
# Migrations
make migration msg="Description"  # Create migration
make migrate                  # Apply migrations
make migrate-downgrade        # Rollback migration
make migrate-history          # Migration history
```

### 🐳 Docker Commands
```bash
# Container management
make docker-build            # Build production image
make docker-up-dev           # Start development environment
make docker-down             # Stop all services
make docker-logs             # View logs
make docker-shell            # Shell in container
```

---

## 📊 Usage Examples

### 📖 Get Artifact Information
```bash
curl "http://localhost:8001/api/v1/artifacts/{inventory_id}"
```

---

## 🚀 Deployment

### 🏭 Development Deployment

1. **Environment Setup**
```bash
cp .env.template .env
# Configure production parameters
```

2. **Build and Run**
```bash
# Build dev image
make docker-build-dev

# Run in dev mode
make docker-dev
```

---

## 📞 Contacts

If you have questions or suggestions, please:

- 📧 Create an Issue in the repository
- 💬 Discuss in Discussions
- 📧 Contact the developers

---

<div align="center">

**Made with ❤️ for {{ cookiecutter.project_description.lower() }}**

[⬆️ Back to Top](#-{{ cookiecutter.project_slug | replace('_', '-') }})

</div>
