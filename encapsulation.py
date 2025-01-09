class Person:
    def __init__(self, name, age, gender):
        self.__name = name # .__ denotes private attribute
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    # Python doesn't implement method overloading,
    # meaning we can't have a class method with the same name and different parameters.

    @Name.setter
    def Name(self, value):
        if value == "Mike":
            self.__name = f"{value} has already been taken."
        else:
            self.__name = value

    # Static method is not related to a specific class/object

    @staticmethod
    def mymethod():
        print("Hello World!")

p1 = Person('John', 25, 'male')
print(p1.Name)
p1.Name = "Mike"
print(p1.Name)

# Accessing mymethod() function directly from the class
Person.mymethod()
p1.mymethod()
