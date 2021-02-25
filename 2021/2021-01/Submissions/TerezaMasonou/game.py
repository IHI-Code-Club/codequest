"""
# rock paper scissors game
import numpy as np
from enum import IntEnum
import random

# creating enum for hand gestures in rock, paper, scissors
class Hand(IntEnum):
    rock=1
    paper=2
    scissors=3

isGameOver = False

print("Welcome to our game")
count = 1
while not isGameOver:
    print("Choose either rock,paper or scissors")
    user_input = input()
    count = count + 1
    
    """
    First player choice and reassigning user_input variable
    into a integer for later comparison
    """
    hasUserChosenCorrectly = False
    if user_input == Hand.rock.name:
        hasUserChosenCorrectly = True
        user_input = Hand.rock
        print("You have chosen rock")
    elif user_input == Hand.paper.name:
        hasUserChosenCorrectly = True
        user_input = Hand.paper
        print("You have chosen paper")
    elif user_input == Hand.scissors.name:
        hasUserChosenCorrectly = True
        user_input = Hand.scissors
        print("You have chosen scissors")
    else: 
        if count > 3:
            isGameOver = True
        else:
            print("Choose again")
    if hasUserChosenCorrectly == True:
        # Second player choice
        computer_input = random.randint(1,3)

        if computer_input == Hand.rock:
            print("The second player has chosen rock")
        elif computer_input == Hand.paper:
            print("The second player has chosen paper")
        else:
            print ("The second player has chosen scissors")

        # Finding winner

        if user_input == Hand.rock and computer_input == Hand.rock :
            print("Sorry, its a draw. No winner :(")
        elif user_input == Hand.rock and computer_input == Hand.paper :
            print("I am sorry, the second player has won")
        elif user_input == Hand.rock and computer_input == Hand.scissors :
            print("You have won the game!! :)")
        elif user_input == Hand.paper and computer_input == Hand.rock :
             print("You have won the game!! :)")
        elif user_input == Hand.paper and computer_input == Hand.paper :
             print("Sorry, its a draw. No winner :(")
        elif user_input == Hand.paper and computer_input == Hand.scissors :
            print("I am sorry, the second player has won")
        elif user_input == Hand.scissors and computer_input == Hand.rock :
             print("I am sorry, the second player has won")
        elif user_input == Hand.scissors and computer_input == Hand.paper :
             print("You have won the game!! :)")
        elif user_input == Hand.scissors and computer_input == Hand.scissors :
            print("Sorry, its a draw. No winner :(")
        print("Type stop to end the game otherwise press enter to play again")
        another_input = input()
        if(another_input == "stop"):
            isGameOver = True

    



    


"""
