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
    print(f"\n{city} is in the {country}\n")

describe_city("Manchester")
describe_city("London")
describe_city("Kathmandu")


# Returning a simple value.
# Let's look at a function, that takes in a first name and last name and returns a neatly formatted full name.

def full_name(first, last):
    """A function that takes in 2 args and returns a neatly formatted fullname."""
    full = f"{first} {last}"
    return full.title()

musician = full_name("Angus","Young")
print(musician)
actor = full_name("Tom","Cruise")
print(f"{actor} is the best action hero ever.")

# Making an argument optional, sometimes it is necessary to make an argument optional, so that people can choose either
# to provide value or not.

def name(first, last, middle=""):
    """This function takes, first name and last name, and an optional middle name and returns a neatly formatted full name"""
    if middle:
        full = f"\n{first} {middle} {last}"
        return full.title()
    else:
        full = (f"\n"
                f"{first} {last}")
        return full.title()

player = name("Wayne","Rooney","Mark")
print(player)
me = name("Abishek","Phuyal")
print(me)


# More exercises with functions:

# 1 City Names:
def city_country(city, country):
    """A simple function that takes in city & country as arguments and returns in a nicely formatted manner."""
    info = f'\n"{city} {country}"\n'
    return info.title()

uno = city_country("Santiago","Chile")
print(uno)
eng = city_country("London","England")
print(eng)
wal= city_country("Cardiff","Wales")
print(wal)


# 2. Describe Music Album - Music Album

def music_album(artist,album_name):
    """Takes in 2 arguments, name of artist and album name and returns it in a dictionary."""
    album = {"Artist":artist, "Album":album_name}
    return album

gnr = music_album("Guns n Roses","Appetite For Destruction")
print(gnr)
met = music_album("Metallica","Ride The Lightning")
print(met)
acd = music_album("AC/DC","Back in Black")
print(acd)





