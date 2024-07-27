# The python standard library is a set of modules included with every python installation. Now that you've got a basic
# understanding of how functions and classes work, you can start using modules like these that other programmers have
# written.One interesting function from the random module is randint, that takes in 2 integer arguments and returns a
# random number between and including those numbers.

# Here an example of the randint function from the random module.
from random import  randint, choice, sample
number = randint(1,8)
print(number)

# Another interesting function from the random module is the Choice function. This method takes in a list or a tuple,
# and returns a randomly chosen element.

# Here's an example of the choice function.
players =  ["Marcus", "Lisandro", "Joshua"]
first = choice(players)
print(first)

# TRY IT YOURSELF:
# 1. - Die: that prints out a random number between 1 to 6.

class Die:
    """A class that represents the sides of a Die."""
    def __init__(self, sides=6):
        """Initialize the attributes of the Die Class."""
        self.sides = 6

    def roll_die(self):
        """A method that prints out 10 random numbers from the 6 sided die. """
        for self.sides in range(1,11):
            print((randint(1,self.sides)))
        print()

die1 = Die()
die1.roll_die()

die2 = Die(10)
die2.roll_die()



# 2. Lottery Number:
numbers = [1,2,4,7,5,8,0,12,56,87,4345,5676,2040, "q", "w", "n","o", "f"]
winning_number = sample(numbers,4)

print(winning_number)

