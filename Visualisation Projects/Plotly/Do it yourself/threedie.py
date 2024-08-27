from random import random

class Dice:
    def __init__(self, num_sides =6):
        self.num_sides = num_sides

    def roll(self):
        return int(random() * self.num_sides) + 1
