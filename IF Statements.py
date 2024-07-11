# Programming often involves examining a set of conditions and deciding what action to take based upon the given
# conditions. Here's a simple example of if statements in python.

cars = ["BMW", "Audi", "Rolls Royce", "Bugatti", "Mercedes", "Ferrari"]
for car in cars:
    if car == "Ferrari":
        print(car.upper())
    else:
        print(car.title())

# Conditional Tests: At the heart of every conditional statement is an expression that can be evaluated as True or False
# and is called a conditional test. Python uses the values True and False, to decide whether a code iin an if statement
# should be executed.
# If the conditional statement is true, python executes the code and if it is false, it ignores the code.

car = "bmw"
print(car == "bmw")  # This results to true.

# TRY IT YOURSELF - Simple if statements:

age = 20
if age < 18:
    print("You are not old enough to vote: ")
    print("Please come back once you turn 18\n")
else:
    print("You are old enough to vote. \n")

# IF else Statements: - TRY IT YOURSELF

# Example - 1
alien_color = ["green", "yellow", "red"]
for colors in alien_color:
    if colors == "green":
        print("You earn 5 points")
    else:
        pass

# Example - 2
for colors in alien_color:
    if colors == "green":
        print("You earned 5 points.")
    elif colors == "yellow":
        print("You earned 10 points")
    else:
        print("you earned 4 points")

print("\nThis is an if-elif block\n")

# Example - 3 Alien colors 3.
for colors in alien_color:
    if colors == "green":
        print("You earned 5 points")
    elif colors == "yellow":
        print("You earned 10 points")
    elif colors == "red":
        print("You earned 20 points")


print("\nStages of life\n")
# Example  - 4 : Stages of Life
age = 2
if age < 2:
    print("You are a baby")#
elif age >= 2 and age <4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >=13 and age <20:
    print("You are a teenager")
elif age>= 20 and age <65:
    print("You are an adult")
elif age >=65:
    print("You are an elder")

# EXAMPLE - 5: FAVORITE FRUIT
fruits = ["Apple", "Mango", "Banana", "Cherry", "Raspberry", "Blueberry", "Papaya", "Guava", "Orange"]
for fruit in fruits:
    if fruit == "Apple":
        print(f"\nYou really like {fruit}.")
    elif fruit == "Mango":
        print(f"\nYou really like {fruit}")
    else:
        print(f"\n{fruit} is okay.")


# Example - 6:
usernames = ["Admin", "Temp-user", "Manager", "Assistant", "Director"]
for names in usernames:
    if names == "Admin":
        print(f"\nHello, {names} here's your summary for today.")
    else:
        print(f"\nHow are you {names}")


# Example - 7 : Ordinal Numbers:
print("\nThis is a simple program to print out the ordinal numbers. ")
numbers = [1,2,3,4,5,6,7,8,9]
for nums in numbers:
    if nums == 1:
        print("1st")
    elif nums == 2:
        print("2nd")
    elif nums == 3:
        print("3rd")
    else:
        print(f"{nums}th")
