from threedie import Dice
from plotly.graph_objs import Bar, Layout
from plotly import offline

# creating three dice objects
dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice()

# Rolling the dies and storing the results in a list called results

results = []

for i in range(50000):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
    results.append(result)

# Analyzing the results

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
for i in range(3, max_result+1):
    frequency = results.count(i)
    frequencies.append(frequency)
print(frequencies)

# Visualizing the results
x_values = list(range(3, max_result+1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

# Configuring the Histogram:
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')