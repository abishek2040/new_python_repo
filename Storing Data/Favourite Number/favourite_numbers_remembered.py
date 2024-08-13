import json

filename = "favourite_number.json"

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = int(input("Enter your favourite number: "))
    with open(filename, "w") as f:
        json.dump(number, f)
        print("Your favourite number has been saved. ")
else:
    print(f"I know your favourite number! It's {number}.")