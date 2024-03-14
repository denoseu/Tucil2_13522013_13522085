import tkinter as tk
from tkinter import ttk
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

def start_animation():
    # Input koordinat poin-poin
    x_start, y_start = float(start_x_entry.get()), float(start_y_entry.get())
    points = [(x_start, y_start)]

    x, y = float(control_x_entry.get()), float(control_y_entry.get())
    points.append((x, y))

    x_end, y_end = float(end_x_entry.get()), float(end_y_entry.get())
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
    iterations = int(iterations_entry.get())
    ani = FuncAnimation(fig, animate, frames=iterations+1, interval=350, repeat=False)

    # Display animation
    plt.draw()
    plt.show()

# Create GUI
root = tk.Tk()
root.title("Bezier Curve Animation")

# Input widgets
start_label = ttk.Label(root, text="Start Point (x, y):")
start_label.grid(row=0, column=0, padx=5, pady=5)
start_x_entry = ttk.Entry(root)
start_x_entry.grid(row=0, column=1, padx=5, pady=5)
start_y_entry = ttk.Entry(root)
start_y_entry.grid(row=0, column=2, padx=5, pady=5)

control_label = ttk.Label(root, text="Control Point (x, y):")
control_label.grid(row=1, column=0, padx=5, pady=5)
control_x_entry = ttk.Entry(root)
control_x_entry.grid(row=1, column=1, padx=5, pady=5)
control_y_entry = ttk.Entry(root)
control_y_entry.grid(row=1, column=2, padx=5, pady=5)

end_label = ttk.Label(root, text="End Point (x, y):")
end_label.grid(row=2, column=0, padx=5, pady=5)
end_x_entry = ttk.Entry(root)
end_x_entry.grid(row=2, column=1, padx=5, pady=5)
end_y_entry = ttk.Entry(root)
end_y_entry.grid(row=2, column=2, padx=5, pady=5)

iterations_label = ttk.Label(root, text="Iterations:")
iterations_label.grid(row=3, column=0, padx=5, pady=5)
iterations_entry = ttk.Entry(root)
iterations_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

start_button = ttk.Button(root, text="Start Animation", command=start_animation)
start_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
