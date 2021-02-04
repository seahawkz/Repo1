## List less then #s

l1 = [1, 1, 11, 7, 3, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for n in l1:
    if n < 5:
        print(n) 
print([n for n in l1 if n < 5])

odd = [n for n in l1 if n % 2 != 0]
even = [n for n in l1 if n % 2 == 0]
print(odd)
print(even)

## Get unique items from list
l2 = []
for n in l1:
    if n not in l2:
        l2.append(n)
for n in l2:
    print(n)
for n in l2:
    if n < 5:
        print(n) 
print([n for n in l2 if n < 5])

odd2 = [n for n in l2 if n % 2 != 0]
even2 = [n for n in l2 if n % 2 == 0]
## Sort list
odd2.sort(reverse = True)
even2.sort()

print(odd2)
print(even2)   


