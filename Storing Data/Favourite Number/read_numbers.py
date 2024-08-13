import json
filename = "favourite_number.json"

with open(filename) as f:
    content = json.load(f)
    print(f"Your favourite number is: {content}.")