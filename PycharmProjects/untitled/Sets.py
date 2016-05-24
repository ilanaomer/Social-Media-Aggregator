import time
import random
from random import randint
num = 0
rs = set()
for i in range(10000):
    rs.add(randint(1,1000000))
t = time.time()
for x in rs:
    if randint(1,1000000) in rs:
        num += 1
t = time.time()-t
print("There is {} times. its take {} seconds.".format(num,t))


num = 0
rs = []
for i in range(10000):
    rs.append(randint(1,1000000))
t = time.time()
for x in rs:
    if randint(1,1000000) in rs:
        num += 1
t = time.time()-t
print("There is {} times. its take {} seconds.".format(num,t))





