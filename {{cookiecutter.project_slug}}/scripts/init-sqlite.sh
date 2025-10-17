#!/bin/bash
# SQLite initialization script for {{ cookiecutter.project_name }}
# This script is executed when the SQLite container is first created

set -e

echo "Initializing SQLite database for {{ cookiecutter.project_name }}..."

# Create data directory if it doesn't exist
mkdir -p /data

# Set database path
DB_PATH="/data/{{ cookiecutter.database_name }}.db"

# Create SQLite database file if it doesn't exist
if [ ! -f "$DB_PATH" ]; then
    echo "Creating SQLite database at $DB_PATH"
    touch "$DB_PATH"
    chmod 666 "$DB_PATH"
    
    # Create initial tables using sqlite3 command
    sqlite3 "$DB_PATH" << 'EOF'
-- Enable foreign key support
PRAGMA foreign_keys = ON;

-- Create initial metadata table to track database initialization
CREATE TABLE IF NOT EXISTS database_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT NOT NULL UNIQUE,
    value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert initialization record
INSERT OR IGNORE INTO database_metadata (key, value) VALUES ('initialized', '{{ cookiecutter.project_name }}');
INSERT OR IGNORE INTO database_metadata (key, value) VALUES ('version', '1.0.0');
INSERT OR IGNORE INTO database_metadata (key, value) VALUES ('created_at', datetime('now'));

-- Show database info
SELECT 'Database initialized successfully' as status;
SELECT datetime('now') as initialization_time;
EOF
    
    echo "SQLite database initialized successfully"
else
    echo "SQLite database already exists at $DB_PATH"
fi

# Set proper permissions
chmod 666 "$DB_PATH"

echo "SQLite initialization completed"
