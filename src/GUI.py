import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os, sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

########## ALGORITMA ##########
def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def draw_bezier_curve(P0, P1, P2, iterations, current_iteration, ax):
    if iterations == 0:
        ax.plot([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], 'b-')
    else:
        Q0 = midpoint(P0, P1)
        Q1 = midpoint(P1, P2)
        R0 = midpoint(Q0, Q1)
        
        draw_bezier_curve(P0, Q0, R0, iterations - 1, current_iteration, ax)
        draw_bezier_curve(R0, Q1, P2, iterations - 1, current_iteration, ax)
        
        if iterations == current_iteration:
            ax.plot([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], '--', color='grey')

def start_animation():
    global ani
    start_time = time.time()

    # Mengambil nilai input dari entry pada GUI
    update_point_text()
    x_start, y_start = float(start_x_entry.get()), float(start_y_entry.get())
    P0 = (x_start, y_start)

    x, y = float(control_x_entry.get()), float(control_y_entry.get())
    P1 = (x, y)

    x_end, y_end = float(end_x_entry.get()), float(end_y_entry.get())
    P2 = (x_end, y_end)

    def animate(iteration):
        ax.clear()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        current_time = time.time() - start_time
        ax.set_title(f'Bezier Curve Iteration {iteration} (Time exe.: {current_time:.2f} detik)')
        ax.grid()
        ax.axis('equal')

        # Plot titik-titik awal
        plt.plot(*P0, 'ro')
        plt.text(P0[0], P0[1], 'P0')
        plt.plot(*P1, 'ro')
        plt.text(P1[0], P1[1], 'P1')
        plt.plot(*P2, 'ro')
        plt.text(P2[0], P2[1], 'P2')

        # Menggambar kurva bezier
        for i in range(1, iteration + 1):
            draw_bezier_curve(P0, P1, P2, iteration, i, ax)

    fig, ax = plt.subplots()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Bezier Curve')
    ax.grid()
    ax.axis('equal')

    iterations = int(iterations_entry.get())
    ani = FuncAnimation(fig, animate, frames=iterations + 1, interval=350, repeat=False)

    canvas2.fig_photo = draw_figure(canvas2_animation, fig)

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

########## BANTUAN FUNGSI UNTUK GUI ##########
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return ImageTk.PhotoImage(img)

# load gambar png untuk resize
def load_image_transparent(image_path, width, height):
    img = Image.open(image_path).resize((width, height), Image.NEAREST)
    return ImageTk.PhotoImage(img)

# switch notebook tab
def switch_tab(tab_index):
    notebook.select(tab_index)

def update_point_text():
    # fetch points
    x_start, y_start = start_x_entry.get(), start_y_entry.get()
    x_control, y_control = control_x_entry.get(), control_y_entry.get()
    x_end, y_end = end_x_entry.get(), end_y_entry.get()
    
    text_x = 668
    start_y = 300
    line_height = 35
    
    canvas2.create_text(text_x, start_y, text=f"{x_start}            {y_start}", fill="black", anchor="center")
    canvas2.create_text(text_x, start_y + line_height, text=f"{x_control}            {y_control}", fill="black", anchor="center")
    canvas2.create_text(text_x, start_y + 2 * line_height, text=f"{x_end}            {y_end}", fill="black", anchor="center")

def exit_program():
    root.quit()  # quit tkinter application
    root.destroy()  # destroy tkinter window
    sys.exit()  #  exit python

########## TKINTER GUI ##########
root = tk.Tk()
root.title("Bezier Curve Maker")
root.geometry("850x768")

# create notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

##### page 1 #####
page1 = ttk.Frame(notebook)
notebook.add(page1, text='Input')

# create canvas
canvas1 = tk.Canvas(page1, width=850, height=768)
canvas1.pack(fill="both", expand=True)

# background
background_image = ImageTk.PhotoImage(file=resource_path("assets/page-1/Dashboard.png"))
canvas1.create_image(0, 0, image=background_image, anchor="nw")

# header
header_image = load_image_transparent(resource_path("assets/page-1/header.png"), 920, 40)
canvas1.create_image(425, 28, image=header_image, anchor="center") 

# logo
logo_image = load_image_transparent(resource_path("assets/page-1/logo.png"), 920, 254)
canvas1.create_image(425, 175, image=logo_image, anchor="center") 

# control
control_image = load_image_transparent(resource_path("assets/page-1/control.png"), 130, 35)
canvas1.create_image(78, 75, image=control_image, anchor="center")

# text
text_image = load_image_transparent(resource_path("assets/page-1/title.png"), 630, 50)
canvas1.create_image(410, 160, image=text_image, anchor="center")

canvas1.images = [background_image, header_image, logo_image, control_image, text_image]

# frame untuk input table
entry_frame = tk.Frame(page1, bg='#dabecb', bd=5)
entry_frame.place(relx=0.5, rely=0.45, relwidth=0.85, relheight=0.5, anchor='n')
entry_frame.grid_rowconfigure(0, minsize=40)

# input table
x_label = tk.Label(entry_frame, text="x", font=('Arial', 18), bg='#dabecb')
x_label.grid(row=1, column=1, padx=0, pady=0, sticky='nsew')
y_label = tk.Label(entry_frame, text="y", font=('Arial', 18), bg='#dabecb')
y_label.grid(row=1, column=2, padx=0, pady=0, sticky='nsew')

start_label = tk.Label(entry_frame, text="Start Point:", font=('Arial', 18), bg='#dabecb')
start_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
start_x_entry = tk.Entry(entry_frame, font=('Arial', 18), borderwidth=0, highlightthickness=0)
start_x_entry.grid(row=2, column=1, padx=(0, 5), pady=5, sticky='we')
start_y_entry = tk.Entry(entry_frame, font=('Arial', 18), borderwidth=0, highlightthickness=0)
start_y_entry.grid(row=2, column=2, padx=5, pady=5, sticky='we')

control_label = tk.Label(entry_frame, text="Control Point:", font=('Arial', 18), bg='#dabecb')
control_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
control_x_entry = tk.Entry(entry_frame, font=('Arial', 18), borderwidth=0, highlightthickness=0)
control_x_entry.grid(row=3, column=1, padx=(0, 5), pady=5, sticky='we')
control_y_entry = tk.Entry(entry_frame, font=('Arial', 18), borderwidth=0, highlightthickness=0)
control_y_entry.grid(row=3, column=2, padx=5, pady=5, sticky='we')

end_label = tk.Label(entry_frame, text="End Point:", font=('Arial', 18), bg='#dabecb')
end_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
end_x_entry = tk.Entry(entry_frame, font=('Arial', 18), borderwidth=0, highlightthickness=0)
end_x_entry.grid(row=4, column=1, padx=(0, 5), pady=5, sticky='we')
end_y_entry = tk.Entry(entry_frame, font=('Arial', 18), borderwidth=0, highlightthickness=0)
end_y_entry.grid(row=4, column=2, padx=5, pady=5, sticky='we')

iterations_label = tk.Label(entry_frame, text="Iteration:", font=('Arial', 18), bg='#dabecb')
iterations_label.grid(row=5, column=0, padx=5, pady=5, sticky='e')
iterations_entry = tk.Entry(entry_frame, font=('Arial', 18), borderwidth=0, highlightthickness=0)
iterations_entry.grid(row=5, column=1, padx=(0, 5), pady=5, sticky='we')

# generate curve button
button_image_path = resource_path("assets/page-1/curve.png")
button_image = load_image_transparent(button_image_path, 180, 38)
# button ke page 2
start_button = tk.Button(entry_frame, image=button_image, command=lambda: switch_tab(1), borderwidth=0, highlightthickness=0, relief='flat')
start_button.image = button_image  # keep a reference to prevent garbage-collection
start_button.place(relx=0.5, rely=0.75, anchor='center')

##### page 2 #####
page2 = ttk.Frame(notebook)
notebook.add(page2, text='Animation')

# create canvas
canvas2 = tk.Canvas(page2, width=850, height=768)
canvas2.pack(fill="both", expand=True)

# background
background_image2 = ImageTk.PhotoImage(file=resource_path("assets/page-2/Dashboard.png"))
canvas2.create_image(0, 0, image=background_image2, anchor="nw")

# header
header_image2 = load_image_transparent(resource_path("assets/page-2/header.png"), 920, 40)
canvas2.create_image(425, 28, image=header_image2, anchor="center") 

# control
control_image2 = load_image_transparent(resource_path("assets/page-2/control.png"), 130, 35)
canvas2.create_image(78, 75, image=control_image2, anchor="center")

# text
text_image2 = load_image_transparent(resource_path("assets/page-2/title.png"), 400, 70)
canvas2.create_image(400, 110, image=text_image2, anchor="center")

# result
result_image2 = load_image_transparent(resource_path("assets/page-2/result.png"), 710, 510)
canvas2.create_image(400, 410, image=result_image2, anchor="center")

# exit
exit_image2 = load_image_transparent(resource_path("assets/page-2/exit.png"), 60, 30)
canvas2.create_image(390, 680, image=exit_image2, anchor="center")
# exit button
exit_button = tk.Button(page2, image=exit_image2, command=exit_program, borderwidth=0)
exit_button_window = canvas2.create_window(390, 680, anchor="center", window=exit_button)

canvas2.images = [background_image2, header_image2, control_image2, result_image2, exit_image2]

# canvas untuk si animasi di page 2
canvas2_animation = tk.Canvas(page2, width=700, height=500)
canvas2_animation.place(x=68, y=190, width=440, height=430)

def on_show_page2(event):
    if notebook.index("current") == 1:
        start_animation()  # panggil fungsi ketika udah di page 2 aja

notebook.bind("<<NotebookTabChanged>>", on_show_page2)

root.mainloop()
