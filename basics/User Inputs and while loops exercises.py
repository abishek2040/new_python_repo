# TRY IT YOURSELF

# Pizza Toppings:
"""Write a loop that prompts a user to enter a series of pizza toppings until they enter 'quit' value.
As they enter each topping, print a message saying you'll add that topping to their pizza. """

prompt = "\nName the toppings you'd like on your pizza. "

toppings = []
topping = ""
while topping != "Quit":
    topping = input(prompt)

    if topping != "Quit":
        toppings.append(topping)
        print(f"\n{topping.title()} is added to your pizza")
    else:
        print("\nThank you for your order. \nYou've ordered a pizza with the following toppings:")
        for items in toppings:
            print(items)


# Movie Tickets:
age = int(input("How old are you? \n"))
if age < 3:
    print("You don't need to pay for the ticket. ")
elif age > 3 and age < 12:
    print("The ticket price is $10 for you.")
elif age <= 12:
    print("The ticket price for you is $15.")


