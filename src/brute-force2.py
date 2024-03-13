import numpy as np
import matplotlib.pyplot as plt
import math

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

def plot_bezier_curve(points):
    t_values = np.linspace(0, 1, 100)
    curve_points = np.array([bezier_curve_brute_force(t, points) for t in t_values])
    
    plt.plot(curve_points[:,0], curve_points[:,1], label='Bézier Curve')
    plt.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bézier Curve')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    n = int(input("Masukan jumlah titik (minimal 3): "))
    
    x_start, y_start = map(float, input("Masukan start point (x,y): ").split(","))
    start_point = np.array([x_start, y_start])

    points = [start_point]
    for i in range(n - 2):
        x, y = map(float, input(f"Masukan koordinat untuk control point {i+1} (x,y): ").split(","))
        points.append(np.array([x, y]))
    
    x_end, y_end = map(float, input("Masukan end point (x,y): ").split(","))
    end_point = np.array([x_end, y_end])
    points.append(end_point)
    
    plot_bezier_curve(points)

if __name__ == "__main__":
    main()