# Plotting a simple line graph:

import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
cubes = [1, 8, 27, 64, 125]

fig, (ax,ay) = plt.subplots(2)
ax.plot(squares)
ay.plot(cubes)
ax.plot(squares, linewidth=3)
ay.plot(cubes, linewidth=3)
ax.set_title("Squares", fontsize=13)
ax.set_xlabel("Value", fontsize=13)
ax.set_ylabel("Square of Value", fontsize=13)
ay.set_xlabel("Value", fontsize=13)
ay.set_ylabel("Cube of Value", fontsize=13)
ay.set_title("Cubes" , fontsize=13)

ax.tick_params(axis='both', labelsize=13)

plt.show()

