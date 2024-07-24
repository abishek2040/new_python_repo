""" You don't always have to start from scratch to write a class, If the class you're writing is a specialized version
of another class you wrote, you can use inheritance. When one class inherits from another, it takes on the attributes
and methods from the inherited class. The original class is called a parent class and the new class is called a child
class. The child can inherit any or all classes of the parent class and is also free to define new attributes which are
specific to that class. """

""" Here's an example of how inheritance works in python, we are going to create a class named Car which will be the 
parent class and will create another class named Electric_Car, which will be the child class and will inherit attributes 
and the method from the original Car class. """

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


class Electric_car(Car):
    """Represents the aspects of a car, specific to electric values."""
    def __init__(self, make, model, year):
        """Initialize the aspects of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75
        # We can also add any new specific attributes to the child class. Here we'll add an attribute named battery size

    def describe_battery(self):
        """A method that prints out information about the battery."""
        print(f"The battery size on this car is: {self.battery_size} kWh.")

    # We can also override any attributes or methods that have been inherited from the parent class, for example:
    def fill_gas(self):
        """Overriding the method that was inherited from the superclass, to override the method, you'll need to create
        a method with the same name on the subclass."""
        print("Electric cars doesn't need a gas tank you imbecile. ")


car1 = Car("Tesla", "Model 3", 2020)
car1.describe_car()

car2 = Electric_car("Audi", "E-tron", 2024)
car2.describe_car()
car2.describe_battery()
car2.fill_gas()


# INSTANCES AS ATTRIBUTES:
"""When modelling something from the real world in code, you may find that you're adding more and more detail to a class
you're going to find that you have a growing list of attributes and methods, and that your files are becoming very
lengthy. In this case you might realize that a part of one class can be written as a separate class.

The Electric car class is getting longer, so we can move the details about the battery into a separate class
named battery. Then we can use a Battery instance as an attribute in the Electric_car class."""


