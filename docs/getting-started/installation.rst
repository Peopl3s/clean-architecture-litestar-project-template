Installation
============

This guide will help you install and use the Clean Architecture FastAPI template.

Prerequisites
-------------

Before you begin, ensure you have the following installed:

* **Python 3.12+** - `Download Python <https://www.python.org/downloads/>`_
* **Cookiecutter** - Template rendering tool
* **Git** - Version control system
* **Docker & Docker Compose** (optional) - For containerized development

Installing Cookiecutter
------------------------

Install cookiecutter using pip:

.. code-block:: bash

   pip install cookiecutter

Or using pipx (recommended for global tools):

.. code-block:: bash

   pipx install cookiecutter

Creating a Project
------------------

From GitHub
~~~~~~~~~~~

Create a new project directly from the GitHub repository:

.. code-block:: bash

   cookiecutter https://github.com/Peopl3s/clean-architecture-fastapi-project-template.git

From Local Clone
~~~~~~~~~~~~~~~~

If you want to customize the template or work offline:

.. code-block:: bash

   # Clone the template repository
   git clone https://github.com/Peopl3s/clean-architecture-fastapi-project-template.git
   cd clean-architecture-fastapi-project-template

   # Create a new project from the local template
   cookiecutter .

Interactive Setup
~~~~~~~~~~~~~~~~~

During project creation, you'll be prompted for various configuration options:

.. code-block:: text

   project_name [My FastAPI Project]: My Awesome API
   project_slug [my_awesome_api]:
   project_description [A modern FastAPI application]: An awesome API
   author_name [Your Name]: John Doe
   author_email [your.email@example.com]: john@example.com
   github_username [yourusername]: johndoe
   version [0.1.0]:
   python_version [3.12]:
   use_database [postgresql]: postgresql
   use_cache [redis]: redis
   use_broker [kafka]: kafka
   add_docker [y]: y
   add_tests [y]: y
   add_docs [y]: y
   add_precommit [y]: y
   license_type [MIT]: MIT

Non-Interactive Setup
~~~~~~~~~~~~~~~~~~~~~~

For automation or CI/CD, use non-interactive mode:

.. code-block:: bash

   cookiecutter https://github.com/Peopl3s/clean-architecture-fastapi-project-template.git \
     --no-input \
     project_name="My Awesome API" \
     project_description="An awesome API for my project" \
     author_name="John Doe" \
     author_email="john@example.com" \
     github_username="johndoe" \
     use_database="postgresql" \
     use_cache="redis" \
     use_broker="kafka"

Post-Installation
-----------------

After creating your project:

1. Navigate to the project directory:

.. code-block:: bash

   cd your-project-slug

2. Install dependencies:

.. code-block:: bash

   # Using Poetry
   poetry install

   # Or using pip
   pip install -e ".[dev]"

3. Set up environment:

.. code-block:: bash

   cp env.template .env
   # Edit .env with your configuration

4. Start development:

.. code-block:: bash

   # With Docker
   make docker-up

   # Or locally
   make migrate
   poetry run python -m your_project_slug.main

Next Steps
----------

* Read the :doc:`quickstart` guide
* Learn about :doc:`template-variables`
* Explore the :doc:`../user-guide/project-structure`
