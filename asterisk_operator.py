# Use Cases

mul = 4 * 3
pwr = 2 ** 3
lst = [2] * 2
tp = ("abc", "123") * 2

print(mul)
print(pwr)
print(lst)
print(tp)


def num(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


num(1, 2, 3, 4, 5, 6, 7, 8, 9, zero=0)

mylist = [3, 4]  # The number of elements must match the number of parameters when unpacking
num(*mylist)

mydict = {'a': 1, 'b': 2}
num(*mydict)  # Keys of mydict
num(**mydict)  # Values of mydict

number_list = [1, 2, 3, 4, 5]

*beginning, last = number_list
bgn, *lst = number_list
b, *m, lt = number_list

print(*beginning)
print(last)

print(bgn)
print(lst)

print(m)

my_tuple = (1, 2, 3)
my_lst = [4, 5, 6]

row_list = [*my_tuple, *my_lst]
print(row_list)

dict1 = {'A': 1, 'B': 2}
dict2 = {'C': 3, 'D': 4}

key_dict = [*dict1, *dict2]
value_dict = {**dict1, **dict2}

print(key_dict)
print(value_dict)
