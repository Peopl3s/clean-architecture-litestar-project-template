-- MySQL initialization script for {{ cookiecutter.project_name }}
-- This script is executed when the MySQL container is first created

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `{{ cookiecutter.database_name }}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user if it doesn't exist and grant privileges
CREATE USER IF NOT EXISTS '{{ cookiecutter.database_user }}'@'%' IDENTIFIED BY '{{ cookiecutter.database_password }}';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON `{{ cookiecutter.database_name }}`.* TO '{{ cookiecutter.database_user }}'@'%';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Switch to the created database
USE `{{ cookiecutter.database_name }}`;

-- Create initial tables (if needed)
-- This is where you can add any initial table creation
-- Note: Alembic migrations will handle the actual schema creation

-- Show current database and user
SELECT DATABASE() as current_database;
SELECT CURRENT_USER() as current_user;
