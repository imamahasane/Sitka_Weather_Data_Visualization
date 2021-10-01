import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize= (15, 9))
    ax.scatter(rw.x_values, rw.y_values, s = 15)

    point_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_number, cmap=plt.cm.Blues, edgecolors='none', s=15)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

