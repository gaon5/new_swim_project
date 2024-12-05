import os

class Config:
    # Database Configuration
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASS = os.getenv("DB_PASS", "12345678")
    DB_NAME = os.getenv("DB_NAME", "new_swim")
    SSL_CA_PATH = os.path.join(os.path.dirname(__file__), 'ssl', 'BaltimoreCyberTrustRoot.crt.pem')


import os

# Fetch database connection details from environment variables
dbhost = os.getenv("DB_HOST", "127.0.0.1")  # Default to localhost if not set
dbport = os.getenv("DB_PORT", "3306")       # Default MySQL port
dbuser = os.getenv("DB_USER", "root")       # Default to local MySQL root user
dbpass = os.getenv("DB_PASS", "12345678")   # Default password for local setup
dbname = os.getenv("DB_NAME", "new_swim")   # Default local database name
SSL_CA_PATH = os.path.join(os.path.dirname(__file__), 'ssl', 'BaltimoreCyberTrustRoot.crt.pem')

