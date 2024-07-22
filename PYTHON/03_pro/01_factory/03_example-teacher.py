from abc import ABC, abstractstaticmethod

class IPerson(ABC):

    @abstractstaticmethod
    def person_method():
        """ Interface method """

class Student(IPerson):

    def __init__(self):
        self.name = "Student name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Teacher name"

    def person_method(self):
        print("I am A teacher")



class PersonFactory:

    @staticmethod
    def build_person(person_type: str) -> (Student | Teacher | None):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()


if __name__ == '__main__':
    choice = input(": ")
    person = PersonFactory.build_person(choice)
    person.person_method()
