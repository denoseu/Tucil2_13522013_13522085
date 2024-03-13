import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bezier_curve(t, points):
    if len(points) == 1:
        return points[0]
    elif len(points) == 2:
        # linear interpolation for two points
        return (1 - t) * points[0] + t * points[1]
    else:
        # bagi poin poinnya jadi 2 bagian
        titik_tengah = len(points) // 2
        right_points = points[titik_tengah:]
        left_points = points[:titik_tengah + 1]
        
        # hitung rekursif left and right poinnya
        left_curve = bezier_curve(t, left_points)
        right_curve = bezier_curve(t, right_points)
        
        # linear interpolation left sama right poin
        return (1 - t) * left_curve + t * right_curve

def update_line(num, curve_points, line, lines):
    line.set_data(curve_points[:num, 0], curve_points[:num, 1])
    for i, l in enumerate(lines):
        l.set_data([points[i][0], curve_points[num, 0]], [points[i][1], curve_points[num, 1]])
    return line, *lines

n = int(input("Masukkan n: "))
points = []

# input start and end points
x_start, y_start = map(float, input("Masukkan start point (x,y): ").split(","))
points.append(np.array([x_start, y_start]))

# input control points
for i in range(n-2):
    x, y = map(float, input("Masukkan control point ke-{} (x,y): ".format(i+1)).split(","))
    points.append(np.array([x, y]))

x_end, y_end = map(float, input("Masukkan end point (x,y): ").split(","))
points.append(np.array([x_end, y_end]))

# hitung nilai dengan t = 0,1, 50 kali
t_values = np.linspace(0, 1, 50)

# Menghitung semua titik kurva bezier
curve_points = np.array([bezier_curve(t, points) for t in t_values])

# plotting
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-', label='Bézier Curve')
ax.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Bézier Curve Animation')

lines = [ax.plot([], [], 'g--')[0] for _ in range(n-1)]  # Garis antar titik kontrol

def init():
    line.set_data([], [])
    for l in lines:
        l.set_data([], [])
    return line, *lines

ani = animation.FuncAnimation(fig, update_line, frames=len(curve_points), fargs=(curve_points, line, lines),
                              init_func=init, blit=True)

plt.legend(fontsize='small')
plt.grid(True)
plt.axis('equal')

plt.show()
