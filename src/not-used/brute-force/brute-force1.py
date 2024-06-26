import numpy as np
import matplotlib.pyplot as plt

### ALGORITHM ###
def bezier_curve_recursive(t, points):
    if len(points) == 1:
        return points[0]
    else:
        new_points = []
        for i in range(len(points)-1):
            new_point = (1 - t) * points[i] + t * points[i+1]
            new_points.append(new_point)
            print(f"For t = {t}: {new_points}")
        return bezier_curve_recursive(t, new_points)

n = int(input("Masukkan n: "))
points = []

# Masukan poin-poin
x_start, y_start = map(float, input("Masukan start point (x,y): ").split(","))
points.insert(0, np.array([x_start, y_start]))
                   
# input control points, kurangin 2 karena n udah termasuk start dan end points
num_points = n-2
for _ in range(num_points):
    x, y = map(float, input("Masukan control point (x,y): ").split(","))
    points.append(np.array([x, y]))

x_end, y_end = map(float, input("Masukan end point (x,y): ").split(","))
points.append(np.array([x_end, y_end]))

# t nya dari 0 sampai 1, 100 titik
t_values = np.linspace(0, 1, 1000)

# cari curve points
curve_points = np.array([bezier_curve_recursive(t, points) for t in t_values])

# plotting
plt.plot(curve_points[:,0], curve_points[:,1], label='Bézier Curve')
plt.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bézier Curve')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()