##  Guessing game
import random

ranNum = random.randint(1,99)
count = 0
guess = 0

while guess != ranNum and guess != 'exit':
    guess = input("Guess a number between 1 and 99: ")
    if guess == 'exit':
        break
    guess = int(guess)
    count += 1
    if ranNum == guess:
        print("You have guessed my number!")
        print("It only took you", count, "tries!")
    elif guess > ranNum:
        print("Your guess is higher than my number, please try again.")
    elif guess < ranNum:
        print("Your guess is lower than my number, please try again.")
    else:
        print('Please enter a valid number between 1 and 9.  Type "exit" to leave program')