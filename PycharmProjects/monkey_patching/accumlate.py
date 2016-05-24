def accumulate(data):
    counter_data = 0
    for i in data:
        counter_data += i
        yield (i, counter_data)

for i, total in accumulate(range(1, 11)):  # in python 2: use xrange.
    print(i, total)

print()

for i, total in accumulate([100, 10, 5, 200]):
    print(i, total)