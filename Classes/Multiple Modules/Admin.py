class Admin(User):
    """A subclass that inherits attributes and the methods from the User superclass."""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()