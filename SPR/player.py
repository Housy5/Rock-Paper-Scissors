from system import cls
import random

class Player:
    
    def __init__(self, name: str):
        self.score = 0
        self.name = name

class ComputerPlayer(Player):
    
    options = ("s", "p", "r")
    
    def __init__(self):
        Player.__init__(self, "Computer")
    
    def roll(self):
        return random.choice(self.options)

def max_player(p1: Player, p2: Player) -> Player:
    return p1 if p1.score > p2.score else p2 

def create_player():
    opt = 'n'
    while opt != 'y':
        cls()
        name = input("Please enter a name: ")
        opt = input(f"Are you sure you want to use {name}? (y/n): ").lower()
    return Player(name)