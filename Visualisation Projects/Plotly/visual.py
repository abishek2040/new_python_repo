# Analyzing and visualizing the result of the Analysis from the Dice class.

from Die import Dice
from plotly import offline
from plotly.graph_objs import Bar, Layout

die = Dice() # Creating an object from the class Dice.

# Make some rolls and store the result in a list called results.

results = []
for i in range(10000):
    result = die.roll()
    results.append(result)


# Analyzing the results and counting the number of occurrences of each value.
frequencies = []
for i in range(1, die.num_sides+1):
    frequency =  results.count(i)
    frequencies.append(frequency)
print(frequencies)

# Creating the Histogram
x_values = list(range(1, die.num_sides+1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

# Configuring the layout and adding final touches:
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one Dice 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout':my_layout}, filename='1000.html')