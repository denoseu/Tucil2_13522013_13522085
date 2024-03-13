import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def draw_bezier_curve(points, iterations, current_iteration):
    if iterations == 0:
        plt.plot([point[0] for point in points], [point[1] for point in points], 'b-')
    else:
        new_points = [midpoint(points[i], points[i+1]) for i in range(len(points)-1)]
        
        draw_bezier_curve(new_points, iterations - 1, current_iteration)
        
        if iterations == current_iteration:
            plt.plot([point[0] for point in points], [point[1] for point in points], 'r--')

def animate(iteration):
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Bezier Curve Iteration {iteration}')
    ax.grid()
    ax.axis('equal')
    for i in range(1, iteration + 1):
        draw_bezier_curve(points, iteration, i)
    ax.autoscale()

# Inisialisasi plot
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Bezier Curve')
ax.grid()
ax.axis('equal')

# Input jumlah titik dan titik-titiknya
n = int(input("Masukkan jumlah titik: "))
points = []
for i in range(n):
    point = tuple(map(float, input(f"Masukkan koordinat titik {i+1} (format: x y): ").split()))
    points.append(point)

# Buat animasi
iterations = int(input("Masukkan jumlah iterasi: "))
ani = FuncAnimation(fig, animate, frames=iterations, interval=350, repeat=True)

# Tampilkan animasi
plt.show()
