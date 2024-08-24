import matplotlib.pyplot as plt

from RandomWalks import RandomWalk

while True:
# Make a Random Walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig,ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values,s=10, edgecolors="none", c=point_numbers,cmap=plt.cm.Blues)

    #Emphasize the first and the last points to create an appealing visualisation.

    ax.scatter(0, 0, c='green', edgecolors='none', s=45)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], edgecolors='none', c='red', s=45)
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.set_title("Random Walk", fontsize=24, c="Green")
    ax.set_xlabel("X Values", fontsize=14, c="Red")
    ax.set_ylabel("Y Values", fontsize=14, c="Red")
    ax.tick_params(axis='both', which='major', labelsize=14)
    plt.savefig('RandomWalk.png', bbox_inches='tight')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        print("Thank you for generating the walks with us: ")
        break

