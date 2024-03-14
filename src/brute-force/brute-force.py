## KIRAIN DIVIDE N CONQUER TAUNYA BRUTE FORCE :(

import numpy as np
import matplotlib.pyplot as plt
import os, time

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

# hitung nilai dengan t = 0,1, 100 kali
t_values = np.linspace(0, 1, 100)
print(t_values)

start_time = time.time()
curve_points = np.array([bezier_curve(t, points) for t in t_values])
end_time = time.time()

print("Waktu eksekusi: ", end_time - start_time, " detik")

# plotting
plt.plot(curve_points[:,0], curve_points[:,1], label='Bézier Curve')
plt.plot([point[0] for point in points], [point[1] for point in points], 'ro-', label='Control Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bézier Curve\nWaktu eksekusi: {} detik'.format(end_time - start_time))
plt.legend(fontsize='small')
plt.grid(True)
plt.axis('equal')

# # save to folder /test
# # current directory
# current_directory = os.path.abspath(os.path.dirname(__file__))
# # mundur 1 folder
# parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

# file_name = input("Masukkan nama file (contoh: 'xx.png'): ")
# file_path = parent_directory + "/test/" + file_name
# plt.savefig(file_path)

plt.show()
