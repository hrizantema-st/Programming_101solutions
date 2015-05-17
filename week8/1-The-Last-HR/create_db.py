import json
import sqlite3
import requests
from settings import DB_NAME
from settings import SQL_FILE


conn = sqlite3.connect(DB_NAME)
with open(SQL_FILE, "r") as f:
    conn.executescript(f.read())
    conn.commit()

with open("students.json", "r") as f2:
    text = f2.read()
    json_req = json.loads(text)


#req = requests.get('https://hackbulgaria.com/api/students/')
#json_req = req.json()


def insertin_the_info_in_db(connection):
    cursor = connection.cursor()
    courses_list = []
    for each in json_req:

        cursor.execute("""INSERT INTO Students(name, github, available)
            VALUES (?, ?, ?)""", (each["name"], each["github"], each["available"]))
        current_student_id = cursor.lastrowid

        for course in each["courses"]:
            if course["name"] not in courses_list:
                courses_list.append(course["name"])
                cursor.execute(
                    """INSERT INTO Courses(name) VALUES (?)""", (course["name"],))
                current_course_id = cursor.lastrowid
            else:
                cursor.execute(
                    """SELECT id FROM Courses WHERE name=?""", (course["name"],))
                tmp = cursor.fetchone()
                current_course_id = tmp[0]

            cursor.execute("""INSERT INTO Students_to_courses(student_id, course_id) VALUES (?, ?)""", (current_student_id, current_course_id))



insertin_the_info_in_db(conn)
conn.commit()
conn.close()
