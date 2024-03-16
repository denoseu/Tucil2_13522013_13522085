import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

def binomial_coefficient(n, k):
    if 0 <= k <= n:
        n_fact = math.factorial(n)
        k_fact = math.factorial(k)
        return n_fact // (k_fact * math.factorial(n - k))
    else:
        return 0

def bezier_curve_brute_force(t, points):
    n = len(points) - 1
    result = np.zeros(2)
    for i, p in enumerate(points):
        result += binomial_coefficient(n, i) * ((1 - t) ** (n - i)) * (t ** i) * np.array(p)
    return result

def plot_bezier_curve(frame, ax, points):
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Beziér Curve Iteration {frame}')
    ax.grid()
    ax.axis('equal')
    ax.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
    for i in range(1, frame + 1):
        t_values = np.linspace(0, 1, i*2+1)
        curve_points = np.array([bezier_curve_brute_force(t, points) for t in t_values])
        if i == frame:
            ax.plot(curve_points[:,0], curve_points[:,1], color='red', label='Current Iteration')
        else:
            ax.plot(curve_points[:,0], curve_points[:,1], linestyle='dotted', color='gray')
    ax.legend()

def main():
    # Input n titik
    n = int(input("Masukan jumlah titik yang hendak dimasukkan: "))

    while (n < 2):
        print("\nUntuk membuat kurva masukan 2 atau lebih titik!")
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

    iteration = int(input("Masukan jumlah iterasi: "))

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, plot_bezier_curve, frames=iteration+1, fargs=(ax, points), interval=500, repeat=False)
    plt.show()

if __name__ == "__main__":
    main()
