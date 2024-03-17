import numpy as np
import matplotlib.pyplot as plt
import math
import timeit
from matplotlib.animation import FuncAnimation

# menghitung bobot tiap titik kontrol
def binomial_coefficient(n, k):
    if 0 <= k <= n:
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    else:
        return 0

# secara langsung menentukan titik dengan menghitung menggunakan rumus kurva bezier
def bezier_curve_points(points, iterations):
    curve_points = []
    for t_value in range(iterations):
        t = t_value / (iterations - 1)
        curve_point = [0, 0]
        for point_index in range(len(points)):
            coefficient = binomial_coefficient(len(points) - 1, point_index)
            bezier_term = coefficient * ((1 - t) ** (len(points) - 1 - point_index)) * (t ** point_index)
            curve_point[0] += bezier_term * points[point_index][0]
            curve_point[1] += bezier_term * points[point_index][1]
        curve_points.append(curve_point)
    return np.array(curve_points)


# VISUALISASI
def update(frame, ax, points, curves, iterations, execution_time):
    ax.clear()
    ax.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
    curve = curves[:frame+1]  # Select curve points up to the current iteration
    ax.plot(curve[:, 0], curve[:, 1], 'b-', label=f'Iteration {frame}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Bezier Curve Iteration {frame}')
    ax.legend()
    ax.axis('equal')

    execution_time_info = f'Execution Time: {execution_time:.2f} seconds'
    ax.text(0.95, 0.05, execution_time_info, transform=ax.transAxes, ha='right', va='bottom')


def main():
    # Input n titik
    n = int(input("Masukkan jumlah titik yang hendak dimasukkan: "))
    while n < 2:
        print("\nUntuk membuat kurva masukkan 2 atau lebih titik!")
        n = int(input("Masukkan jumlah titik yang hendak dimasukkan: "))

    # Input koordinat poin-poin
    x_start, y_start = map(float, input("Masukkan start point (x,y): ").split(","))
    points = [(x_start, y_start)]

    # control points
    for i in range(n-2):
        x, y = map(float, input("Masukkan control point {}: (x,y): ".format(i+1)).split(","))
        points.append((x, y))
    
    # end points
    x_end, y_end = map(float, input("Masukkan end point (x,y): ").split(","))
    points.append((x_end, y_end))

    # banyak iterasi
    iterations = int(input("Masukkan jumlah iterasi: "))

    start_time = timeit.default_timer()
    curves = bezier_curve_points(points, iterations+1)
    
    fig, ax = plt.subplots()

    execution_time = timeit.default_timer() - start_time
    
    ani = FuncAnimation(fig, update, frames=iterations+1, fargs=(ax, points, curves, iterations, execution_time), interval=150, repeat=False)
    plt.show()

if __name__ == "__main__":
    main()