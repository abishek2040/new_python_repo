def get_name(first, last, middle= ""):
    """A function that takes in first and last name and provides a neatly formatted output."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# To check the above function works, we create a program that uses the function .

