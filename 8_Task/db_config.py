import psycopg2

DB_SETTINGS = {
    "dbname": "testdb",
    "user": "postgres",
    "password": "4324",  
    "port": "5432"
}

def get_connection():
    """Establishes and returns a database connection with robust error handling."""
    try:
        connection = psycopg2.connect(**DB_SETTINGS)
        return connection
    except Exception as e:
        print(f"Database Connection Failed: {e}")
        return None
