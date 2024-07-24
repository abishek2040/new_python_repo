"""When a class gets too lengthy, we can move the attributes and the methods, into a separate class"""

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """"Initialize the attributes of the car class. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Assigning a default value to an attribute.

    def describe_car(self):
        """A method that describes the car based on the information provided."""
        print(f"The car is {self.model} by {self.make} and was released in the year {self.year}.\n")

    def read_odometer(self):
        """This method just prints out the odometer reading."""
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """A method that updates the odometer reading. """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cannot roll back an odometer.")

    def increase_odometer(self, miles):
        """Increase the odometer value."""
        self.odometer_reading += miles

class Battery:
    """A class that describes the battery of a car."""
    def __init__(self, battery_size = 75):
        """Initialize the attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints the information about the battery."""
        print(f"The car has {self.battery_size}-KWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")



class Electric_car(Car):
    """Represents the aspects of a car, specific to electric values."""
    def __init__(self, make, model, year):
        """Initialize the aspects of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

car1 = Electric_car("Tesla", "Model-3", 2023)
car1.describe_car()
car1.battery.describe_battery()
car1.battery.get_range()