import sqlite3

drop_table_if_exist = """
DROP TABLE IF EXISTS company
"""
create_table_query = """
CREATE TABLE company(id INTEGER PRIMARY KEY, name TEXT,
                   monthly_salary INTEGER,  yearly_bonus INTEGER, position TEXT)
"""

conn = sqlite3.connect("company")
cursor = conn.cursor()
cursor.execute(drop_table_if_exist)
cursor.execute(create_table_query)

emp1 = ("Ivan Ivanov", 5000, 10000, "Software Developer")
emp2 = ("Rado Rado", 500, 0, "Technical Support Intern")
emp3 = ("Ivo Ivo", 10000, 100000, "CEO")
emp4 = ("Petar Petrov", 3000, 1000, "Marketing Manager")
emp5 = ("Maria Georgieva", 8000, 10000, "COO")


employees = [emp1, emp2, emp3, emp4, emp5]

insert_initial_info = """
INSERT INTO company(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)"""


cursor.executemany(insert_initial_info, employees)
conn.commit()
conn.close()
