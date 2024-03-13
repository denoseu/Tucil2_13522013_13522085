import matplotlib.pyplot as plt

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def draw_line(point1, point2):
    plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'b-')

def divide_and_conquer(P0, P1, P2, iterations):
    Q0 = midpoint(P0, P1)
    Q1 = midpoint(P1, P2)
    R0 = midpoint(Q0, Q1)

    draw_line(P0, P1)  # Gambar garis antara P0 dan P1
    draw_line(P1, P2)  # Gambar garis antara P1 dan P2
    draw_line(Q0, Q1)  # Gambar garis antara Q0 dan Q1
    draw_line(P0, R0)  # Gambar garis antara P0 dan R0
    draw_line(R0, P2)  # Gambar garis antara R0 dan P2

    if iterations > 1:
        S0 = midpoint(P0, Q0)
        S1 = midpoint(Q0, R0)
        S2 = midpoint(R0, Q1)
        S3 = midpoint(Q1, P2)

        draw_line(S0, S1)  # Gambar garis antara S0 dan S1
        draw_line(S2, S3)  # Gambar garis antara S2 dan S3

        T0 = midpoint(S0, S1)
        T1 = midpoint(S2, S3)

        draw_line(T0, T1)  # Gambar garis antara T0 dan T1

        divide_and_conquer(P0, S0, T0, iterations - 1)
        divide_and_conquer(T1, S2, P2, iterations - 1)

# Titik awal, kontrol antara, dan titik akhir
P0 = (2, 2)
P1 = (3, 3)
P2 = (6, 2)

# Plot titik-titik
plt.plot(*P0, 'ro')
plt.text(P0[0], P0[1], 'P0')
plt.plot(*P1, 'ro')
plt.text(P1[0], P1[1], 'P1')
plt.plot(*P2, 'ro')
plt.text(P2[0], P2[1], 'P2')

# Panggil fungsi divide_and_conquer
iterations = int(input("Masukkan jumlah iterasi: "))
divide_and_conquer(P0, P1, P2, iterations)

# Tampilkan plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Divide and Conquer')
plt.grid()
plt.axis('equal')
plt.show()
