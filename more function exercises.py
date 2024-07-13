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
# when you pass a list to a function, the function can modify the passed list and it will be permanent, allowing you
# to work efficiently even when you're dealing with large amount of data.

# Here's a simple example of modifying a list without using functions, we'll do it again using functions later.
# a 3d printing company gets orders to print and stores it in a list, it moves the orders to completed list once it
# has been printed.

orders_received = ["Ball","Pen","Mouse","Computer","Keyboard","Bottle"]
completed = []

while orders_received:
    current_orders = orders_received.pop()
    print(f"\nPrinting {current_orders.title()}")
    completed.append(current_orders)
print(completed)
print(orders_received)
for orders in completed:
    print(orders)

# We are going to Re-organize this code, by using functions.

def modify_lists(orders, completed_orders):
    """This function takes a list as an argument, and transfer all the elements to the other list. """
    while orders:
        current_orders = orders.pop()
        print(f"Printing: {current_orders.title()}")
        completed_orders.append(current_orders)

def show_completed(completed_orders):
    """This function displays all the elements from the completed_orders list. """
    print(f"\nThe following models have printed. ")
    for corders in completed_orders:
        print(f"{corders}\n")

orders = ["Ball","Pen","Book","Watch","Mouse","Phone"]
completed_orders = []

modify_lists(orders, completed_orders)
show_completed(completed_orders)



# Passing lists to a function: TRY IT YOURSELF:

# 1. Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which
# prints each text message.

messages = ["Hey", "hi", "hello","Gooday","Howdy","Namaste"]

def show_message(messages):
    """A function that takes in a list as an input and prints out the elements of the list."""
    for message in messages:
        print(message)

show_message(messages)


# Exercise - 2: Sending Messages - Move the messages to a different list:

def move_messages(messages, sent_messages):
    """Takes 2 lists as input and moves the messages from the messages argument to the sent_messages list."""
    while messages:
        current_message = messages.pop()
        print(f"\nMoving Message: {current_message}")
        sent_messages.append(current_message)

def print_messages(sent_messages):
    """Prints out the moved messages."""
    for message in sent_messages:
        print(message)

messages = ["Hey", "hi", "hello","Gooday","Howdy","Namaste"]
sent_messages = []

move_messages(messages, sent_messages)
print_messages(sent_messages)

print(messages)
print(sent_messages)


# Exercise - 3: Not permanently changing the list - Making a copy of the original list without modifying it.

def move_messages(messages, sent_messages):
    """Takes 2 lists as input and moves the messages from the messages argument to the sent_messages list."""
    while messages:
        current_message = messages.pop()
        print(f"\nMoving Message: {current_message}")
        sent_messages.append(current_message)

def print_messages(sent_messages):
    """Prints out the moved messages."""
    for message in sent_messages:
        print(message)

messages = ["Hey", "hi", "hello","Gooday","Howdy","Namaste"]
sent_messages = []

move_messages(messages[:], sent_messages)
print_messages(sent_messages[])

print(messages)
print(sent_messages)

