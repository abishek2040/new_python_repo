# Functions are named block of code in python that are designed to do one specific job or task, that are available to
""" Functions in simple terms are a block of code that is designed to do one specific task, they are helpful to tackle
    repeatitive tasks. If you need to run the function you call the function with any parameters that it requires or without
    it. """

# Here's a simple example of a function in pyhton:

def greet_user():
    """This function prints out the hello message."""
    print("Hello,how are you doing. ")

greet_user() #Here we are calling the function, it runs the print statement.


# Here's another function example that takes in a name as an input.

def greet_user(name):
    """A simple function that takes in a name, and prints out a greetings message."""
    print(f"\nHello, {name} really nice to see you here today. ")

greet_user("Abishek") # Calling the function and passing the argument: "Abishek" to the parameter: "name".
greet_user("Lewis")
