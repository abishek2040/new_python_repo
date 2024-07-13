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
