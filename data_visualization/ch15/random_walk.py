# random walk class

from random import choice
#import random

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""

        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

        # try this later, choose a random location for starting point
        #random.seed()
        #self.x_values = [random.randint(0,10)]
        #self.y_values = [random.randint(0,10)]

    def fill_walk(self):
        """Calculate all positions in the walk."""

        # Keep taking steps until the walk reaches desired length
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction
            x_step = self.get_dist_direction()
            y_step = self.get_dist_direction()

            # Reject moves that go nowhere (note: why?)
            if (x_step and y_step) == 0:
                continue

            # Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_dist_direction(self):
        """Get distance and direction of each step, made this a method"""
        # Calculate distance and direction for step
        # I'm lazy so why not make this process a method
        direction = choice([1,-1])
        distance = choice(range(5))
        step = direction * distance

        return step
