# Python is not statically typed, which means the variable types are not known until run-time
# mypy is a static type checker for Python

def func(param: int) -> str:
    if type(param) is bool:
        pass
    else:
        print("Compiling at run-time...")

    return f"{param + 10}"

def a_func(a_param: str):
    print(a_param)

def b_func(b_param: list[int]):
    if type(b_param) is not list:
        print("Expecting a list of integers!")
    else:
        print(b_param)

b_func(a_func(func(10)))
