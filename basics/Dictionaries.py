# Dictionaries are one of the most important data structures in python programming.
# They can store almost infinite amount of data within it.

# Here's a simple dictionary:
user_1 = {
    "First Name":"Abishek",
    "Last Name" : "Phuyal",
    "Age":22,
}

print(user_1["Age"]) # Printing the age, we can navigate through the dictionaries using the key.

#Dictionaries are dynamic structures, thus they can be modified unlike tuples, here's how to modify dictionaries.

user_1["Height"] = 5.5
user_1["Weight"] = 62
print(user_1)

# Another example of working with dictionaries:
alien_0 = {
    "x-position":0,
    "y-position":25,
    "Speed":"medium",
}

if alien_0["Speed"] == "slow":
    x_increment =1
elif alien_0["Speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
# The new position of the alien is the x_increment + old position
alien_0["x-position"] = alien_0["x-position"] + x_increment
print(f"\nThe new Position: {alien_0['x-position']}")

# Favorite programming language:

programming_Language = {
    "Jen":"c",
    "Abishek":"Python",
    "Sarbesh":"Java",
    "Sudarshan":"Python",
    "Pramish":"C++",
}

for name, languages in programming_Language.items():
    print(f"\n{name}'s favorite programming language is: {languages}.")

print()

for name in sorted(programming_Language.keys()):
    print(name)

print()

for languages in set(programming_Language.values()): # Set is a collection in python, in which all values must be unique
    print(languages)


# TRY IT YOURSELF:

rivers = {
    "Nile":"Egypt",
    "Thames":"England",
    "Amazon":"Brazil",
    "Mississippi":"Usa",
    "Ganga":"India",
    "Gandaki":"Nepal",
}

for river,country in rivers.items():
    print(f"\nThe river {river} runs through {country}.")

print("\nThe list of rivers:")
for river in rivers.keys():
    print(river)

print("\nThe list of countries: ")
for countries in rivers.values():
    print(countries)

print()
names_left = ["Sumit", "Abishek", "Pramish", "Sudarshan", "Sarbesh", "Chirag", "Abhaya"]
for names in names_left:
    if names not in programming_Language.keys():
        print(f"{names}, you need to complete the poll.\n")
    else:
        print(f"{names} Thanks for completing the poll. \n")


# A list of dictionaries:
# Nesting: sometimes you'll want to store multiple dictionaries inside a list, or a list of items as a value
# in a dictionary, which is called nesting.

# Here's a simple example of list of dictionaries:
user_2 = {"First Name":"Sudarshan","Last Name":"Bastola", "Age":23}
user_3 = {"First Name":"Sumit","Last Name":"Gyawali", "Age":22}
user_4 = {"First Name":"Pramish","Last Name":"Kapair", "Age":23}

names = [user_2,user_3,user_4] # Storing the dictionaries in the list "Names"
for name in names:
    print(name)


# List in a dictionary: For example:

pizza = {
    "Crust":"thick",
    "Toppings":["Mushrooms","Sausages","Cheese"]
}
# Summarize the order:

print(f"\nYou've ordered a {pizza['Crust']} crust pizza with the following toppings:")
for topping in pizza["Toppings"]:
    print(topping)



# A dictionary inside a dictionary:

users = {
    "aeinstein":{
        "first":"Albert",
        "last":"Einstein",
        "Location":"Princeton"
    },

    "mcurie":{
        "first":"Marie",
        "last":"Curie",
        "Location":"Paris",
    },

    "wrooney":{
        "first":"Wayne",
        "last":"Rooney",
        "Location":"Liverpool"
    }
}

for name,user_info in users.items():
    print(f"\nUsername: {name}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['Location']}"

    print(full_name)
    print(location)



# TRY IT YOURSELF - Cities:

cities = {
    "London":{
        "Country":"England",
        "Population":"10 Million",
        "Language":"English",
        "Mayor":"Sadik Khan",
    },

    "Kathmandu":{
        "Country":"Nepal",
        "Population":"1 Million",
        "Language":"Nepali",
        "Mayor":"Balen Shah",
    },

    "New York":{
        "Country":"USA",
        "Population":"8 Million",
        "Language":"English",
        "Mayor":"Eric Adams",
    },

    "Madrid":{
        "Country":"Spain",
        "Population": "3 Million",
        "Language":"Spanish",
        "Mayor":"Jorge Silva",
    },
}

for city,info in cities.items():
    print(f"\nHere's some facts about {city}")
    print(info["Country"])
    print(info["Population"])
    print(info["Language"])
    print(info["Mayor"])























