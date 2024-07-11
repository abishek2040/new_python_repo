# Using a while loop with Lists & Dictionaries
# A for Loop is effective for looping through a list, but you shouldn't modify a list inside a for loop because python
# will have trouble keeping track of the items in the list. To modify a list, while you work through, use a while loop.

# Example of working with while loops in a list.

unconfirmed_users = ["Alice", "Brian", "Max","Lewis", "Brad"]
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users:
print(f"\nThe following users have been verified: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing all instances of specific items from a list using a while loop.
pets = ["dogs", "cats", "dogs", "parrots", "dogs", "cats","cats"]
print(pets)

while "cats" in pets:
    pets.remove("cats")

print(pets) # It removes all the instances of "cats" from the list.


# Filling a dictionary with user input using a while loop.
# In this program, we'll ask the user to enter a name and a message and store them in a dictionary.
# We'll connect each response to the particular user and end the program if anyone enters an empty name or message.

responses = {}

while True:
    # Prompt for the user's name and response.
    name = input("What is your name? \n?")
    message = input("Enter any message:\n")

    # Store the response in the dictionary.
    responses[name] = message

    # If both name and message are blank, end the loop.
    if name == "" and message == "":
        break

# Here's what the responses dictionary looks like:
for name, message in responses.items():
    print(f"{name.title()} said: {message}")

print(responses)

# Exercises - While Loops:

sandwich_orders = ["bacon", "tuna", "veggie", "chicken","Pastrami", "Pastrami", "tuna", "Pastrami"]
finished_sandwiches = []

print("We have run out of Pastrami sandwiches.")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

print(f"\nThe only sandwiches we've got is: {sandwich_orders}")

while sandwich_orders:
    in_process = sandwich_orders.pop()
    print(f"Your {in_process.title()} sandwich is being prepared.")
    finished_sandwiches.append(in_process)

print("\nThe following sandwiches have been made:")
for sandwiches in finished_sandwiches:
    print(sandwiches.title())


# Exercise -3 : Dream Vacation

results = {}

active = True

while active:
    name = input("What is your name? \n")
    place = input("Where is your dream holiday destination? ")

    results[name] = place

    repeat = input("\nDo you want to continue. (yes/no)")
    if repeat == "no":
            active = False

# Here's the results of the survey.
for name, place in results.items():
    print(f"{name}'s dream holiday destination is: {place}. ")
