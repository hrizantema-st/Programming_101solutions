import sqlite3
from settings import DB_NAME


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

"""
    List all students with their GitHub accounts.
    List all courses,
    List all students and for each student - list the courses he has been attending.
    Find the students that have attented the most courses in Hack Bulgaria.
"""
while True:
    command = input("Enter a command:")
    if command == "list_all_students_and_github":
        cursor.execute("""SELECT name, github FROM Students""")
    elif command == "list_all_courses":
        cursor.execute("""SELECT * FROM Courses""")
    elif command == "list_all_students_with_courses":
        cursor.execute("""SELECT name, course FROM Students""")
    elif command == "list_the_best_students":
        cursor.execute("""SELECT name, COUNT(name) FROM Students GROUP BY name ORDER BY COUNT(name) DESC LIMIT 5;""")
    else:
        print("Invalid input!")
