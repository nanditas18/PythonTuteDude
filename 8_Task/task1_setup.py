from db_config import get_connection

def create_table():
    connection = get_connection()
    if not connection:
        print("Task 1 Aborted: Could not establish a database connection.")
        return

    print("Connection success: Securely connected to PostgreSQL server.")
    cursor = None
    
    try:
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            course VARCHAR(100) NOT NULL
        );
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        print("Table creation confirmation: students table verified or created successfully.")
        
    except Exception as e:
        print(f"Error during table creation: {e}")
        if connection:
            connection.rollback()
            print("Transaction safely rolled back due to error.")
            
    finally:
        if cursor:
            cursor.close()
            print("Cursor closed successfully.")
        if connection:
            connection.close()
            print("Database connection securely closed.")

if __name__ == "__main__":
    print("RUNNING TASK 1: SETUP")
    create_table()
