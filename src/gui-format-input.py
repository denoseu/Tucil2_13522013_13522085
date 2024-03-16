import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class BezierAnimationGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bezier Curve Animation")
        self.geometry("800x600")

        self.canvas = tk.Canvas(self, width=800, height=500)
        self.canvas.pack()

        self.start_button = tk.Button(self, text="Start Animation", command=self.start_animation)
        self.start_button.pack()

        self.iterations_entry = tk.Entry(self)
        self.iterations_entry.pack()
        self.iterations_entry.insert(0, "Enter number of iterations")

    def midpoint(self, point1, point2):
        return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

    def draw_bezier_recursive(self, points, iterations):
        if len(points) == 2 or iterations == 0:
            xs, ys = zip(*points)  # unpack points into x and y coordinates
            self.canvas.create_line(xs, ys, fill='blue')
        else:
            new_points = [points[0]]
            for i in range(len(points) - 1):
                new_points.append(self.midpoint(points[i], points[i + 1]))
            new_points.append(points[-1])
            self.draw_bezier_recursive(new_points, iterations - 1)

    def animate(self, iteration):
        self.canvas.delete("all")
        self.canvas.create_text(400, 530, text=f'Bezier Curve Iteration {iteration}', font=("Arial", 16), anchor="center")
        self.canvas.create_text(400, 550, text=f'Iterations: {self.iterations}', font=("Arial", 12), anchor="center")

        # Display points
        for i, point in enumerate(self.points):
            self.canvas.create_oval(point[0] - 3, point[1] - 3, point[0] + 3, point[1] + 3, fill="red")
            self.canvas.create_text(point[0] + 10, point[1] - 10, text=f'P{i}', font=("Arial", 10), anchor="nw")

        # Draw curve
        self.draw_bezier_recursive(self.points, iteration)

    def start_animation(self):
        self.iterations = int(self.iterations_entry.get())
        self.points = []

        # Input coordinate points
        x_start, y_start = map(float, simpledialog.askstring("Input", "Enter start point (x,y): ").split(","))
        self.points.append((x_start, y_start))

        x, y = map(float, simpledialog.askstring("Input", "Enter control point (x,y): ").split(","))
        self.points.append((x, y))

        x_end, y_end = map(float, simpledialog.askstring("Input", "Enter end point (x,y): ").split(","))
        self.points.append((x_end, y_end))

        # Initialize plot
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('Bezier Curve')
        self.ax.grid()
        self.ax.axis('equal')

        # Create animation
        self.ani = FuncAnimation(self.fig, self.animate, frames=self.iterations + 1, interval=350, repeat=False)

        # Display animation
        plt.show()

if __name__ == "__main__":
    app = BezierAnimationGUI()
    app.mainloop()
