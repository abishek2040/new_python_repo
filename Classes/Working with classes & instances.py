# Working with classes and instances:
"""You can use classes to represent many real-world situations. Once you write a class, you'll spend most of your time
working with instances created from that class. One of the first tasks you'll want to do is modify the attributes
associated with a particular instance. You can modify the attributes of an instance directly or write methods that
update attributes in specific ways. """


# The Car Class: Let's write a new class representing a car. Our class will store information about the kind of car
# we're working with, and it will have a method tha summarizes this information.

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make =  make
        self.model = model
        self.year = year

    def describe(self):
        """A method that describes the properties of the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

car_1 = Car("Audi", "E-tron", 2024)
print(car_1.describe())

# To make the class more interesting, let's add an attribute that changes over time. We'll add an attribute that stores
# the car's milage.

# Assigning a default value:
class Carr:
    """A car class with one default value."""
    def __init__(self, make, model, year):
        """Initialize the attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def describe_car(self):
        """Describe the car."""
        long_name = f"{self.year}, {self.model}, {self.make}"
        return long_name

    def read_odometer(self):
        """Method that prints the odometer reading."""
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, milage): # Modifying an attribute through a method.
        """A method to update the odometer's value."""
        self.odometer = milage
        print(f"New odometer Reading:{self.odometer}")

    def increment(self, miles):
        """Incrementing the attribute's value through an attribute."""
        self.odometer += miles
        print(f"The new odometer value is: {self.odometer}")

car3 = Carr("Tesla","Model 3 ", 2024)
print(car3.describe_car())
car3.read_odometer()

# Modifying Attribute's value directly, an attributes values can be modified in multiple different ways:
# Modifying an Attribute's value directly: car3.odometer = 100 (Car3 is the instance, odometer is the parameter, and we
# modify the value directly.
car3.odometer = 100
car3.read_odometer() # It prints out the odometer reading is 100.

car3.update_odometer(250) # Calling the method to update the value.

# Incrementing an attribute's value through a method.
car3.read_odometer()
car3.increment(100)

# 24-07-2024: TRY IT YOURSELF

# 1.
