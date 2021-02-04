## Create program that asks for a number then prints out all the divisors of that number
def divisors():
    num = int(input("Give me a number to divide: "))
    div = []
    l1 = list(range(1,num + 1))
    for n in l1:
        if num % n == 0:
            div.append(n)
    print(div)

for x in range(4):
    divisors()
