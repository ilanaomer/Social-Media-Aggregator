import os
from csv import DictReader

with open('ctemplate.txt', encoding="utf-8") as fTemp:
    s = fTemp.read()

with open('cow.csv', encoding="utf-8") as f:
    d = DictReader(f)
    for x in d:
        path_name = os.path.join("Co_html", "{}.html".format(x['short_name']))
        with open(path_name, "w", encoding="utf-8") as fw:
            print(s.format(x['name'], x['name'], x['capital'], x['population'], x['land'], x['continent']), file=fw)
            #     fw.write(s.format(x['name'], x['name'], x['capital'], x['population'], x['land'], x['continent']))
