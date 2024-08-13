# Favorite Number:

import json

number = int(input("Enter your favourite number: "))
filename = "favourite_number.json"
with open(filename, "w") as fn:
    json.dump(number, fn)
    print("Thank you your number has been saved. ")