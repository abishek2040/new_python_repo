import matplotlib.pyplot as plt

from RandomWalks import RandomWalk

# Make a Random Walk
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk
plt.style.use('classic')
fig,ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_title("Random Walk", fontsize=24, c="Green")
ax.set_xlabel("X Values", fontsize=14, c="Red")
ax.set_ylabel("Y Values", fontsize=14, c="Red")
ax.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('RandomWalk.png', bbox_inches='tight')
plt.show()