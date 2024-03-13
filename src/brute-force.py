import numpy as np
import matplotlib.pyplot as plt

def kuadrat_bezier(t, p_start, p_control, p_end):
    return (1 - t) ** 2 * p_start + 2 * (1 - t) * t * p_control + t ** 2 * p_end

x0, y0 = map(float, input("start point (comma-separated): ").split(","))
x1, y1 = map(float, input("end point (comma-separated): ").split(","))
x2, y2 = map(float, input("control point (comma-separated): ").split(","))

p_start = np.array([x0, y0])
p_end = np.array([x1, y1])
p_control = np.array([x2, y2])

t_values = np.linspace(0, 1, 100)
curve_points = np.array([kuadrat_bezier(t, p_start, p_control, p_end) for t in t_values])

plt.plot(curve_points[:,0], curve_points[:,1], label='Bézier Curve')
plt.plot([p_start[0], p_control[0], p_end[0]], [p_start[1], p_control[1], p_end[1]], 'ro-', label='Control Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quadratic Bézier Curve')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
