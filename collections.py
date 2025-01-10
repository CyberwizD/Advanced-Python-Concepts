# Collections - Counter, namedtuple, OrderedDict, defaultdict, deque

import collections as cs

# Counter
letters = "aaaabbbccd"
letter_count = cs.Counter(letters)

print(letter_count.items())
print(list(letter_count.elements()))
print(letter_count)
print(letter_count.keys())
print(letter_count.values())
print(letter_count.most_common(2))  # (2) represents the two most common element
print(letter_count.most_common(2)[0])  # [0] accesses the tuple index
print(letter_count.most_common(2)[0][1])  # [1] access the second element of the tuple


# Namedtuple
point = cs.namedtuple("Point", 'x, y, z')
pt1 = point(2, 3, 4)
print(pt1)
print("Added Points: ", pt1.x + pt1.y + pt1.z)


# OrderedDict
ordered_dict = cs.OrderedDict()  # Or ordered_dict = {}
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)


# DefaultDict
d = cs.defaultdict(int)  # int as default type
d['a'] = 1
d['b'] = 2

print(d)
print(d['a'])
print(d['c'])  # Returns 0. [] if default type is list


# Deque
d = cs.deque()

d.append(1)
d.popleft()
d.rotate()
d.clear()
d.append(0)
d.append(1)
d.appendleft(1)
d.extend([2])
d.extendleft([2])

print(d)
