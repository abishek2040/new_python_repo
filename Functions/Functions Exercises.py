# Here is some exercises from the functions chapter.

# 1. write a function to print out a message.

def print_out():
    """A simple function to print out a message"""
    print("Hello, I am doing very well today how are you.")

print_out()

# 2. Write a program that takes your favourite book and prints out about it.

def message(book):
    """A simple function that takes in a favourite book and prints it out."""
    print(f"{book} is my favourite book.")

message("\nThink & Grow Rich")

# Types of Arguments - Positional arguments vs Keyword Arguments
# when we call a function with parameters, we need to provide arguments as the same order of the parameters.

# for example.

def full_name(name, surname):
    """This function asks for name & surname and prints out both."""
    print(f"{name} {surname}")

full_name("Abishek", "Phuyal")
full_name("Phuyal", "Abishek") # Here the order matters, while passing the argument.

# Let's have a look at the keyword argument, where the keyword doesn't matter.

full_name(surname="Phuyal",name="Abishek") # No matter the position of the passed arguments, we always get the right result.


# Default values in a function, for example:
def describe_pet(name, color, type="dog"):
    """A simple function with a default value."""
    print(f"I have a pet {type}, it's name is: {name}.")
    print(f"It's color is: {color}")

describe_pet("Rocky", "black ")


# Exercise - 3

def make_shirt(size, message):
    """Accepts size & message on the shirt and prints out information."""
    print(f"\nWe are printing your {size} size shirt with the message '{message}' on it.")

make_shirt("M", "Hello World")


# Exercise - 4:
def default_shirt(message, size = "M"):
    """Shirt with default value Medium"""
    print(f"\t\nWe are printing your {size} size shirt with the message `{message}` on it.")

default_shirt("I love python")


# Exercise - 5

def describe_city(city, country="UK"):
    """Accepts name of the city and its country"""
    print(f"\n{city} is in the {country}")

describe_city("Manchester")
describe_city("London")
describe_city("Kathmandu")
