"""TRY IT YOURSELF - EXERCISES:"""

class Restaurant:
    """A class that models different restaurants. """
    def __init__(self, name, cuisine):
        """Initialize the attributes of the class. """
        self.name = name
        self.cuisine = cuisine
        self.numbers_served = 10

    def describe_restaurant(self):
        """A method that describes the restaurant."""
        print(f"The name of the restaurant is: {self.name} and it serves {self.cuisine} food.")

class Icecreamstand(Restaurant):
    """Creating a new class that inherits some attributes from the superclass."""
    def __init__(self, name, cuisine):
        """Initializing the attributes of the superclass."""
        super().__init__(name, cuisine)
        self.flavours = ["Chocolate", "Vanilla", "Blueberry", "Cookies&cream"]

    def print_flavours(self):
        """This method prints out the available flavours."""
        print(f"The available flavours are:")
        for flavour in self.flavours:
            print(flavour)

shop1 = Icecreamstand("Baskin&Robin", "Dessert")
shop1.describe_restaurant()
shop1.print_flavours()

