# While loops with functions:
def music_info(artist,album):
    """A function that takes in artist name and album name and presents in a neatly formatted way."""
    info = {"Artist":artist,"Album":album}
    return info

while True:
    print("Enter 'q' to quit.")
    artist_name = input("What is the name of the artist: ")
    if artist_name == "q":
        break
    album_name = input("What is the name of the Album: ")
    if album_name == "q":
        break

    details = music_info(artist_name, album_name)
    print(details)
print("Thank you for playing: ")



# Passing a list to a function:
print()
def greet_users(guests):
    """This function takes a list of users and prints out personalized greetings to each user on the list."""
    for users in guests:
        print(f"Hello {users}, really nice to see you here.")

one = ["Abishek","Pramis","Rejin","Sudarshan"]
greet_users(one)


# Modifying a list in a function:
