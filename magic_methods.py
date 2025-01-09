class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # deconstructor
    def __del__(self):
        print("Object has been deconstructed")

p = Person("John", 12)

# Operator Overload

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self, *args, **kwargs):
        return "Vector"

v1 = Vector(10, 20)
v2 = Vector(30, 40)
v3 = v1 + v2
print(v3(), v3)
