import random
import string

n = 0

for i in range(1000000):
    x = random.random()
    y = random.random()
    square = x**2 + y**2
    if square <= 1:
        n += 1

print(n/250000)