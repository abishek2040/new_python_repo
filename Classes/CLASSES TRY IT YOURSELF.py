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


# Exercise - 2: Admin User

class User:
    """An attempt to model a user: """
    def __init__(self, first_name, last_name):
        """Initialize the attributes of the class."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Describe User"""
        print(f"\nThe user name is: {self.first_name} {self.last_name}")

    def greet_user(self):
        """A method that greets the user."""
        print(f"Hello, {self.first_name} {self.last_name} good to see you today.")


class Privileges:
    """A new class that holds the privileges for the admin user. """
    def __init__(self):
        """Initialize the attributes for this class."""
        self.privileges = ["Can Add Post", "Can Delete Post", "Can Add User", "Can Ban User"]

    def show_privileges(self):
        """A method that lists out all the privileges for the admin user."""
        print(f"\nHello you are an Admin & you have the following rights.")
        for actions in self.privileges:
            print(actions)

class Admin(User):
    """A subclass that inherits attributes and the methods from the User superclass."""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


admin1 = Admin("Abishek", "Phuyal")
admin1.describe_user()
admin1.greet_user()
admin1.privileges.show_privileges()