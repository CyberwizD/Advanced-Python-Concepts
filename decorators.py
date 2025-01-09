# Decorators adds functionality to a function

def mydecorator(func):
    def wrapper(*args, **kwargs: object):
        return_value = func(*args, **kwargs)
        print("Adding a decorator to your function...")
        return return_value

    return wrapper

@mydecorator
def hello_world(person):
    print(f"Hello {person}")
    return f"Hello {person}!"

# mydecorator(hello_world)() # Not a standard way of using a decorator

print(hello_world("John"))


# Practical Example #1 - Logging

def logged(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open('logfile.txt', 'a+') as file:
            fname = func.__name__
            file.write(f"{fname} function returned a value - {value}\n")
            print(f"{fname} function returned a value - {value}\n")

        return value
    return wrapper

@logged
def add(x, y):
    return x + y

@logged
def multiply(x, y):
    return x * y

@logged
def divide(x, y):
    return x / y

add(10, 20)
multiply(10, 20)
divide(10, 20)


# Practical Example #2 - Timing

import time

def timer(func):
    def wrapper(*args, **kwargs):
        time_before = time.time()
        value = func(*args, **kwargs)
        time_after = time.time()
        fname = func.__name__
        print(f"{fname} function execution time - {time_after - time_before}")

        return value
    return wrapper

@timer
def number_count():
    sum = 0
    for i in range(10000000):
        sum += i

    return sum

number_count()
