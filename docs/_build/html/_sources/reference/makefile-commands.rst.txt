Makefile Commands
=================

The generated project includes a comprehensive Makefile with commands for common development tasks.

Development Commands
--------------------

install
~~~~~~~

Install production dependencies.

.. code-block:: bash

   make install

Uses ``uv sync`` to install all production dependencies defined in ``pyproject.toml``.

install-dev
~~~~~~~~~~~

Install development dependencies.

.. code-block:: bash

   make install-dev

Installs all dependencies including development tools (linting, testing, type checking).

dev-setup
~~~~~~~~~

Complete development environment setup.

.. code-block:: bash

   make dev-setup

Runs ``install-dev`` and displays setup completion message.

Code Quality Commands
---------------------

lint
~~~~

Run linting with ruff.

.. code-block:: bash

   make lint

Checks code for style issues and potential errors without making changes.

lint-fix
~~~~~~~~

Run linting and fix auto-fixable issues.

.. code-block:: bash

   make lint-fix

Automatically fixes issues that ruff can resolve.

format
~~~~~~

Format code with ruff.

.. code-block:: bash

   make format

Applies consistent code formatting across the project.

type-check
~~~~~~~~~~

Run type checking with mypy.

.. code-block:: bash

   make type-check

Validates type hints and catches type-related errors.

check
~~~~~

Run all checks (lint + format check + type check).

.. code-block:: bash

   make check

Comprehensive code quality check. Useful before committing.

Testing Commands
----------------

test
~~~~

Run tests.

.. code-block:: bash

   make test

Runs the full test suite with pytest in verbose mode.

test-cov
~~~~~~~~

Run tests with coverage.

.. code-block:: bash

   make test-cov

Generates HTML and terminal coverage reports.

clean
~~~~~

Clean up cache and temporary files.

.. code-block:: bash

   make clean

Removes ``__pycache__``, ``.pytest_cache``, ``.ruff_cache``, coverage files, etc.

Database Commands
-----------------

migration
~~~~~~~~~

Create a new migration file.

.. code-block:: bash

   make migration msg="Add users table"

Generates an Alembic migration with auto-detected changes.

migrate
~~~~~~~

Apply all pending migrations.

.. code-block:: bash

   make migrate

Upgrades database to the latest schema version.

migrate-downgrade
~~~~~~~~~~~~~~~~~

Downgrade to previous migration.

.. code-block:: bash

   make migrate-downgrade

Rolls back the last applied migration.

migrate-history
~~~~~~~~~~~~~~~

Show migration history.

.. code-block:: bash

   make migrate-history

Displays all migrations and their status.

migrate-current
~~~~~~~~~~~~~~~

Show current migration.

.. code-block:: bash

   make migrate-current

Shows the currently applied migration version.

migrate-stamp
~~~~~~~~~~~~~

Stamp database with current migration.

.. code-block:: bash

   make migrate-stamp

Marks the database as being at a specific migration version without applying changes.

Docker Commands
---------------

docker-build
~~~~~~~~~~~~

Build Docker image for production.

.. code-block:: bash

   make docker-build

Builds the production Docker image.

docker-build-dev
~~~~~~~~~~~~~~~~

Build Docker image for development.

.. code-block:: bash

   make docker-build-dev

Builds the development Docker image with dev dependencies.

docker-build-test
~~~~~~~~~~~~~~~~~

Build Docker image for testing.

.. code-block:: bash

   make docker-build-test

Builds the testing Docker image.

docker-up
~~~~~~~~~

Start all services with docker-compose.

.. code-block:: bash

   make docker-up

Starts all services defined in ``docker-compose.yml`` in detached mode.

docker-up-dev
~~~~~~~~~~~~~

Start development environment.

.. code-block:: bash

   make docker-up-dev

Starts services with the dev profile.

docker-down
~~~~~~~~~~~

Stop all services.

.. code-block:: bash

   make docker-down

Stops and removes all Docker containers.

docker-logs
~~~~~~~~~~~

Show logs for all services.

.. code-block:: bash

   make docker-logs

Follows logs from all running services.

docker-logs-app
~~~~~~~~~~~~~~~

Show logs for application.

.. code-block:: bash

   make docker-logs-app

Follows logs from the application container only.

docker-shell
~~~~~~~~~~~~

Open shell in running app container.

.. code-block:: bash

   make docker-shell

Opens a bash shell inside the running application container.

docker-migrate
~~~~~~~~~~~~~~

Run database migrations in Docker.

.. code-block:: bash

   make docker-migrate

Runs migrations inside a Docker container.

docker-test
~~~~~~~~~~~

Run tests in Docker.

.. code-block:: bash

   make docker-test

Executes the test suite in a Docker container.

docker-clean
~~~~~~~~~~~~

Clean up Docker resources.

.. code-block:: bash

   make docker-clean

Removes containers, volumes, and orphaned resources.

docker-rebuild
~~~~~~~~~~~~~~

Rebuild and restart services.

.. code-block:: bash

   make docker-rebuild

Performs a clean rebuild of all Docker services.

Environment Commands
--------------------

setup-env
~~~~~~~~~

Create .env file from template.

.. code-block:: bash

   make setup-env

Runs the environment setup script to create ``.env`` from ``env.template``.

dev-setup-docker
~~~~~~~~~~~~~~~~

Set up development environment with Docker.

.. code-block:: bash

   make dev-setup-docker

Complete Docker-based development setup including database and services.

CI/CD Commands
--------------

ci
~~

Run CI pipeline (lint + type check + test).

.. code-block:: bash

   make ci

Runs all quality checks and tests. Suitable for CI/CD pipelines.

Message Broker Commands (Kafka)
--------------------------------

docker-kafka-logs
~~~~~~~~~~~~~~~~~

Show Kafka logs.

.. code-block:: bash

   make docker-kafka-logs

docker-kafka-shell
~~~~~~~~~~~~~~~~~~

Open shell in Kafka container.

.. code-block:: bash

   make docker-kafka-shell

docker-kafka-topics
~~~~~~~~~~~~~~~~~~~

List Kafka topics.

.. code-block:: bash

   make docker-kafka-topics

docker-kafka-create-topic
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create Kafka topic.

.. code-block:: bash

   make docker-kafka-create-topic

docker-kafka-consume
~~~~~~~~~~~~~~~~~~~~

Consume messages from Kafka topic.

.. code-block:: bash

   make docker-kafka-consume

Common Workflows
----------------

Starting Development
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   make install-dev
   make setup-env
   # Edit .env file
   make docker-up
   make migrate

Before Committing
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   make format
   make check
   make test

Deploying
~~~~~~~~~

.. code-block:: bash

   make docker-build
   make docker-up
   make docker-migrate

Troubleshooting
~~~~~~~~~~~~~~~

.. code-block:: bash

   make docker-logs        # Check logs
   make docker-shell       # Debug inside container
   make docker-clean       # Clean up
   make docker-rebuild     # Fresh start

Help
----

help
~~~~

Show available commands.

.. code-block:: bash

   make help

Displays all available Makefile commands with descriptions.

See Also
--------

* :doc:`../user-guide/configuration` - Environment configuration
* :doc:`../development/docker` - Docker guide
* :doc:`../development/migrations` - Database migrations
