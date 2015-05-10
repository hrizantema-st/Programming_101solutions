DROP TABLE IF EXISTS Students;
CREATE TABLE Students(id INTEGER PRIMARY KEY,
                      name TEXT,
                      github TEXT,
                      available INTEGER,
                      course TEXT,
                      course_group INTEGER);

DROP TABLE IF EXISTS Courses;
CREATE TABLE Courses(id INTEGER PRIMARY KEY,
                     name TEXT);

DROP TABLE IF EXISTS Students_to_courses;
CREATE TABLE Students_to_courses(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(id),
    FOREIGN KEY(course_id) REFERENCES Courses(id) );

