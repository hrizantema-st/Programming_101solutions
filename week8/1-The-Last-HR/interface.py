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
        info = cursor.execute("""SELECT name, github
                                 FROM Students""")
        info_to_print = info.fetchall()
        for each in info_to_print:
            print(each)
    elif command == "list_all_courses":
        info = cursor.execute("""SELECT * FROM Courses""")
        info_to_print = info.fetchall()
        for each in info_to_print:
            print(each)
    elif command == "list_all_students_with_courses":
        info = cursor.execute("""SELECT a.name, b.name
                                 FROM  Students AS a
                                 JOIN Students_to_courses AS c ON c.student_id=a.id
                                 JOIN Courses AS b ON b.id=c.course_id""")
        info_to_print = info.fetchall()
        for each in info_to_print:
            print(each)
    elif command == "list_the_best_students":
        info = cursor.execute("""SELECT name, COUNT(name)
                                 FROM Students
                                 GROUP BY name
                                 ORDER BY COUNT(name)
                                 DESC LIMIT 5;""")
        info_to_print = info.fetchall()
        for each in info_to_print:
            print(each)
    else:
        print("Invalid input!")
