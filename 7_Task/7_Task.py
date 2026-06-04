import psycopg2

def getConnection():
    try:
        return psycopg2.connect(
            dbname="testdb", user="postgres", password="4324", host="localhost"
        )
    except Exception as e:
        print("Connection error:", e)

def table(conn):
    try:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS students(id SERIAL PRIMARY KEY, name TEXT, age INT);")
        cur.execute("INSERT INTO students(name, age) VALUES (%s,%s)", ("Aman", 20))
        cur.execute("SELECT * FROM students;")
        print(cur.fetchall())
        conn.commit()
    except Exception as e:
        print("DB error:", e)

conn = getConnection()
if conn:
    table(conn)
    conn.close()
