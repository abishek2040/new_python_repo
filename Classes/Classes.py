# In object oriented programming, you write classes that represent the real world things and situations, and you create
# objects based on these classes. When you write a class, you define the general behaviour that a whole category of
# objects can have.

""" When you create individual objects from the class, each object is automatically equipped with the general behaviour;
 you can then give the object any unique trait that you desire. Making an object from a class is called instantiation,
 and you work with instances of a class.
 Understanding object oriented programming, will help you see the world as a programmer does. It'll help you really
 know your code, not just what's happening line by line, but the bigger concepts behind it.
 """

# We can model almost anything using classes, here's an example, by creating a simple class Dog.

class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize the name and age attributes. """
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is sitting.")

    def roll_over(self):
        """simulate, rolling over of the dog in response to a command."""
        print(f"{self.name} is rolling over on the floor.")

# Let's make an instance representing a specific dog.

my_dog = Dog("Rocky",7) # Creating an instance my_dog from the dog class representing a specific dog.
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Tommy",12)
print(f"\nMy dog's name is: {your_dog.name}")
your_dog.sit()
your_dog.roll_over()


# TRY IT YOURSELF:
# 1. Restaurant:

class Restaurant:
    """Modelling a restaurant object."""
    def __init__(self, name, cuisine):
        """Initialize the details of the restaurant."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(f"\nThe name of the restaurant is: {self.name} & it servers {self.cuisine} food.")

    def open(self):
        print(f"Yes we are open today.")

restaurant = Restaurant("Spice69", "Indian.")
restaurant.describe_restaurant()
restaurant.open()

nepali_restaurant = Restaurant("Gurkha Lounge", "Nepali")
nepali_restaurant.describe_restaurant()
nepali_restaurant.open()

british = Restaurant("The Red Lion", "British")
british.describe_restaurant()
british.open()


class User:
    """Modelling a general user object. """
    def __init__(self, first_name, last_name):
        """Initialize the parameters of the class. """
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Describe the user object."""
        print(f"\nThe user's name is: {self.first_name} {self.last_name}")

    def greet_user(self):
        """A method that describes the specific user."""
        print(f"Hello, Mr {self.last_name} how are you doing today. Great to see you out here.")

user1 = User("Abishek", "Phuyal")
user1.describe_user()
user1.greet_user()

user2 = User("Tony", "Tatton")
user2.describe_user()
user2.greet_user()

user3 = User("Tina", "Turner")
user3.describe_user()
user3.greet_user()

