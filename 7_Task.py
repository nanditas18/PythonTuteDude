import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="name",
    user="postgres",
    password="4324"
    )

cur = conn.cursor()

cur.execute("SELECT * FROM stud")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()

cur.close()
conn.close() 