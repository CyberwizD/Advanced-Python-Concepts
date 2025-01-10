from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def print_data(self):
        """ Implement in child class """


class Person_Singleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if Person_Singleton.__instance is None:
            print("Error: No instance found!")
            print("Creating...")

            Person_Singleton("Default Name", 0)

        return Person_Singleton.__instance

    def __init__(self, name, age):
        if Person_Singleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            Person_Singleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {Person_Singleton.__instance.name}")
        print(f"Age: {Person_Singleton.__instance.age}")


p1 = Person_Singleton("John", 25)
print(p1)
p1.print_data()

p2 = Person_Singleton.get_instance()
print(p2)
p2.print_data()
