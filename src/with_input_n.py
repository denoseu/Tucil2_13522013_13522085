import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def draw_bezier_recursive(points, iterations):
    if len(points) == 2 or iterations == 0:
        xs, ys = zip(*points) # unpack points into x and y coordinates
        plt.plot(xs, ys, 'b-')
    else:
        new_points = []
        for i in range(len(points)-1):
            new_points.append(midpoint(points[i], points[i+1]))
        new_points = [points[0]] + new_points + [points[-1]]
        draw_bezier_recursive(new_points, iterations - 1)

# Input n titik
n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

# Input koordinat poin-poin
x_start, y_start = map(float, input("Masukan start point (x,y): ").split(","))
points = [(x_start, y_start)]

# Input control points
for i in range(n-2):
    x, y = map(float, input("Masukan control point {}: (x,y): ".format(i+1)).split(","))
    points.append((x, y))

x_end, y_end = map(float, input("Masukan end point (x,y): ").split(","))
points.append((x_end, y_end))

# Create animation frames
def animate(iteration):
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Bezier Curve Iteration {iteration}')
    ax.grid()
    ax.axis('equal')

    # Display points
    for i, point in enumerate(points):
        plt.plot(*point, 'ro')
        plt.text(point[0], point[1], f'P{i}')

    # Draw curve
    draw_bezier_recursive(points, iteration)

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Bezier Curve')
ax.grid()
ax.axis('equal')

# Create animation
iterations = int(input("Masukan banyak iterasi: "))
ani = FuncAnimation(fig, animate, frames=iterations+1, interval=350, repeat=False)

# Display animation
plt.draw()
plt.show()
