#!/bin/bash

# Set environment variables (modify accordingly)
export FLASK_APP=app
export FLASK_ENV=production

# Create migrations directory (if it doesn't exist)
if [ ! -d "migrations" ]; then
  flask db init
fi

# Generate a new migration
flask db migrate -m "Your migration message"

# Apply the migration to the database
flask db upgrade
