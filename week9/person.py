from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship


Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    person_name = Column(String)
    person_age = Column(Integer)

    def __str__(self):
        return " {} - {} ".format(self.id, self.person_name)

    def __repr__(self):
        return self.__str__()


engine = create_engine("sqlite:///people.db")

Base.metadata.create_all(engine)

session = Session(bind=engine)

session.add_all([Person(person_name="Rado", person_age=23),
                 Person(person_name="Ivo", person_age=21),
                 Person(person_name="Ivan", person_age=23)])
"""
all_people = session.query(Person).all()
print(all_people)


print("\n")

rado = session.query(Person).filter(Person.person_name == "Rado").all()
print(rado)


twenty_three = session.query(Person.person_name, Person.person_age).filter(Person.person_age == 23).all()

for t in twenty_three:
    print(t)

print(twenty_three)

rado2 = session.query(Person.person_name, Person.id).filter(Person.person_name == "Rado").all()

for r in rado2:
    print(r)
"""

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("people.id"))
    student = relationship("Person", backref="grades")
