# Itertools - product, permutations, combinations, accumulate, groupby, infinite iterators

import itertools as itr
import operator

# Product
a = [1, 2]
b = [3, 4]
product = itr.product(a, b)
print(list(product))


# Permutations
a = [1, 2]
perm = itr.permutations(a)
print(list(perm))


# Combinations
b = [1, 2, 3]
comb = itr.combinations(b, 2)
print(list(comb))


# Accumulate
c = [1, 2, 3, 4, 5]
acc = itr.accumulate(c, func=operator.mul)
print(list(c))
print(list(acc))


# Groupby
d = [1, 2, 3, 4]
group_obj = itr.groupby(a, key=lambda x: x < 3)

for key, value in group_obj:
    print(key, list(value))

persons = [
    {
        'name': 'Tim',
        'age': 23
    },
    {
        'name': 'Dan',
        'age': 13
    },
    {
        'name': 'John',
        'age': 39
    },
    {
        'name': 'Lisa',
        'age': 18
    }
]

group_people = itr.groupby(persons, lambda p: p['name'])

for key, value in group_people:
    print(key, list(value))


# Count
for i in itr.count(10):  # Starts the iteration with 10
    print(i)
    if i == 20:
        break

e = [1, 2, 3]
for i in itr.repeat(e, 3):
    print(e)
