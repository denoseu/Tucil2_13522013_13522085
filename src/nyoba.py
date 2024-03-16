import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os, sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def draw_bezier_recursive(points, iterations):
    if len(points) == 2 or iterations == 0:
        xs, ys = zip(*points)
        plt.plot(xs, ys, 'b-')
    else:
        new_points = []
        for i in range(len(points)-1):
            new_points.append(midpoint(points[i], points[i+1]))
        new_points = [points[0]] + new_points + [points[-1]]
        draw_bezier_recursive(new_points, iterations - 1)

def start_animation():
    # Ensure global declaration if variables are used outside function scope
    global ani  # Add this if 'ani' might be referenced elsewhere or to prevent garbage collection

    update_point_text()
    x_start, y_start = float(start_x_entry.get()), float(start_y_entry.get())
    points = [(x_start, y_start)]

    x, y = float(control_x_entry.get()), float(control_y_entry.get())
    points.append((x, y))

    x_end, y_end = float(end_x_entry.get()), float(end_y_entry.get())
    points.append((x_end, y_end))

    def animate(iteration):
        ax.clear()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(f'Bezier Curve Iteration {iteration}')
        ax.grid()
        ax.axis('equal')

        for i, point in enumerate(points):
            plt.plot(*point, 'ro')
            plt.text(point[0], point[1], f'P{i}')

        draw_bezier_recursive(points, iteration)

    fig, ax = plt.subplots()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Bezier Curve')
    ax.grid()
    ax.axis('equal')

    iterations = int(iterations_entry.get())
    ani = FuncAnimation(fig, animate, frames=iterations+1, interval=350, repeat=False)

    canvas2.fig_photo = draw_figure(canvas2_animation, fig)

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

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

# Function to switch notebook tab
def switch_tab(tab_index):
    notebook.select(tab_index)

def update_point_text():
    # Fetch the points
    x_start, y_start = start_x_entry.get(), start_y_entry.get()
    x_control, y_control = control_x_entry.get(), control_y_entry.get()
    x_end, y_end = end_x_entry.get(), end_y_entry.get()
    
    # Coordinates for the text on canvas2, adjust as necessary for your layout
    text_x = 668  # Horizontal center
    start_y = 300  # Adjust this value to place the text above the result image
    line_height = 35  # Adjust based on your font size for vertical spacing
    
    # Create or update the text
    # This example assumes you're creating new text every time. You could also update existing text.
    canvas2.create_text(text_x, start_y, text=f"{x_start}            {y_start}", fill="black", anchor="center")
    canvas2.create_text(text_x, start_y + line_height, text=f"{x_control}            {y_control}", fill="black", anchor="center")
    canvas2.create_text(text_x, start_y + 2 * line_height, text=f"{x_end}            {y_end}", fill="black", anchor="center")

# TKINTER GUI
root = tk.Tk()
root.title("Bezier Curve Maker")
root.geometry("850x768")

# Create Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Page 1
page1 = ttk.Frame(notebook)
notebook.add(page1, text='Input')

# Page 2
page2 = ttk.Frame(notebook)
notebook.add(page2, text='Animation')

# Create Canvas
canvas1 = tk.Canvas(page1, width=850, height=768)
canvas1.pack(fill="both", expand=True)

# Background Image for Page 1
background_image = ImageTk.PhotoImage(file=resource_path("assets/page-1/Dashboard.png"))
canvas1.create_image(0, 0, image=background_image, anchor="nw")

# Header Image for Page 1
header_image = load_image_transparent(resource_path("assets/page-1/header.png"), 920, 46)
canvas1.create_image(425, 28, image=header_image, anchor="center") 

# Logo Image for Page 1
logo_image = load_image_transparent(resource_path("assets/page-1/logo.png"), 920, 250)
canvas1.create_image(425, 175, image=logo_image, anchor="center") 

# Control Image for Page 1
control_image = load_image_transparent(resource_path("assets/page-1/control.png"), 80, 20)
canvas1.create_image(60, 70, image=control_image, anchor="center")

# Text Image for Page 1
text_image = load_image_transparent(resource_path("assets/page-1/title.png"), 630, 50)
canvas1.create_image(410, 160, image=text_image, anchor="center")

canvas1.images = [background_image, header_image, logo_image, control_image, text_image]

# Entry and Label Frames for Page 1
entry_frame = tk.Frame(page1, bg='#dabecb', bd=5)
entry_frame.place(relx=0.5, rely=0.45, relwidth=0.85, relheight=0.5, anchor='n')

# Input widgets (add these within the entry_frame)
start_label = ttk.Label(entry_frame, text="Start Point:", font=('Arial', 18))
start_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
start_x_entry = ttk.Entry(entry_frame, font=('Arial', 18))
start_x_entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky='we')
start_y_entry = ttk.Entry(entry_frame, font=('Arial', 18))
start_y_entry.grid(row=0, column=2, padx=5, pady=5, sticky='we')

control_label = ttk.Label(entry_frame, text="Control Point:", font=('Arial', 18))
control_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
control_x_entry = ttk.Entry(entry_frame, font=('Arial', 18))
control_x_entry.grid(row=1, column=1, padx=(0, 5), pady=5, sticky='we')
control_y_entry = ttk.Entry(entry_frame, font=('Arial', 18))
control_y_entry.grid(row=1, column=2, padx=5, pady=5, sticky='we')

end_label = ttk.Label(entry_frame, text="End Point:", font=('Arial', 18))
end_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
end_x_entry = ttk.Entry(entry_frame, font=('Arial', 18))
end_x_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky='we')
end_y_entry = ttk.Entry(entry_frame, font=('Arial', 18))
end_y_entry.grid(row=2, column=2, padx=5, pady=5, sticky='we')

iterations_label = ttk.Label(entry_frame, text="Iterate:", font=('Arial', 18))
iterations_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
iterations_entry = ttk.Entry(entry_frame, font=('Arial', 18))
iterations_entry.grid(row=3, column=1, padx=(0, 5), pady=5, sticky='we')

# Load Button Image for Page 1
button_image_path = resource_path("assets/page-1/curve.png")
button_image = load_image_transparent(button_image_path, 180, 45)

# Button to switch to Animation Page
start_button = tk.Button(entry_frame, image=button_image, command=lambda: switch_tab(1), borderwidth=0, highlightthickness=0, relief='flat')
start_button.image = button_image  # keep a reference to prevent garbage-collection
start_button.grid(row=4, column=0, columnspan=3, padx=5, pady=20)

# Create Canvas for Page 2
canvas2 = tk.Canvas(page2, width=850, height=768)
canvas2.pack(fill="both", expand=True)

# Background Image for Page 2
background_image2 = ImageTk.PhotoImage(file=resource_path("assets/page-2/Dashboard.png"))
canvas2.create_image(0, 0, image=background_image2, anchor="nw")

# Header Image for Page 2
header_image2 = load_image_transparent(resource_path("assets/page-2/header.png"), 920, 46)
canvas2.create_image(425, 28, image=header_image2, anchor="center") 

# Control Image for Page 2
control_image2 = load_image_transparent(resource_path("assets/page-2/control.png"), 80, 20)
canvas2.create_image(60, 70, image=control_image2, anchor="center")

# Text Image for Page 2
text_image2 = load_image_transparent(resource_path("assets/page-2/title.png"), 400, 70)
canvas2.create_image(400, 110, image=text_image2, anchor="center")

# Result Image for Page 2
result_image2 = load_image_transparent(resource_path("assets/page-2/result.png"), 710, 510)
canvas2.create_image(400, 410, image=result_image2, anchor="center")

# Exit Image for Page 2
exit_image2 = load_image_transparent(resource_path("assets/page-2/exit.png"), 60, 30)
canvas2.create_image(390, 680, image=exit_image2, anchor="center")

canvas2.images = [background_image2, header_image2, control_image2, result_image2, exit_image2]

# Add canvas for animation on Page 2
canvas2_animation = tk.Canvas(page2, width=700, height=500)
canvas2_animation.place(x=68, y=190, width=440, height=430)  # Adjust x, y, width, height as needed

def on_show_page2(event):
    if notebook.index("current") == 1:  # Check if the current tab is the animation page
        start_animation()  # Call start_animation only when page 2 is shown

notebook.bind("<<NotebookTabChanged>>", on_show_page2)  # Ensure this is in place to handle tab changes

root.mainloop()