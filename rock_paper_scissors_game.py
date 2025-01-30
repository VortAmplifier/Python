# Rock, Paper, Scissors Game in Python
# Game rules:
# -----------
# 1. If one player chooses rock and the other player chooses scissors, then rock wins.
# 2. If one player chosses scissors and the other player chooses paper, then scissors wins.
# 3. If one player chooses paper and the other player chooses rock, then paper wins.
# 4. If both players make the same choice, the game must be played again to determine the winner.
# Simple probability is used for total of six possible combinations 2 players x 3 choices of game pairs

import random

computer_items = {1: "rock", 2: "paper", 3: "scissors"}

print("---ROCK, PAPER, SCISSORS GAME---")
print("--------------------------------")

while True:
    player_item = input("Enter rock, paper or scissors: ")
    random_comp_item = random.randint(1, 3)
    print("Computer chose", computer_items[random_comp_item])
    if player_item == "rock" and computer_items[random_comp_item] == "scissors":
        print("You win! Rock smashes scissors.")
    elif player_item == "scissors" and computer_items[random_comp_item] == "paper":
        print("You win! Scissors cuts paper")
    elif player_item == "paper" and computer_items[random_comp_item] == "rock":
        print("You win! Paper wraps rock.")
    elif player_item == "rock" and computer_items[random_comp_item] == "paper":
        print("Computer wins! Paper covers rock.")
    elif player_item == "scissors" and computer_items[random_comp_item] == "rock":
        print("Computer wins! Rock smashes scissors.")
    elif player_item == "paper" and computer_items[random_comp_item] == "scissors":
        print("Computer wins! Scissors cuts paper.")
    elif player_item == computer_items[random_comp_item]:
        print("A draw! Game repeats again")
        print("--------------------------")
        continue

    play_again = input("Would you like to play again? (y/n) ")
    if play_again.lower() == "y":
        continue
    elif play_again.lower() == "n":
        break
print("Game exit: Success! Come back later to play Rock, Paper, Scissors")

    
