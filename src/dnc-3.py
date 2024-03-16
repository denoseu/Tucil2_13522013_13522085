import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# mencari mid point 2 titik
def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# menggambar kurva bezier
def draw_bezier_curve(P0, P1, P2, iterations, current_iteration):
    if iterations == 0:
        plt.plot([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], 'r-')
    else:
        Q0 = midpoint(P0, P1)
        Q1 = midpoint(P1, P2)
        R0 = midpoint(Q0, Q1)
        
        draw_bezier_curve(P0, Q0, R0, iterations - 1, current_iteration)
        draw_bezier_curve(R0, Q1, P2, iterations - 1, current_iteration)
        
        if iterations == current_iteration:
            plt.plot([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], '--')


print("\n-- Kurva Bezier dengan 3 titik kontrol --")

# # titik awal dan akhir
# P0 = (0, 0)
# P1 = (4, 4)
# P2 = (8, 0)

# Input koordinat poin-poin
x_start, y_start = map(float, input("Masukan start point (x,y): ").split(","))
P0 = (x_start, y_start)

x_control, y_control = map(float, input("Masukan control point (x,y): ").split(","))
P1 = (x_control, y_control)

x_end, y_end = map(float, input("Masukan end point (x,y): ").split(","))
P2 = (x_end, y_end)

points = [P0, P1, P2]

# buat kurva animasi
def animate(iteration):

    # plot titik-titik awal
    plt.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Beziér Curve Iteration {iteration}')
    ax.grid()
    ax.axis('equal')
    for i in range(1, iteration + 1):
        draw_bezier_curve(P0, P1, P2, iteration, i)
    ax.autoscale()

    # tampilkan waktu eksekusi
    execution_time = time.time() - start_time
    ax.text(0.95, 0.05, f'Execution Time: {execution_time:.2f} seconds', transform=ax.transAxes, ha='right', va='bottom', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))


# inisialisasi plot
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Beziér Curve')
ax.grid()
ax.axis('equal')

# buat animasi
iterations = int(input("Masukkan jumlah iterasi: "))
start_time = time.time()
ani = FuncAnimation(fig, animate, frames=iterations, interval=350, repeat=False)

# tampilkan animasi
plt.draw()
plt.show()