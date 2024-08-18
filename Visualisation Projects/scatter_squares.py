# Using scatter() to plot and style the individual points.
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax =plt.subplots()
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
ax.scatter(x,y, s=100)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()