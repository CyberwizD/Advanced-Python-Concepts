# Lambda parameter: expression

from functools import reduce


def func(x, y):
    return x + y


print(func(2, 3))

_2Dpoints = [(1, 6), (3, 5), (5, 4)]
sorted_2Dpoints = sorted(_2Dpoints, key=lambda x: x[1])

print(sorted_2Dpoints)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
c = filter(lambda y: y % 2 == 0, a)
d = [x for x in a if x % 2 == 0]
e = reduce(lambda x, y: x * y, a)

print(list(b))
print(list(c))
print(list(d))
print(e)
