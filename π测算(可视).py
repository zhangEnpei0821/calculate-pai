import matplotlib.pyplot as plt
import random
import string

plt.style.use('seaborn')
fig, ax = plt.subplots()

m = 100
n = 0

for i in range(m):
    x = random.random()
    y = random.random()
    square = x**2 + y**2
    if square <= 1:
        n += 1
        ax.scatter(x, y, c='red', s=5)
    else:
        ax.scatter(x, y, c='green', s=5)

print(4*n/m)
plt.show()