# storing your functions in modules:
# Let's create a module that contains the module, make_pizza()

def make_pizza(size, *toppings):
    """A module that takes 1 fixed argument size and another arbitrary keyword argument toppings. """
    print(f"Making a {size} size pizza with the following toppings: \n")
    for topping in toppings:
        print(topping)

