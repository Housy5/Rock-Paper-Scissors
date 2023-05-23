from system import *
from player import *

import random
import math

def compliment(opt: str):
    options = "spr"
    index = (options.index(opt) + 1) % 3
    return options[index] 

def translate(opt: str):
    options = ("Scissors", "Papper", "Rock")
    for x in options:
        if x[0].lower() == opt:
            return x
    return None

def get_user_choice():
    legals = "spr"
    choice = input("Please enter your option ((s)cissors, (p)apper, (r)ock): ").lower()
    return choice if choice in legals else random.choice(legals)

def score_function(x):
    sum = 0
    for i in range(x):
        sum += math.ceil(math.log(i + 1, math.pi))
    return sum + 1

def request_rounds():
    min = 1
    default = 3
    max = 50
    
    try:
        rounds = int(input(f"Please enter the number of rounds you want to play ({min} - {max}): "))
        return rounds if rounds in range(min, max) else default
    except ValueError:
        return default

def main():
    computer = ComputerPlayer()
    player = create_player()
    rounds = request_rounds()
    round_count = 0
    
    while round_count < rounds:
        cls()
        print(f"Round: {round_count}/{rounds}.")
        print(f"Computer score: {computer.score}.")
        print(f"{player.name}'s score: {player.score}.")
        computer_choice = computer.roll()
        player_choice = get_user_choice()
        
        print()
        if computer_choice == player_choice:
            print("It's a tie!")
        elif computer_choice == compliment(player_choice):
            print("Player wins this round!")
            player.score += score_function(round_count)
        else:
            print("Computer wins this round!")
            computer.score += score_function(round_count)
        
        print()
        print(f"Computer choice: {translate(computer_choice)}.")
        print(f"{player.name}'s choice: {translate(player_choice)}.")
        input("Press enter to continue...")
        round_count += 1

    cls()
    print(f"Computer score: {computer.score}.")
    print(f"{player.name}'s score: {player.score}.")
    if computer.score == player.score:
        print("It's a tie!")
        return
    print(f"{max_player(player, computer).name} won!")
    
if __name__ == "__main__":
    check_os()
    main()