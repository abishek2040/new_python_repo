# Last chapter, we learned about Lists, in this chapter we will see how to loop through lists using couple of lines of code.
# Loops are very effective and easy way to perfrom the same task over and over again using simple line of code, that makes your programs more readable and clean.

# As we go further into our python journey, we'll come across various types of loops, for loop, while loops and more. For & while are the most widely used loops in python.

# Here's an example of Loop in python.
name = ["Alice", "Bob", "Conan", "Daniel", "Elizabeth", "Frank"]
for i in name:
    print(i)
# Here using the for loop we can print all the items in the list (name) using just 2 lines of code, rather than printing them one by one.

# Doing more within a for loop.
print()
for i in name:
    print(f"Hello, {i} very nice to meet you. ")
    print("I am looking forward to knowing you. \n")
print("Thank you everyone for coming. \n")

# Errors: Indentation errors are one of the most common errors in python.

# TRY IT YOURSELF
pizza = ["Margarita", "Mushroom", "Neapolitan"]
for names in pizza:
    print(f"I like {names} pizza.")
print("I really love pizza. \n")

animals = ["Dog", "Cat", "Tiger", "Leopard", "Boar"]
for types in animals:
    print(f"A {types}, would make a great pet.")
print("All the above mentioned animals have 4 legs")

# Making Numerical Lists:
# There are many reasons or situations where we need to store a large list of numbers or numerical values, lists are an ideal way of storing numbers in python.

# The range() function in python. The range function in python makes it easier to generate a series of numbers. For example, if you wish to print out 1000 numbers, you can use the range() function.

for numbers in range(1,6):
    print(numbers)

numbers = list(range(1,11))
print(numbers) # This prints out list of numbers from 1 to 10
print()
# Making a list of first 20 even numbers.
even_numbers = list(range(0,20,2))
print(even_numbers)
print()
# Working with lists:
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)


# Simple statistics with  a list of numbers.
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))

# List comprehension:
# List comprehension is a style in which you can create the same list in a single line of code, It might be a bit hard first, but with a bit of practice it will be very handy.
# For examples

squares = [value ** 2 for value in range (1,11)]
print(squares) # List comprehensions are very helpful if you find yourself creating multiple lists, that might seem very repetitive.

# TRY IT YOURSELF.
# 1
for i in range(1,21):
    print(i)

#2.
numbers = list(range(1,1000001))
print(numbers)
print(min(numbers))
print(max(numbers))

odd_numbers = [value for value in range(1,20,2)]
print(odd_numbers)

#3. Make a multiple of 3 from 3 to 30, use a for loop to print the numbers in your list.
multiple = [numbers for numbers in range(3,30,3)]
print(multiple)

#4. Cubes: A number raised to the 3rd power is called a cube. For example the cube of 2 is written as 2**3 in python.

cube = [number**3 for number in range(1,11)]
print(cube)
print()
# Navigating through a list,
# Looping through a slice,
players = ["Charlie", "Aaron", "Kobe", "Marcus", "Bruno"]
print("Here are the 3 best players in my team: \n")
for player in players[2:]:
    print(player.lower())

# Copying a list:
# Often you would like to copy a list, and create a new one based on the other list, here's how we can copy or clone a list in python.
my_order = ["momo", "Pizza", "Burger", "Coke"]
friend_order = my_order[:]
print()
my_order.append("Salad")
friend_order.append("Chowmein")
print(my_order)
print(friend_order)


# TRY IT YOURSELF

# Exercisse - 1
random_list = ["Keys", "House", "Shoes", "Wallet", "Phone", "Pen", "Bottle", "Food"]
print("The first 3 item s in the list are: ")
print(random_list[0:4])
print("\nThe 3 items in the middle of the list are: ")
print(random_list[2:5])
print("\nThe last 3 items in the list are: ")
print(random_list[5:])


# Tuples: Tuples are also a data structure in python, they are basically exactly like lists, the only difference is: that tuples use parenthesis instead of square brackets. Once you define a tuple
# you can access individual elements by using each item's index just as you'd do for a list. One unique thing about tuples are that they are immutable, the items inside the tuple cannot be changed or replace unlike a list.
print()
print()

dimensions = (200,300)
print(dimensions[0])
print(dimensions[1])
print()
# Looping through all values in a tuple:
for numbers in dimensions:
    print(numbers)

# Once again, you cannot change the elements inside a tuple, you'll need to change the entire tuple, if you wish to change an element. for eg:

names = ("Abishek", "Barshana")
print(names)
names = ("Barshana", "Abishek")
print(names)

print("I will be a billionaire before march 10 2040.:)")