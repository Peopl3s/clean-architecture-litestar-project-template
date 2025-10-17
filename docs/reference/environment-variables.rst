Environment Variables
=====================

Complete reference of environment variables used in generated projects.

Application Variables
---------------------

APP_NAME
~~~~~~~~
* **Type**: String
* **Default**: Project name
* **Description**: Application name

APP_VERSION
~~~~~~~~~~~
* **Type**: String
* **Default**: 0.1.0
* **Description**: Application version

DEBUG
~~~~~
* **Type**: Boolean
* **Default**: false
* **Description**: Enable debug mode

LOG_LEVEL
~~~~~~~~~
* **Type**: String
* **Default**: INFO
* **Options**: DEBUG, INFO, WARNING, ERROR, CRITICAL
* **Description**: Logging level

Server Variables
----------------

HOST
~~~~
* **Type**: String
* **Default**: 0.0.0.0
* **Description**: Server host

PORT
~~~~
* **Type**: Integer
* **Default**: 8000
* **Description**: Server port

WORKERS
~~~~~~~
* **Type**: Integer
* **Default**: 1
* **Description**: Number of worker processes

Database Variables
------------------

DATABASE_URL
~~~~~~~~~~~~
* **Type**: String
* **Required**: Yes
* **Format**: ``driver://user:password@host:port/database``
* **Examples**:

  * PostgreSQL: ``postgresql+asyncpg://user:pass@localhost:5432/db``
  * MySQL: ``mysql+aiomysql://user:pass@localhost:3306/db``
  * SQLite: ``sqlite+aiosqlite:///./database.db``

DB_ECHO
~~~~~~~
* **Type**: Boolean
* **Default**: false
* **Description**: Echo SQL queries to console

DB_POOL_SIZE
~~~~~~~~~~~~
* **Type**: Integer
* **Default**: 5
* **Description**: Connection pool size

Cache Variables
---------------

REDIS_URL
~~~~~~~~~
* **Type**: String
* **Format**: ``redis://host:port/db``
* **Example**: ``redis://localhost:6379/0``

REDIS_PASSWORD
~~~~~~~~~~~~~~
* **Type**: String
* **Description**: Redis password

See Also
--------

* :doc:`../user-guide/configuration` - Configuration guide
* :doc:`../getting-started/template-variables` - Template variables
