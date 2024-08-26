# Molecular Motion:
from random import choice


class RandomWalk:
    """A class to generate a randomwalk for a molecular motion. """

    def __init__(self, num_points):
        """Initialise the attributes of the walk. """
        self.num_points = num_points

        # The walk starts at the cordinate (0,0
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """A method to get the step."""
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        y_step = y_direction * y_distance

        return x_step, y_step

    def fill_walk(self):
        """A method to fill the walk."""
        while len(self.x_values) < self.num_points:
            x_step, y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

                # Calculate the next x and y values for the walk.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
