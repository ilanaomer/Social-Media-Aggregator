def make_return_out_scop_i(i):
    def f():
        return i
    return f

def make_printers_buggy(n):
    l = []
    for i in range(n):
        l.append(make_return_out_scop_i(i))

    return l

printers = make_printers_buggy(10)

for f in printers:
    print(f())
