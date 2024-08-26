from eightdie import Dice
from plotly import  offline
from plotly.graph_objs import Bar, Layout

# Create two D8 dice.
die_1 = Dice()
die_2 = Dice()

# Roll the dice and store the results in a list.
results = []
for i in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)

# Analyze the results.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for i in range(2, max_results+1):
    frequency = results.count(i)
    frequencies.append(frequency)
print(frequencies)

# Visualize the results:

x_values = list(range(2, max_results+1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

# Set the chart title and axis labels.
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
