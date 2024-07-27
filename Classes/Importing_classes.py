"""As we add more functionality to our code, it becomes very long and diffcult to manage, even while using inheritance
properly. To help, python lets you store classes in modules and then import the classes you need to your main program."""

# Here we are going to import the User class from the file named User.py and call one of the methods of the class.

from User import User

user1 = User("Abishek","Phuyal")
user1.describe_user()
user1.greet_user() # Here we ran the 15 line class file using just 2 lines, thus importing is very useful to manage your code.

"""There are various different ways to import a class or a whole module in python for eg: 
 * Import the whole module: import "module_name"
 * Import a single Class: from "module_name" import "class_name"
 * Importing all classes in a module: from "module_name" import *
 * import multiple classes in a module: from "module_name" import "class_name", "class_name2"...
 * Using Aliases: from "module_name" import "Class_name" as alias 
 """



# TRY IT YOURSELF:

from Classes import Restaurant
restautant1 = Restaurant("Spice69", "Spicy")
restautant1.describe_restaurant()

