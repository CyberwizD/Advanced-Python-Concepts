# Sequence of 1 to 90

def mygenerator(n):
    for i in range(n):
        yield i

values = mygenerator(90)

for x in values:
    print(x)

def infinite_sequence():
    sum = 1
    while True:
        yield sum
        sum += 2

value = infinite_sequence()

for i in value:
    print(i)
    if i == 99:
        break


# Trial
num_list = []
for i in range(90):
    num_list.append(i)

print(num_list)
