##  Ask for number, print out if number is even or odd.
def oddEven():
    num = int(input("Please give me a number: "))
    if num % 4 == 0:
        print(num, "is a multiple of 4")
    elif num % 3 == 0:
        print(num, "is a multiple of 3")
    elif num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")

for n in range(4):
    oddEven()
