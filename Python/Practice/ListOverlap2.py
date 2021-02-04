##  Compare two randomly created lists and return a new list with common items

import random

a = random.sample(range(1,50), 25)
b = random.sample(range(1,50), 30)
c = [n for n in a if n in b]
a.sort()
b.sort()
c.sort()

print(a)
print(b)
print(c)
