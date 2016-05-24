import calendar


class MyTextCalendar(calendar.TextCalendar):
    def formatmonth(self, theyear, themonth, w=0, l=0):
        s = super().formatmonth(theyear,themonth)
        for i in s.split()[9:]:
            i = '*' if int(i) % 7 or int(i) / 10 == 7 else i
        return "".join(s)


c = MyTextCalendar()
result = c.formatmonth(2014, 5)
print("My calendar:")
print("-" * 40)
print(result)
print("-" * 40)

expected = '''      May 2014
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  *  8  9 10 11
12 13  * 15 16  * 18
19 20  * 22 23 24 25
26  *  * 29 30 31
'''
print("Expected:")
print("-" * 40)
print(expected)
print( "-" * 40)

assert result == expected