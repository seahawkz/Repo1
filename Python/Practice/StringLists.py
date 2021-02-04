###  Ask user for a string, then determine if it is a palindrome
def palindromeTest():
    word = str(input("Please enter a word: "))
    rev = word[::-1]
    print(rev)
    if word == rev:
        print("This word is a palindrome")
    else:
        print("This word isn't a palindrome")
for i in range(4):
    palindromeTest()
    