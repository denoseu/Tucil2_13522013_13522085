import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fungsi untuk menghitung titik pada kurva Bezier
def bezier(t, points):
    n = len(points) - 1
    result = np.zeros(2)
    for i, (x, y) in enumerate(points):
        binomial_coef = np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))
        result += binomial_coef * (1 - t)**(n - i) * t**i * np.array([x, y])
    return result

# Fungsi untuk menggambar animasi
def animate(frame):
    plt.cla()
    plt.plot(*zip(*control_points), 'bo--')
    if frame > 0:
        t = frame / (num_frames - 1)
        bezier_curve = bezier(t, control_points)
        plt.plot(bezier_curve[0], bezier_curve[1], 'r-')
        plt.title(f'Frame {frame+1}/{num_frames}')

# Titik kontrol kurva Bezier
control_points = [(1, 1), (2, 4), (5, 6), (7, 3)]

# Inisialisasi plot
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)

# Jumlah frame animasi
num_frames = 50

# Membuat animasi
ani = FuncAnimation(fig, animate, frames=num_frames, interval=100)

# Menyimpan animasi sebagai file GIF (butuh ImageMagick)
# ani.save('bezier_animation.gif', writer='imagemagick', fps=10)

# Tampilkan animasi
plt.show()
