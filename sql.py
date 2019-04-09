import os
import sqlite3

with sqlite3.connect('example.db') as conn:
    print('db created')
    cur = conn.cursor()
    cur.execute('''
            create table department (
                department_id INTEGER PRIMARY KEY,
                department_name TEXT
            )''')
    cur.execute('''
            create table employee (
                employee_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                gender TEXT,
                position TEXT,
                department_id INTEGER,
                salary NUMERIC,
                FOREIGN KEY(department_id) REFERENCES department(department_id)
            )''')
    print('tables created')
    cur.execute('''
            insert into department (department_name)
            values ("IT"), ("Sales")
            ''')
    cur.execute('''
            insert into employee (first_name, last_name, gender,
            position, department_id, salary)
            values ("Super", "Man", "M", "Tester", 1, 75000)
            ''')
    for row in cur.execute('select * from department'):
        print(row)
    for row in cur.execute('select * from employee'):
        print(row)
    cur.execute('drop table employee')
    cur.execute('drop table department')
    print('tables dropped')

os.remove('example.db')
print('removed db')
