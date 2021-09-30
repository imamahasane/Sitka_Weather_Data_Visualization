
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax, plt.plot(input_values, squares, linewidth = 3)
#ax.plot(squares, linewidth = 3)

# Set chart title and label axes
ax.set_title("Square Number", fontsize = 24)
ax.set_xlabel("Valu", fontsize=14)
ax.set_ylabel("Square of Valu", fontsize = 14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize = 14)

plt.show()
