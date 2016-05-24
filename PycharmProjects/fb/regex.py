import re


re_camel_case_functions = re.compile(r"\b_?[a-z]+[A-Z]\w*\b")

with open("ut.txt") as ut:
    heystack = ut.read()


#http://stackoverflow.com/questions/7322028/how-to-replace-uppercase-with-underscore
def f(me):
    return re.sub('(?<!^)(?=[A-Z])', '_', me.group(0)).lower()


print(re_camel_case_functions.sub(f, heystack))


# def fix(m):
#     return "_" + m.group(0).lower()
#
#
# def f(me):
#     return RE3.sub(fix, me.group(0))



