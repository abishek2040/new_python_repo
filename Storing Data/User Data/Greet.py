import json

filename = "username.json"
with open(filename) as fn:
    username = json.load(fn)
    print(f"Hello, {username} welcome back.")