class User:
    """Modelling a general user object. """
    def __init__(self, first_name, last_name):
        """Initialize the parameters of the class. """
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Describe the user object."""
        print(f"\nThe user's name is: {self.first_name} {self.last_name}")

    def greet_user(self):
        """A method that describes the specific user."""
        print(f"Hello, Mr {self.last_name} how are you doing today. Great to see you out here.")