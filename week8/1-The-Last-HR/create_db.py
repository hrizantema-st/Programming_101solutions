import json
import sqlite3
import requests
from settings import DB_NAME
from settings import SQL_FILE

conn = sqlite3.connect(DB_NAME)
with open(SQL_FILE, "r") as f:
    conn.executescript(f.read())
    conn.commit()

req = requests.get('https://hackbulgaria.com/api/students/')
json_req = json.loads(req.text)

def insertin_the_info_in_db(connection):
    cursor = connection.cursor()
    courses_list = []
    for each in json_req:

        for course in each["courses"]:
            if course["name"] not in courses_list:
                cursor.execute("""INSERT INTO Courses(name) VALUES (?)""", (course["name"],))
                courses_list.append(course["name"])

        cursor.execute("""INSERT INTO Students(name, github, available, course, course_group)
            VALUES (?, ?, ?, ?, ?)""", (each["name"], each["github"], each["available"], course["name"], course["group"]))


'''
        cursor.execute("""SELECT student_id FROM students WHERE """)
       cursor.execute("""INSERT INTO students_to_courses(student_id, course_id, group) VALUES (?, ?, ?)""",
'''

insertin_the_info_in_db(conn)
conn.commit()
conn.close()
