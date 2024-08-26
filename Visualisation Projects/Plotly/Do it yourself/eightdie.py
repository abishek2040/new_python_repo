from random import  randint

# Create a Dice class to model a die - Default sides = 8

class Dice:
    """Modelling a dice object."""
    def __init__(self, num_sides=8):
        self.num_sides = num_sides


    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
