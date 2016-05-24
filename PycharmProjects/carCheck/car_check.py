import collections

class Report:
    def __init__(self, num='00-000-00'):
        self.number = num
        self.check_list = collections.OrderedDict()

    def add_check(self, component, result):
        self.check_list[component] = result

    def passed(self):
        # for c, b in self.check_list.items():
        #     if b is False:
        #         return False
        # return True
        return all(self.check_list.values())

    def render(self):
        s = "Results for car #{}\n".format(self.number)
        for compo, res in self.check_list.items():
            s += "* {}: {}\n".format(compo, "OK" if res else "Failed")
        s += "PASSED" if self.passed() else "NOT PASSED"
        return s
