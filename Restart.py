print("Hello World, I am restarting Python after 6 months. ")
print("I will be combining this restart from a book as well as online courses. \nBy september, I will have better understanding of data science and machine learning. ")

# Here are some basic exercises to recap our previous journey

# Working with variables,
print(5+3)
num = 3
print(f"\nMy favourite number is: {num}")

# Data structure in python.
print("There are four  basic data structures in python, list, tuples, dictionaries & sets. \nLet's learn about Lists in python, one of the most basic and important data types in python. ")
# A list is a collection of items in a particluar order, either if it's a single item or a million, lists make it easier to load and extract data, here's some examples of lists in python.

# Try It Yourself

guest_List = ["George", "Michael", "Gandhi"]
print(f"\n{guest_List[2]}, is unable to attend the dinner, so the new list is: ")
print("I found a bigger dinner table, so the new list is: ")
guest_List.pop()
guest_List.append("Bobby")
guest_List.insert(0,"Abishek")
guest_List.insert(2, "Rooney")
guest_List.append("Beckham")

print("Apologies guys, the dinner table won't be delivered on time, so I'll have to remove some people from the list. ")
del guest_List[:]
for i in guest_List:
    print(f"\nHello, {i} I invite you for dinner at my place.")
print(guest_List)


# Sorting list in python:
Cars = ["Bmw", "Audi", "Bugatti", "Tesla", "Mercedes"]
Cars.sort() # This sort() method changes the order of the list permanently.
print(Cars)

# We can sort a list temporarily using the sorted() function:
Cars.reverse()
print(Cars)

# Using the len() function to find out the length of a list, or a data structure.
print(len(Cars))
print(f"The length of the cars list is : {len(Cars)}")
print()
print()
print()
# Final Exercise - Lists:

places = ["Marrakech", "Rome", "Geneva", "Yosemite", "Zambia", "Ladakh"]
print(places)

print(sorted(places))
print(places)
places.reverse()#
print(places)
places.sort()
print(places)