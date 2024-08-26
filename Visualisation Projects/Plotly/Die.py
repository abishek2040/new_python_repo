# Rolling Dice with Plotly:
# Plotly is a data visualization library that provides a convenient way to create interactive plots and visualizations.
from random import randint

class Dice:
    """A class representing a single Die."""
    def __init__(self, num_sides=6):
        """Assume six sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

