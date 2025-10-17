#!/bin/bash

# Always recreate .env from template
echo "Creating .env file from template..."
cp env.template .env
echo "✅ .env file created successfully!"
echo "📝 Please review and modify .env file if needed"
