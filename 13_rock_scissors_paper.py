import random
import time

commands=["rock", "paper", "scissors"]
user_score=0
computer_score=0

while True:
    user=input("Choose between rock, paper, scissors or break (if you say break, the game will be over.):")
    if user=="rock" or user=="paper" or user=="scissors" or user=="break":
        computer=random.choice(commands)
        if user=="rock" and computer=="scissors":
            print("You win, congratulations!")
            print("Selection of computer: ", computer, "Your selection: ", user)
            user_score=user_score+1
            time.sleep(0.5)
        elif user=="scissors" and computer=="paper":
            print("You win, congratulations!")
            print("Selection of computer: ", computer, "Your selection: ", user)
            user_score=user_score+1
            time.sleep(0.5)
        elif user=="paper" and computer=="rock":
            print("You win, congratulations!")
            print("Selection of computer: ", computer, "Your selection: ", user)
            user_score=user_score+1
            time.sleep(0.5)
        elif user==computer:
            print("Draw!")
            print("Selection of computer: ", computer, "Your selection: ", user)
            time.sleep(0.5)
        elif user=="break":
            print("The game is over, goodbye!")
            break            
        else:
            print("Computer won, maybe next time!")
            print("Selection of computer: ", computer, "Your selection: ", user)
            computer_score=computer_score+1
            time.sleep(0.5)
    else:
        print("You entered incorrectly, please correct your answer. (rock, paper, scissors)")
print("Computers score: ", computer_score, "   Users score: ", user_score)
