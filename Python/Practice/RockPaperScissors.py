### Rock paper scissors game
def rps():
    ## get player names
    player1 = input("Please tell me your name: ")
    player2 = input("Please tell me your name: ")
    ## have player choose r p s
    def choice():
        p1c = input(player1 + " please choose rock, paper or scissors: ")
        if p1c == "exit":
            exit()
        p2c = input(player2 + " please choose rock, paper or scissors: ")
        if p2c == "exit":
            exit()
        rs = "Rock smashes scissors,"
        sp = "Scissors cut paper"
        pr = "Paper covers rock,"
        if p1c == p2c:
            print("It's a tie!!  Please choose again")
            choice()
        elif p1c == 'rock' and p2c == 'scissors':
            print(rs, player1, "you win!")
        elif p1c == 'rock' and p2c == 'paper':
            print(pr, player2, "you win!")
        elif p1c == 'scissors' and p2c == 'paper':
            print(sp, player1, "you win!")
        elif p1c == 'scissors' and p2c == 'rock':
            print(rs, player2, "you win!")
        elif p1c == 'paper' and p2c == 'rock':
            print(pr, player1, "you win!")
        elif p1c == 'paper' and p2c == 'scissors':
            print(rs, player2, "you win!")
        else:
            print('Please make a valid selection or type "exit" to leave the game')
            choice()
            

    choice()

rps()      





