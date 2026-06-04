from db_config import get_connection

def insert_student(name, course):
    connection = get_connection()
    if not connection:
        return

    cursor = None
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO students (name, course) VALUES (%s, %s);"
        cursor.execute(insert_query, (name, course))
        connection.commit()
        print("Data insertion successful")
    except Exception as e:
        print(f"Error during data insertion: {e}")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def display_students():
    connection = get_connection()
    if not connection:
        return

    cursor = None
    try:
        cursor = connection.cursor()
        select_query = "SELECT id, name, course FROM students;"
        cursor.execute(select_query)
        records = cursor.fetchall()
        
        print("SELECT OUTPUT")
        for row in records:
            print(f"ID: {row} | Name: {row} | Course: {row}")
            
    except Exception as e:
        print(f"Error retrieving data: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    print("RUNNING TASK 2 OPERATIONS")
    insert_student("Alex Mercer", "Data Science")
    insert_student("Python", "Web Development")
    display_students()
