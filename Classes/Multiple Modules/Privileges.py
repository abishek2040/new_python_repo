from User import User
class Privileges:
    """A new class that holds the privileges for the admin user. """
    def __init__(self):
        """Initialize the attributes for this class."""
        self.privileges = ["Can Add Post", "Can Delete Post", "Can Add User", "Can Ban User"]

    def show_privileges(self):
        """A method that lists out all the privileges for the admin user."""
        print(f"\nHello you are an Admin & you have the following rights.")
        for actions in self.privileges:
            print(actions)

class Admin(User):
    """A subclass that inherits attributes and the methods from the User superclass."""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()