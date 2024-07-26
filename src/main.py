import matplotlib.pyplot as plt

# Create a simple 5x5 grid
fig, ax = plt.subplots(figsize=(5, 5))

# Draw the grid lines
for x in range(6):
    ax.axhline(x, color='black', linewidth=1)

# Draw the vertical lines only extending to 1/5 the length
# for y in range(6):
    # ax.plot([y, y], [0, 1], color='black', linewidth=1)
ax.plot([2, 2,2], [2, 1,0], color='black', linewidth=1)

# Set the limits and aspect ratio
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_aspect('equal')

# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])

plt.show()
