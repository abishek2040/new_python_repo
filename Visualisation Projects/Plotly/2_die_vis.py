from dietwo import Dice
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Dice()
die_2 = Dice(10)

# Make some rolls and store it in a list.
results = []
for i in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

# Configure the layout of the histogram:

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two Dice 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename='d2.html')