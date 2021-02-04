###  Take a list of numbers and make a new list with only even

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

for n in a:
    if n % 2 == 0:
        b.append(n)
print(b)

##better way to do it....

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]

print(b)

##  generate random lists, then run

import random

numlist = []
list_length = random.randint(5,15)


while len(numlist) < list_length:
    numlist.append(random.randint(1,75))
    

evenlist = [number for number in numlist if number % 2 == 0] 
evenlist.sort()

print(numlist)
print(evenlist)