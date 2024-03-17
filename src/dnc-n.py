import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# untuk mencari titik tengah
def mid(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# secara rekursif mencari titik tengah dari list of points
def recursive_midpoint(points, next_points):
    if len(points) == 1:
        return points[0], next_points
    else:
        midpoints = []
        for i in range(len(points) - 1):
            midpoints.append(mid(points[i], points[i+1]))
        if len(midpoints) == 1:
            to = len(next_points) // 2 
            next_points.insert(to, midpoints[0])
        else:
            to = len(next_points) // 2 
            next_points.insert(to, midpoints[-1])
            next_points.insert(to, midpoints[0])
        return recursive_midpoint(midpoints, next_points)

# mengambil titik-titik terluar untuk proses kurva selanjutnya   
def make_the_next(points, next_points, middle):
    going = [points[0]] + next_points + [points[-1]]
    if len(going) % 2 == 0:
        to = len(going) // 2
        going.insert(to, middle)
    return going

# mengumpulkan titik-titik untuk menggambar kurva
def gather_graph_points(graph_points, middle_points):
    if len(middle_points) == 1 and len(graph_points) == 2:
        to = len(graph_points) // 2 
        graph_points.insert(to, middle_points[0])
        return graph_points
    else:
        mid_graph = len(graph_points) // 2 
        left_half_graph = graph_points[:mid_graph+1]
        right_half_graph = graph_points[mid_graph:]

        mid_middle = len(middle_points) // 2 
        left_half_middle = middle_points[:mid_middle]
        right_half_middle = middle_points[mid_middle:]

        return gather_graph_points(left_half_graph, left_half_middle)[:-1] + gather_graph_points(right_half_graph, right_half_middle)

# secara rekursif membagi list of points menjadi sesuai panjang 'length'
def divide_list_of_points(points, length):
    num_points = len(points)
    if num_points <= length:
        return [points]
    else:
        midpoint = num_points // 2
        left_half = points[:midpoint+1]
        right_half = points[midpoint:]
        return divide_list_of_points(left_half, length) + divide_list_of_points(right_half, length)

# memproses kurva bezier sesuai iterasi yang dimasukkan dan menyimpan titik-titik kurva untuk tiap iterasinya
def iterations(points, next_points, graph_points, iteration, i_now, save_graphs):

    if iteration == 0:
        save_graphs.append(graph_points)
        return save_graphs
    elif len(next_points) <= len(points):
        new_mids = []
        new_midpoints, new_next_points = recursive_midpoint(points, next_points)
        new_mids.append(new_midpoints)
        graph_points = gather_graph_points(graph_points, new_mids)
        save_graphs.append(graph_points)
        return iterations(points, new_next_points, graph_points, iteration-1, i_now+1, save_graphs)
    else:
        top = graph_points[len(graph_points)//2]
        next_points = make_the_next(points, next_points, top)
        divided_next_points = divide_list_of_points(next_points, len(points))
        each_next = []
        new_mids = []
        for part in divided_next_points:
            new_midpoints, the_next = recursive_midpoint(part, [])
            new_mids.append(new_midpoints)
            for next in the_next:
                each_next.append(next)
        graph_points = gather_graph_points(graph_points, new_mids)
        save_graphs.append(graph_points)

        return iterations(points, each_next, graph_points, iteration-1, i_now+1, save_graphs)


# Input n titik
n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

while (n < 4):
    print("\nUntuk membuat kurva masukan 4 atau lebih titik!")
    n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

# Input koordinat poin-poin
x_start, y_start = map(float, input("Masukan start point (x,y): ").split(","))
points = [(x_start, y_start)]

# Input control points
for i in range(n-2):
    x, y = map(float, input("Masukan control point {}: (x,y): ".format(i+1)).split(","))
    points.append((x, y))

x_end, y_end = map(float, input("Masukan end point (x,y): ").split(","))
points.append((x_end, y_end))

print("Iterasi maksimum ialah n+1! (dengan n jumlah titik yang dimasukkan)")
i = int(input("Masukan jumlah iterasi: "))
while i > n+1:
    print("Iterasi maksimum ialah n+1! (dengan n jumlah titik yang dimasukkan)")
    i = int(input("Masukan jumlah iterasi: "))

# Untuk penggunaan otomatis
# points = [(1.0, 0.0), (0.0, 3.0), (3.0, 6.0), (6.0, 6.0), (9.0, 3.0), (8.0, 0.0)]
# points = [(0.0, 0.0), (2.0, 5.0), (6.0, 7.0), (10.0, 5.0), (12.0, 0.0)]
# points = [(0.0, 0.0), (0.0, 8.0), (8.0, 8.0), (8.0, 0.0)]

# Memulai program
start_time = time.perf_counter()

# Inisialisasi
next_points = []
graph_points = [points[0], points[-1]]
previous_curves = []
saved_graphs = []

# Mengambil titik-titik untuk membentuk kurva bezier
saved_graphs = iterations(points, next_points, graph_points, i, 0, saved_graphs)

# Akhir program
end_time = time.perf_counter()

# Waktu eksekusi
time_execution = (end_time - start_time) *1000


# VISUALISASI
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid()
ax.axis('equal')

# Untuk memperlihatkan kurva tiap iterasi
def animate(iteration, time_execution, control_points):

    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Beziér Curve {iteration} Iteration ')
    ax.grid()
    ax.axis('equal')

    # kurva yang bukan current curve akan berwarna abu garis-garis
    for i in range(iteration):
        points = saved_graphs[i]
        x_points, y_points = zip(*points)
        ax.plot(x_points, y_points, '--', color='gray', label='Curve Before' if i == 0 else '')

    # kurva yang merupakan current curve akan berwarna biru
    points = saved_graphs[iteration]
    x_points, y_points = zip(*points)
    ax.plot(x_points, y_points, 'b-',  label='Current Curve')
    ax.plot([point[0] for point in control_points], [point[1] for point in control_points], 'ro-', label='Control Points')
    ax.legend(loc='lower right', fontsize=10)

    execution_time_info = f'Execution Time: {time_execution:.2f} milliseconds'
    ax.text(0.5, 0.965, execution_time_info, transform=ax.transAxes, ha='center', fontsize=10)

iterations = len(saved_graphs)
ani = FuncAnimation(fig, animate, frames=iterations, fargs=(time_execution, points), interval=300, repeat=False)

plt.show()