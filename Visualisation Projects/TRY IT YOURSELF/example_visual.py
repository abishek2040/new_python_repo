# visualising the path

import matplotlib.pyplot as plt
from MolecularMotion import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
plt.plot(rw.x_values, rw.y_values, linewidth=2)

# Set title:
ax.set_title("Random Walk", fontsize=24, c="Green")
ax.set_xlabel("X Values", fontsize=14, c="Red")
ax.set_ylabel("Y Values", fontsize=14, c="Red")

plt.plot(0,0, c="red", linewidth=150)
plt.plot(rw.x_values[-1], rw.y_values[-1], c="green", linewidth=100)
plt.savefig('RandomWalk.png', bbox_inches='tight')
plt.show()