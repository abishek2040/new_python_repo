import json

filename = "username.json"
try:
    with open(filename) as fn:
        username = json.load(fn)
except FileNotFoundError:
    username = input("Enter your username: ")
    with open(filename, "w") as fn:
        json.dump(username, fn)
        print(f"We will remember you when you come back {username}")
else:
    print(f"Welcome back {username}")


