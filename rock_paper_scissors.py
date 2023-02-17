import random

while True:

    choices =['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None



    while player not in choices:
        player = input("rock, paper, or scissors? :").lower()


    if player == computer:
        print("computer: ", computer)
        print("player: " ,player)
        print("Tie") 
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: " ,player)
            print("you lose!")
        if computer == "scissor":
            print("computer: ", computer)
            print("player: " ,player)
            print("you win!")
    elif player == "scissor":
        if computer == "rock":
            print("computer: ", computer)
            print("player: " ,player)
            print("you win!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: " ,player)
            print("you lose!")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: " ,player)
            print("you lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: " ,player)
            print("you win!")


    play_again = input("play again? Yes/No: ").lower()
    
    if play_again != "yes":
        break
print("Thanks for playing!")
        
