#!/usr/bin/env python3
"""
Post-generation hook for cookiecutter template.
This script automatically generates a .env file based on the cookiecutter context.
"""

import os
import sys
from pathlib import Path


def generate_env_file(context):
    """Generate .env file based on cookiecutter context."""

    project_dir = Path(os.getcwd())
    env_file = project_dir / ".env"

    # Extract variables from context
    project_name = context.get("project_name", "").replace(" ", "_").lower()
    project_description = context.get("project_description", "")
    author_name = context.get("author_name", "")
    author_email = context.get("author_email", "")
    github_username = context.get("github_username", "")
    domain_name = context.get("domain_name", "")
    use_broker = context.get("use_broker", "")
    use_cache = context.get("use_cache", "")
    use_database = context.get("use_database", "")
    add_docker = context.get("add_docker", "n")

    # Generate database URL based on selected database
    if use_database == "postgresql":
        database_url = f"postgresql://antiques_user:antiques_password@localhost:5432/{project_name}"
    elif use_database == "mysql":
        database_url = f"mysql+pymysql://antiques_user:antiques_password@localhost:3306/{project_name}"
    elif use_database == "sqlite":
        database_url = f"sqlite:///./{project_name}.db"
    else:
        database_url = ""

    # Generate cache URL based on selected cache
    if use_cache == "redis":
        cache_url = "redis://localhost:6379/0"
    elif use_cache == "keydb":
        cache_url = "redis://localhost:6379/0"
    elif use_cache == "tarantool":
        cache_url = "tarantool://localhost:3301"
    elif use_cache == "dragonfly":
        cache_url = "redis://localhost:6379/0"
    else:
        cache_url = ""

    # Generate broker URL based on selected broker
    if use_broker == "rabbitmq":
        broker_url = "amqp://guest:guest@localhost:5672/"
    elif use_broker == "kafka":
        broker_url = "kafka://localhost:9092"
    elif use_broker == "nats":
        broker_url = "nats://localhost:4222"
    else:
        broker_url = ""

    # Generate .env content
    env_content = f"""# Environment variables for {project_name}
# Generated automatically by cookiecutter post-gen hook

# Application Settings
ENVIRONMENT=development
LOG_LEVEL=INFO
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=1
DEBUG=true

# Database Configuration
DATABASE_URL="{database_url}"

# Cache Configuration
"""

    if cache_url:
        env_content += f'{use_cache.upper()}_URL="{cache_url}"\n'

    # Message Broker Configuration
    if broker_url:
        env_content += f'\n# Message Broker Configuration\nBROKER_URL="{broker_url}"\n'

    # Security
    env_content += f"""
# Security
SECRET_KEY="your-secret-key-change-this-in-production"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS Settings
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8080"]

# Project Info
PROJECT_NAME="{project_name}"
PROJECT_DESCRIPTION="{project_description}"
PROJECT_VERSION="0.1.0"
AUTHOR_NAME="{author_name}"
AUTHOR_EMAIL="{author_email}"
GITHUB_USERNAME="{github_username}"
DOMAIN_NAME="{domain_name}"

# Docker Settings (if enabled)
"""

    if add_docker == "y":
        env_content += """# Docker-specific settings
DOCKER_HOST=unix:///var/run/docker.sock
"""

    # Additional settings
    env_content += """
# Optional Features
ENABLE_DOCS=true
ENABLE_METRICS=false
ENABLE_TRACING=false

# Email Configuration (optional)
SMTP_HOST=""
SMTP_PORT=587
SMTP_USER=""
SMTP_PASSWORD=""
SMTP_FROM=""

# External API Keys (optional)
EXTERNAL_API_KEY=""

# Monitoring
SENTRY_DSN=""
"""

    # Write the .env file
    try:
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(env_content.strip())
        print(f"✅ Generated .env file at {env_file}")
        return True
    except Exception as e:
        print(f"❌ Failed to generate .env file: {e}")
        return False


def main():
    """Main function to run the post-generation hook."""

    # Cookiecutter doesn't automatically pass context to post-gen hooks
    # We need to read the context from the cookiecutter.json file in the template
    # or extract it from the generated project's configuration

    try:
        import json
        print("🔧 Running post-generation hook...")

        # Try to find context in different possible locations
        context = None

        # Method 1: Look for cookiecutter.json in the parent directory (template root)
        possible_context_files = [
            "../cookiecutter.json",  # Template root
            "cookiecutter.json",     # Current directory
            "../.cookiecutter.json", # Hidden file in template root
        ]

        for context_file in possible_context_files:
            try:
                with open(context_file, 'r', encoding='utf-8') as f:
                    template_context = json.load(f)
                    print(f"📄 Found context in: {context_file}")

                    # Extract the actual values from the template defaults
                    # Since we're in post-gen, we need to get the actual values used
                    # We'll use the defaults as fallback and try to get actual values from project
                    context = {
                        "project_name": template_context.get("project_name", "my_awesome_api"),
                        "project_description": template_context.get("project_description", "An awesome API for my project"),
                        "author_name": template_context.get("author_name", "John Doe"),
                        "author_email": template_context.get("author_email", "john@example.com"),
                        "github_username": template_context.get("github_username", "johndoe"),
                        "domain_name": template_context.get("domain_name", "awesomeapi.com"),
                        "use_broker": template_context.get("use_broker", "rabbitmq"),
                        "use_cache": template_context.get("use_cache", "tarantool"),
                        "use_database": template_context.get("use_database", "mysql"),
                        "add_docker": template_context.get("add_docker", "y"),
                        "add_tests": template_context.get("add_tests", "y"),
                        "add_docs": template_context.get("add_docs", "y"),
                        "add_precommit": template_context.get("add_precommit", "y"),
                        "license_type": template_context.get("license_type", "MIT")
                    }
                    break
            except FileNotFoundError:
                continue

        if not context:
            print("❌ Could not find cookiecutter context file")
            # Use default context as fallback
            context = {
                "project_name": "my_awesome_api",
                "project_description": "An awesome API for my project",
                "author_name": "John Doe",
                "author_email": "john@example.com",
                "github_username": "johndoe",
                "domain_name": "awesomeapi.com",
                "use_broker": "rabbitmq",
                "use_cache": "tarantool",
                "use_database": "mysql",
                "add_docker": "y",
                "add_tests": "y",
                "add_docs": "y",
                "add_precommit": "y",
                "license_type": "MIT"
            }
            print("📄 Using default context")

        # Try to extract actual project name from current directory
        current_dir = Path(os.getcwd()).name
        if current_dir and current_dir != ".":
            context["project_name"] = current_dir
            context["project_slug"] = current_dir
            print(f"📁 Detected project name from directory: {current_dir}")

        # Generate .env file
        success = generate_env_file(context)

        if success:
            print("✅ Post-generation hook completed successfully!")
            sys.exit(0)
        else:
            print("❌ Post-generation hook failed!")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Unexpected error in post-generation hook: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
