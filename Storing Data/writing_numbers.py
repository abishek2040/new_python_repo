# Storing Data in python, using JSON Module. The JSON module allows you to dump simple python data structures into a
# file and load the data from the file the next time the program runs. JSON format is a very efficient way to store data
# in python, or any other language, as it is not specific to python and can be used by people using other programming
# language. It is a portable and an easy to learn human-readable language.

"""JSON was originally developed for JavaScript, however it has become a common format used by many languages including
python."""


"""Using Json.dump() * Json.load()
Let's write 2 programs, one that stores a set of numbers and another program that reads these numbers back into the
memory. The first program will use json.dump() to store and the second program will use the json.load() function to load 
the numbers back into the memory."""

import json

numbers = [1,2,3,4,5,6,7,8,9,0]

filename = "numbers.json"

with open(filename, "w") as f:
    json.dump(numbers, f)


"""Now we'll write another program that loads the numbers back into the memory."""
