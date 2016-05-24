import time

def calculate_life():
    time.sleep(3)
    return 42


def make_it_self_cache(f):
    result = []
    def new_f():
        if not result:
            result.append(f())
        return result[0]
    return new_f


@make_it_self_cache
def get_stuff():
    time.sleep(2)
    return ['apple', 'pear']
# get_stuff = make_it_self_cache(get_stuff)
calculate_life = make_it_self_cache(calculate_life)


for n in range(10):
    print(calculate_life())
for n in range(10):
    print(get_stuff())