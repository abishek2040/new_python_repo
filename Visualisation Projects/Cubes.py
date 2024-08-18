# A number raised to the 3rd power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.

# Plotting the first 5 cubic numbers:
import matplotlib.pyplot as plt

# Generate data for cubic numbers
x_small = list(range(1, 6))           # First five numbers: [1, 2, 3, 4, 5]
y_small = [x**3 for x in x_small]     # Cubic numbers for first five numbers

x_large = list(range(1, 5001))        # First 5000 numbers: [1, 2, 3, ..., 5000]
y_large = [x**3 for x in x_large]     # Cubic numbers for first 5000 numbers

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))  # 2 rows, 1 column

# Plot the first five cubic numbers
ax1.scatter(x_small, y_small, c=y_small, cmap=plt.cm.Greens)
ax1.set_title('First Five Cubic Numbers')
ax1.set_xlabel('Number')
ax1.set_ylabel('Cubic Value')

# Plot the first 5000 cubic numbers
ax2.scatter(x_large, y_large, c=y_large, cmap=plt.cm.Blues)
ax2.set_title('First 5000 Cubic Numbers')
ax2.set_xlabel('Number')
ax2.set_ylabel('Cubic Value')

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig('cubes_colormap.png')

# Display the plots
plt.show()
