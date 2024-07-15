"""Sometimes, we might not know ahead of time, how many arguments a function needs to accept. fortunately python allows
    to pass arbitrary number of statements from the calling statement.
    For Example:"""

def make_pizza(*toppings):
    """Accepts an arbitrary argument and prints it out."""
    print(f"\nMaking the best pizza with the following toppings: ")
    for ingredients in toppings:
        print(ingredients)

make_pizza("Cheese")
make_pizza("Pineapple","Ham","Chicken")


# Using Arbitrary Keyword Arguments:
# sometimes you'll want to accept an arbitrary number of arguments, but you won't know ahead of time what kind of info,
# will be passed to the function, in this case you can pass as many key-value pairs as the function requires.

# for example: Building User Profiles Functions

def build_profiles(first, last, **user_info):
    """Building a dictionary about a user."""
    user_info["First Name"] = first
    user_info["Last Name"] = last
    return user_info

user_profile = build_profiles("Abishek","Phuyal", location = "London", Age = 22)
print(user_profile)


# TRY IT YOURSELF:

def make_sandwich(*filling):
    """A function that asks for the filling on a sandwich and prints. """
    for items in filling:
        print(f"Adding {items} to your sandwich\n")
make_sandwich("Lettuce","Cheese","Chicken")
make_sandwich("Tuna","Onion","Cheese")
make_sandwich("Chicken","Sweet corn")


# User profiles:
def user(first_name, last_name, **info):
    """Build a user profile using arbitrary kwargs"""
    info["first name"] = first_name
    info["last_name"] = last_name
    return info

captain = user("Bruno", "Fernandes", Nationality="Portugal", Age = 26)
print(captain)


# 3. Cars:

def cars(manufacturer, model_name, **misc):
    """Car info - function """
    misc["Manufacturer"] = manufacturer
    misc["Model Name"] = model_name
    return misc

japan = cars("Toyota","Prius", Color="White", Purpose = "Uber")
print(japan)
Italy = cars("Ferrari", "Spyder", Color = "Black", Purpose= "Sport")
print(Italy)
