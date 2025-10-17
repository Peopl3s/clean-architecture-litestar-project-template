Quick Start
===========

Get up and running with the Clean Architecture Litestar template in minutes.

Create Your First Project
--------------------------

1. **Install Cookiecutter**

.. code-block:: bash

   pip install cookiecutter

2. **Generate Project**

.. code-block:: bash

   cookiecutter https://github.com/Peopl3s/clean-architecture-litestar-project-template.git

3. **Configure Your Project**

Answer the prompts with your project details. For a quick start, you can accept most defaults:

.. code-block:: text

   project_name [My Litestar Project]: Todo API
   project_slug [todo_api]:
   project_description: A simple todo list API
   author_name: Your Name
   use_database [postgresql]: postgresql
   use_cache [redis]: redis
   use_broker [none]: none

4. **Navigate to Project**

.. code-block:: bash

   cd todo_api

Project Structure Overview
---------------------------

Your generated project will have this structure:

.. code-block:: text

   todo_api/
   ├── src/
   │   └── todo_api/
   │       ├── domain/              # Business entities
   │       ├── application/         # Use cases
   │       ├── infrastructure/      # External services
   │       │   └── db/              # Database components
   │       │       └── migrations/  # Database migrations
   │       ├── presentation/        # API endpoints
   │       └── config/             # Configuration
   ├── tests/                      # Test suite
   ├── alembic.ini                 # Alembic configuration
   ├── docker-compose.yml          # Docker services
   ├── Dockerfile                  # Application container
   ├── pyproject.toml             # Dependencies
   ├── Makefile                   # Common commands
   └── README.md                  # Project documentation

Running the Application
-----------------------

Using Docker (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Start all services
   make docker-up

   # View logs
   make docker-logs

   # Stop services
   make docker-down

The API will be available at:

* **API**: http://localhost:8000
* **API Docs**: http://localhost:8000/docs
* **ReDoc**: http://localhost:8000/redoc

Local Development
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Install dependencies
   make install-dev

   # Set up environment
   cp env.template .env
   # Edit .env with your database credentials

   # Run migrations
   make migrate

   # Start the application
   poetry run python -m todo_api.main

Exploring the API
-----------------

Health Check
~~~~~~~~~~~~

.. code-block:: bash

   curl http://localhost:8000/health

Response:

.. code-block:: json

   {
     "status": "healthy",
     "version": "0.1.0"
   }

Interactive Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

Open your browser and navigate to:

* **Swagger UI**: http://localhost:8000/docs
* **ReDoc**: http://localhost:8000/redoc

These provide interactive API documentation where you can test endpoints directly.

Development Workflow
--------------------

Running Tests
~~~~~~~~~~~~~

.. code-block:: bash

   # Run all tests
   make test

   # Run with coverage
   make test-cov

Code Quality
~~~~~~~~~~~~

.. code-block:: bash

   # Lint code
   make lint

   # Format code
   make format

   # Type check
   make type-check

   # Run all checks
   make check

Database Migrations
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Create a new migration
   make migration msg="Add users table"

   # Apply migrations
   make migrate

   # View migration history
   make migrate-history

Common Commands
---------------

.. code-block:: bash

   # Development
   make install-dev          # Install dependencies
   make dev-setup           # Complete dev setup

   # Code Quality
   make lint                # Run linting
   make format              # Format code
   make type-check          # Type checking
   make check               # All checks

   # Testing
   make test                # Run tests
   make test-cov            # Tests with coverage

   # Database
   make migration           # Create migration
   make migrate             # Apply migrations
   make migrate-downgrade   # Rollback migration

   # Docker
   make docker-up           # Start services
   make docker-down         # Stop services
   make docker-logs         # View logs
   make docker-shell        # Shell into container

Next Steps
----------

* Learn about :doc:`../user-guide/architecture`
* Explore :doc:`../user-guide/project-structure`
* Read about :doc:`../user-guide/configuration`
* Check out :doc:`../development/code-quality`
