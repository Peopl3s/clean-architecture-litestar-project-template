-- Database initialization script for {{ cookiecutter.project_name }} application
-- This script runs when the PostgreSQL container starts for the first time

-- Create the main user
CREATE USER {{ cookiecutter.database_user }} WITH PASSWORD '{{ cookiecutter.database_password }}';

-- Create the database
CREATE DATABASE {{ cookiecutter.database_name }} OWNER {{ cookiecutter.database_user }};

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE {{ cookiecutter.database_name }} TO {{ cookiecutter.database_user }};

-- Connect to the {{ cookiecutter.database_name }} database
\c {{ cookiecutter.database_name }};

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Set timezone
SET timezone = 'UTC';

-- Grant schema privileges
GRANT ALL ON SCHEMA public TO {{ cookiecutter.database_user }};
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {{ cookiecutter.database_user }};
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO {{ cookiecutter.database_user }};
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO {{ cookiecutter.database_user }};
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO {{ cookiecutter.database_user }};
