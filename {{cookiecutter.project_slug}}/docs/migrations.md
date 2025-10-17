# Database migrations

This project uses Alembic to manage PostgreSQL database migrations.

## Migration commands

### Creating a new migration
```bash
# Create a migration with autogeneration (requires DB connection)
make migration msg="Description of changes"

# Or directly with alembic
poetry run alembic revision --autogenerate -m "Description of changes"
```

### Applying migrations
```bash
# Apply all pending migrations
make migrate

# Or directly
poetry run alembic upgrade head
```

### Rolling back migrations
```bash
# Roll back one migration
make migrate-downgrade

# Or directly
poetry run alembic downgrade -1
```

### Viewing migration history
```bash
# Show migration history
make migrate-history

# Show the current migration
make migrate-current
```

### Other useful commands
```bash
# Mark the DB as being at a specific migration (without applying it)
make migrate-stamp

# Show SQL for a migration (without applying it)
poetry run alembic upgrade head --sql
```

## File structure

- `alembic.ini` - Alembic configuration
- `src/{{cookiecutter.project_slug}}/infrastructures/db/migrations/env.py` - migration environment settings
- `src/{{cookiecutter.project_slug}}/infrastructures/db/migrations/versions/` - directory with migration files
- `src/{{cookiecutter.project_slug}}/infrastructures/db/migrations/script.py.mako` - template for new migrations
