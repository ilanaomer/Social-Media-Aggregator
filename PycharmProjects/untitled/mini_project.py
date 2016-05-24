from csv import DictReader

with open('cow.csv' ,encoding ="utf-8") as f:
    reader = DictReader(f)
    for d in reader:
        print(d)

        