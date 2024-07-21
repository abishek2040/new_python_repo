# Exercise - 1: Create a restaurant class, and add the basic attributes with one changing attribute - numbers served.

# # # # Class - 1
class Restaurant:
    """A model of a running restaurant. """
    def __init__(self, name, cuisine):
        """Initialize the attributes. """
        self.name = name
        self.cuisine = cuisine
        self.numbers_served = 0

    def describe_restaurant(self):
        """Print about the restaurant."""
        print(f"The restaurant serve {self.cuisine} & it's name is: {self.name}")
        print(f"It has served {self.numbers_served} number of people.")

    def set_number_served(self, add):
        """Adds the number of customer served by the restaurant"""
        self.numbers_served = add
        print(f"\nThe restaurant has now served: {self.numbers_served} customers.")

restaurant = Restaurant("Spice 7", "Chinese")
restaurant.describe_restaurant()

restaurant.set_number_served(100)


# # # # Class Exercise -2: Login Attempts

class User:
    """A class that represents a user in a social networking site. """
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Describes the user."""
        print(f"\nThe name of the user is {self.name}, age is {self.age} and the location is: {self.location} & \n"
              f"the login attempts: {self.login_attempts}")

    def increment_login(self):
        """Increases the login attempt of a user"""
        self.login_attempts += 2
        print(f"Login attempts on your account is: {self.login_attempts}")


user1 = User("Abishek", 22, "London")
user1.describe_user()

user1.increment_login()
