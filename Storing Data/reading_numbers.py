import json

filename = "numbers.json"
with open(filename) as f:
    numbers = json.load(f) # Assigning the value from the json file to the variable number & printing it.
print(numbers)
