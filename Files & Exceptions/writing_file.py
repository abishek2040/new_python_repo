# TRY IT YOURSELF:
# Exercise - 1:
name = input("Hello Sir, what is your name. ")

with open("Guest.txt", "a") as guest:
    guest.write(f"{name}\n")


# Exercise - 2:
print("This is another program. ")
while True:
    name = input("What is your name, your name will be recorded on the guest book: \nEnter Q to Quit the program. ")
    with open("guest_book.txt", "a") as gb:
        gb.write(f"{name}\n")
    if name.lower() == "q":
        break
print("Your visit has been recorded.")

# Exercise - 3: Programming Poll:
while True:
    language = input("Enter your favorite programming language. ")
    if language == "Q":
        break
    else:
        with open("Programming.py", "a") as pg:
            pg.write(f"{language}\n")
            print(pg)

