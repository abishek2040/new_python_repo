# Here we'll use python to generate data for random walk, and then use matplotlib to create a visually appealing
# representaion of that data. A random walk is a path that has no clear direction but rather consists of steps
# that are randomly chosen from a set of pre-defined directions. This code will create a random walk with a specified
# number of steps, and then plot the resulting path on a graph.

# To create a random walk, we'll create a RandomWalk class, which will make random decisions about which direction the
# walk should take. The class needs three attributes: One variable to store the number of points in the walks, and two
# lists to store the x- and the y-cordinate values of each point in the walk.

# We'll only need two methods for the RandomWalk Class: The __init__() method and the fill_walk(), which will calculate
# the points in the walk. Let's start with __init__() as shown here.

from random import choice

class RandomWalk:
    """A class to generate Random Walks"""
    def __init__(self, num_points = 5000):
        """Initialise the attributes of the walk."""
        self.num_points = num_points

        #All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2,3,4,5,6,7,8,9,10,11])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2,3,4,5,6,7,8,9,10,11])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values for the walk.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)