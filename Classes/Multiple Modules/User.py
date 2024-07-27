class User:
    """An attempt to model a user: """
    def __init__(self, first_name, last_name):
        """Initialize the attributes of the class."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Describe User"""
        print(f"\nThe user name is: {self.first_name} {self.last_name}")

    def greet_user(self):
        """A method that greets the user."""
        print(f"Hello, {self.first_name} {self.last_name} good to see you today.")