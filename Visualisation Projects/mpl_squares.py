# Plotting a simple line graph:

import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
cubes = [1, 8, 27, 64, 125]

fig, (ax,ay) = plt.subplots(2)
ax.plot(squares)
ay.plot(cubes)
plt.show()

