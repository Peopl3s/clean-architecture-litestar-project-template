Clean Architecture FastAPI Project Template
===========================================

A comprehensive cookiecutter template for creating modern FastAPI applications with clean architecture, Docker support, and best practices included.

.. image:: https://img.shields.io/badge/python-3.12+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python Version

.. image:: https://img.shields.io/badge/FastAPI-0.117+-green.svg
   :target: https://fastapi.tiangolo.com
   :alt: FastAPI

.. image:: https://img.shields.io/badge/code%20style-ruff-000000.svg
   :target: https://github.com/astral-sh/ruff
   :alt: Code Style

Overview
--------

This cookiecutter template provides a production-ready foundation for building FastAPI applications following Clean Architecture principles. It includes everything you need to start developing a scalable, maintainable web application.

**Key Features:**

* 🏗️ **Clean Architecture** - Domain-Driven Design with clear separation of concerns
* ⚡ **FastAPI** - High-performance async web framework
* 🗄️ **Multiple Database Support** - PostgreSQL, MySQL, or SQLite
* 🔄 **Message Brokers** - Kafka, RabbitMQ, or NATS integration
* 💾 **Caching** - Redis, KeyDB, Tarantool, or Dragonfly support
* 🐳 **Docker** - Complete containerization with Docker Compose
* 🧪 **Testing** - Comprehensive test suite with pytest
* 📝 **Code Quality** - Ruff linting, MyPy type checking, pre-commit hooks
* 🔄 **Migrations** - Alembic for database schema management

Quick Start
-----------

Install cookiecutter and create a new project:

.. code-block:: bash

   pip install cookiecutter
   cookiecutter https://github.com/Peopl3s/clean-architecture-fastapi-project-template.git

Follow the prompts to configure your project, then:

.. code-block:: bash

   cd your-project-name
   make install-dev
   make docker-up

Your API will be available at http://localhost:8000 with interactive documentation at http://localhost:8000/docs

Documentation Contents
----------------------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   getting-started/installation
   getting-started/quickstart
   getting-started/template-variables

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user-guide/project-structure
   user-guide/architecture
   user-guide/configuration
   user-guide/database
   user-guide/caching
   user-guide/message-brokers
   user-guide/testing
   user-guide/deployment

.. toctree::
   :maxdepth: 2
   :caption: Development

   development/code-quality
   development/docker
   development/migrations
   development/contributing

.. toctree::
   :maxdepth: 2
   :caption: Advanced Topics

   advanced/customization
   advanced/hooks
   advanced/ci-cd
   advanced/best-practices

.. toctree::
   :maxdepth: 1
   :caption: Reference

   reference/makefile-commands
   reference/environment-variables
   reference/faq
   changelog
   license

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
