# The Factory Method design pattern offers a systematic way to create objects
# while keeping code maintainable and adaptable.

from abc import ABCMeta, abstractmethod  # abc - abstract class


# Instance of this class cannot be created without an implementation for abstract method
class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """ Interface Method """


class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Info"

    def person_method(self):
        print("I'm a Student.")


class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Info"

    def person_method(self):
        print("I'm a Teacher.")


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
            return Teacher()
        else:
            print("Invalid Type!")


if __name__ == "__main__":
    choice = input("Are you a Student or a Teacher? ")

    person = PersonFactory.build_person(choice)
    print(person.person_method())
