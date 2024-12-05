import os

# Fetch database connection details from environment variables
dbhost = os.getenv("DB_HOST", "127.0.0.1")  # Default to localhost if not set
dbport = os.getenv("DB_PORT", "3306")       # Default MySQL port
dbuser = os.getenv("DB_USER", "root")       # Default to local MySQL root user
dbpass = os.getenv("DB_PASS", "12345678")   # Default password for local setup
dbname = os.getenv("DB_NAME", "new_swim")   # Default local database name
