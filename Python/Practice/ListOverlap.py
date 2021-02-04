## Finds common elements from two or more lists

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in b:
    if i in a and i not in c:
        c.append(i)
print(c)