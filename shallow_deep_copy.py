# Shallow copy - One level deep, only references of nested child objects
# Deep copy - Full independent copy

import copy

# Immutable data types
num = 4
cp_num = num
cp_num = 5

print('Original number: ', num)
print('Copied number: ', cp_num)


# Mutable data types
list_ = [1, 2, 3]
list_cp = list_
list_cp[2] = 4

print('Original list: ', list_)
print('Copied list: ', list_cp)  # Original and Copied list remains the same


# Usage of copy module
# Shallow copy - copies only one level of index []
shallow_copy = copy.copy(list_)  # OR copy_list = list_.copy() # OR copy_list = list_[:]
shallow_copy[2] = 6

print('Shallow copy -', shallow_copy)

# Deep copy - copies at all level of index [][][]
large_list = [[1, 2], [3, 4], [5, 6]]
deep_copy = copy.deepcopy(large_list)
deep_copy[1][1] = 3

print('Deep copy -', deep_copy)
