# Errors and Exceptions

# raise Exception
a = -1

if a < 0:
    raise Exception("Value should be greater than zero.")


# Assert Statement
x = -2
assert (x >= 0), 'Value is not positive!'


# Try
try:
    a = 5 / 0
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Error not found!")
finally:
    print("Task Completed!")


# Defined Exceptions
class HighValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


class LowValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise HighValueError('High Value!', x)
    if x < 5:
        raise LowValueError('Low Value!', x)


try:
    test_value(101)
except HighValueError as e:
    print(e.message, e.value)
except LowValueError as e:
    print(e.message, e.value)
