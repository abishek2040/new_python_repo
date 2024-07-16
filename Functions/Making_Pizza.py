import pizza # Imports the module pizza, that has a function to make pizzas.

pizza.make_pizza("Large", "Cheese","Chicken","Ham")
pizza.make_pizza("13", "Ham","Olive","Pineapple")

# To call a function from an imported module, we enter the name of the imported module, pizza in this case, followed
# by the name of the function make_pizza(), separated by dot.

# module_name.function_name() - To call a function from an imported module.

# You can either import the whole module or just import some specific functions from the module.
"""
1. To import the whole module and all functions - we do: "import module_name
2. To import a specific function within the module we do: from module_name import function_name
3. Give an alias to a function: from module_name import function_name as fn (fn) to shorten the name. 
4. give the whole module an alias: import module_name as mn (mn is the alias given to the module in this case.)
5. To import all functions in a module - we do: from module_name import *
"""

# Modules help programmers to style their code and make it more readable, hiding things at the background.
# Modules make it easier to share the code to other programmers.
