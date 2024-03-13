import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# menyimpan kurva sebelumnya supaya ga hilang (bisa di view)
previous_curves = []

# fungsi untuk menggambar bezier secara rekursif
def draw_bezier_recursive(points, iterations):
    if len(points) == 2 or iterations == 0:
        xs, ys = zip(*points)  # unpack points menjadi x and y coordinates
        if iterations == 0:
            plt.plot(xs, ys, 'b-')  # garis normal untuk iterasi terakhir
            # simpan kurva ini untuk iterasi berikutnya
            previous_curves.append((xs, ys))
        # tidak perlu lagi menyimpan kurva di sini karena kita tidak menggunakan previous_curves dalam fungsi ini
    else:
        new_points = []
        for i in range(len(points)-1):
            new_points.append(midpoint(points[i], points[i+1]))
        new_points = [points[0]] + new_points + [points[-1]]
        draw_bezier_recursive(new_points, iterations - 1)

def animate(iteration):
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Beziér Curve Iteration {iteration}')
    ax.grid()
    ax.axis('equal')

    # tampilkan titik
    for i, point in enumerate(points):
        plt.plot(*point, 'ro')
        plt.text(point[0], point[1], f'P{i}')

    # gambar ulang semua kurva sebelumnya dengan garis putus-putus (biar tau yang lalu lalu)
    for curve in previous_curves[:iteration]:
        plt.plot(curve[0], curve[1], '--', color='grey')

    # gambar kurva saat ini
    draw_bezier_recursive(points, iteration)

# contoh titik
points = [(2, 2), (4, 4), (3, 3), (6, 2)]

# inisialisasi plot
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Beziér Curve')
ax.grid()
ax.axis('equal')

# buat animasi
iterations = int(input("Masukkan jumlah iterasi: "))
ani = FuncAnimation(fig, animate, frames=iterations+1, interval=350, repeat=False)

# tampilkan animasi
plt.draw() 
plt.show()
