import numpy as np
import matplotlib.pyplot as plt
import math
import time
from matplotlib.animation import FuncAnimation

# menghitung bobot tiap titik kontrol
def binomial_coefficient(n, k):
    if 0 <= k <= n:
        n1 = math.factorial(n)
        k1 = math.factorial(k)
        return n1 // (k1 * math.factorial(n - k))
    else:
        return 0

# secara langsung membuat kurva bezier
def bezier_curve_direct(t, points):
    n = len(points) - 1
    result = np.zeros(2)
    for i, p in enumerate(points):
        result += binomial_coefficient(n, i) * ((1 - t) ** (n - i)) * (t ** i) * np.array(p)
    return result

def plot_bezier_curve(frame, ax, points, execution_time):
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Beziér Curve Iteration {frame}')
    ax.grid()
    ax.axis('equal')
    ax.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
    for i in range(1, frame + 1):
        t_values = np.linspace(0, 1, i*2+1)
        curve_points = np.array([bezier_curve_direct(t, points) for t in t_values])
        if i == frame:
            ax.plot(curve_points[:,0], curve_points[:,1], color='blue', label='Current Iteration')
        else:
            ax.plot(curve_points[:,0], curve_points[:,1], linestyle='dotted', color='gray')
    ax.legend()

    execution_time_info = f'Execution Time: {execution_time:.2f} seconds'
    ax.text(0.95, 0.05, execution_time_info, transform=ax.transAxes, ha='right', va='bottom', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))


def main():
    # Input n titik
    n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))
    while (n < 2):
        print("\nUntuk membuat kurva masukan 2 atau lebih titik!")
        n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

    # Input koordinat poin-poin
    # start points
    x_start, y_start = map(float, input("Masukan start point (x,y): ").split(","))
    points = [(x_start, y_start)]

    # control points
    for i in range(n-2):
        x, y = map(float, input("Masukan control point {}: (x,y): ".format(i+1)).split(","))
        points.append((x, y))
    
    # end points
    x_end, y_end = map(float, input("Masukan end point (x,y): ").split(","))
    points.append((x_end, y_end))

    # Input jumlah iterasi
    iteration = int(input("Masukan jumlah iterasi: "))
    
    start_time = time.time()
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, plot_bezier_curve, frames=iteration+1, fargs=(ax, points, time.time()-start_time), interval=500, repeat=False)
    plt.show()

if __name__ == "__main__":
    main()
