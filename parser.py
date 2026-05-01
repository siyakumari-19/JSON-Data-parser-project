import json


with open('data.json', 'r') as file:
    parsed_data = json.load(file)

print(parsed_data)


import sqlite3


connection = sqlite3.connect("company_data.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        role TEXT,
        location TEXT
    )
''')

connection.commit()
for emp in parsed_data:
    emp_id = emp["user_id"]
    emp_name = emp["name"]
    emp_role = emp["role"]
    emp_location = emp["location"]

    cursor.execute("INSERT INTO Employees(user_id,name,role,location)VALUES(?,?,?,?)",(emp_id , emp_name ,emp_role, emp_location))
print("Database and Table has successfully created ")
cursor.execute("SELECT * FROM Employees")
db_data = cursor.fetchall()

for row in db_data:
    print(row)