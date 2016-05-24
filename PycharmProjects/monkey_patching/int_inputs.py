def intputs(prompt=">> ", invalid_message="Invalid input"):
    """Generates a sequence of integers read from standard input, one per row,
    until an empty line is reached.  For non-numeric inputs, displays
    invalid_input to the users, and continues input.
    """
    while True:
        s = input(prompt)
        if not s:
            break
        try:
            yield int(s)
        except ValueError:
            print(invalid_message)

# for x in intputs():
#     print(x if x % 7 else "Boom!")
# print("Done!")


def accumulate(data):
    counter_data = 0
    for i in data:
        counter_data += i
        yield (i, counter_data)

for x, total in accumulate(intputs()):
    print("${} accepted, total: ${}".format(x, total))
