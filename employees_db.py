import mariadb

conn = mariadb.connect(
    user="employees",
    password="employees",
    host="localhost",
    port=3307,
    database="employees"
)

cur = conn.cursor()
cur.execute("SELECT id, emp_name FROM Employee")
for id, name in cur:
    print(f"{id} - {name}")

cur.execute("insert into Employee(emp_name) values (?)", ("oktato oktato",))
conn.commit()