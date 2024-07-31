# TRY IT YOURSELF:

# 1. Rental Cars:
car = input("What type of car are you looking to rent? :\n")
print(f"Let me see if I can find you a {car}.")

#2. Restaurant Seating:

people = int(input("How many people are in your group? "))
if people <= 8:
    print("Thank you, your table is ready. ")
else:
    print("You'll have to wait for the bigger table. ")

# 3. Multiples of 10:
mult = int(input("Enter a number: "))
if mult % 10 == 0:
    print(f"{mult}, is a multiple of 10.")
else:
    print(f"{mult}, is not a multiple of 10. a")


# Introducing While Loops:

# The for loop takes a collection of items and executes a block of code once for each item in the collection.
# In contrast, the while loop runs as long as, or while a certain condition is true.

# Example of while loop:

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1


# Example -2 While Loops: Letting users when to quit:
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'Quit' to end the program."

message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)


# Using break to exit a loop:
# To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any
# conditional test, use the break statement. The break statement directs the flow of your program.

# For example:

prompt = "\nPlease enter the name of the city you visited"
prompt += "\n(Enter 'Quit' when you are finished."

active = True
while active:
    city = input(prompt)
    if city == "Quit":
        break
    else:
        print(f"\nI'd love to go to {city.title()}.")


# Using Continue in a loop:
# Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement
# to return to the beginning of the loop based on the result of a conditional test.
# For example:

current_number = 0
while current_number <10:
    current_number += 1
    if current_number %2 == 0:
        continue
    print(current_number)

    