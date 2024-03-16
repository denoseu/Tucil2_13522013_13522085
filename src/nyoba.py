import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os, sys
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

##### TKINTER GUI #####
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return ImageTk.PhotoImage(img)

# Function to load an image with transparency and resize it
def load_image_transparent(image_path, width, height):
    img = Image.open(image_path).resize((width, height), Image.NEAREST)
    return ImageTk.PhotoImage(img)

##### TKINTER GUI #####

root = tk.Tk()
root.title("Bezier Curve Maker")
root.geometry("850x768")

# Create Canvas
canvas = tk.Canvas(root, width=850, height=768)
canvas.pack(fill="both", expand=True)

# Background Image
background_image = ImageTk.PhotoImage(file=resource_path("assets/page-1/Dashboard.png"))
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Header Image
header_image = load_image_transparent(resource_path("assets/page-1/header.png"), 920, 46)
canvas.create_image(425, 28, image=header_image, anchor="center")  # Adjust position as needed

# Logo Image
logo_image = load_image_transparent(resource_path("assets/page-1/logo.png"), 920, 250)
canvas.create_image(425, 175, image=logo_image, anchor="center") 

# Control Image
control_image = load_image_transparent(resource_path("assets/page-1/control.png"), 80, 20)
canvas.create_image(60, 70, image=control_image, anchor="center")  # Adjust position as needed

# Prevent images from being garbage collected
canvas.images = [background_image, header_image, logo_image, control_image]


# Style configuration
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12), background='#f8f8f2')
style.configure('TEntry', font=('Helvetica', 12), fieldbackground='#f8f8f2')

# Entry and Label Frames
entry_frame = tk.Frame(root, bg='#f8f8f2', bd=5)
entry_frame.place(relx=0.5, rely=0.35, relwidth=0.85, relheight=0.6, anchor='n')

# Input widgets (add these within the entry_frame)
start_label = ttk.Label(entry_frame, text="Start Point:")
start_label.grid(row=0, column=0, padx=5, pady=5)
start_x_entry = ttk.Entry(entry_frame)
start_x_entry.grid(row=0, column=1, padx=5, pady=5)
start_y_entry = ttk.Entry(entry_frame)
start_y_entry.grid(row=0, column=2, padx=5, pady=5)

control_label = ttk.Label(entry_frame, text="Control Point:")
control_label.grid(row=1, column=0, padx=5, pady=5)
control_x_entry = ttk.Entry(entry_frame)
control_x_entry.grid(row=1, column=1, padx=5, pady=5)
control_y_entry = ttk.Entry(entry_frame)
control_y_entry.grid(row=1, column=2, padx=5, pady=5)

end_label = ttk.Label(entry_frame, text="End Point:")
end_label.grid(row=2, column=0, padx=5, pady=5)
end_x_entry = ttk.Entry(entry_frame)
end_x_entry.grid(row=2, column=1, padx=5, pady=5)
end_y_entry = ttk.Entry(entry_frame)
end_y_entry.grid(row=2, column=2, padx=5, pady=5)

iterations_label = ttk.Label(entry_frame, text="Iterate:")
iterations_label.grid(row=3, column=0, padx=5, pady=5)
iterations_entry = ttk.Entry(entry_frame)
iterations_entry.grid(row=3, column=1, padx=5, pady=5)

start_button = ttk.Button(entry_frame, text="Generate Curve", command=start_animation)
start_button.grid(row=4, column=0, columnspan=3, padx=5, pady=20)

root.mainloop()
