<h2 align="center"> Tugas Kecil 2 IF2211 Strategi Algoritma </h2>
<h1 align="center">  Membangun Kurva <em> Bézier </em> dengan Algoritma <em> Divide and Conquer </em> Titik Tengah berbasis</h1>

## Contributors
|   NIM    |                  Nama                  |
| :------: | :------------------------------------: |
| 13522013 |        Denise Felicia Tiowanni         |
| 13522085 |          Zahira Dina Amalia            |


## Deskripsi Program
program ini ...

## Project Structure
```
│
├── bin
│
├── doc
│
├── src
│   ├── assets
│   │   ├── page-1
│   │   └── page-2
│   ├── brute-force
│   │   └── brute-force.py
│   ├── dnc-3.py
│   ├── dnc-n.py
│   └── gui.py
│
├── test
│
└── README.md

```

## Program Requirements
Pastikan Python dan pip sudah terinstall pada sistem. Cek Python dengan <code>python --version</code> dan pip dengan <code>pip -V</code>.
### Program requirements untuk DNC-3-titik dan DNC-n-titik
1. Matplotlib <br>
    Berikut adalah command untuk mengunduh matplotlib.
    ```
    pip install matplotlib
    ```
### Program requirements untuk GUI
1. Tkinter <br>
    Berikut adalah command untuk mengunduh Tkinter.
    ```
    pip install tk
    ```
2. Matplotlib <br>
    Berikut adalah command untuk mengunduh matplotlib.
    ```
    pip install matplotlib
    ```
3. PIL <br>
    Berikut adalah command untuk mengunduh PIL.
    ```
    pip install Pillow
    ```

## How to Run and Use (CLI ver.)
### Terdapat 2 versi yang bisa dijalankan, yaitu menghitung kurva Bézier dengan n titik (>= 4) atau 3 titik saja.
1. Clone repository ini dengan 
    ```
    git clone https://github.com/hiirrs/Tucil2_13522013_13522085.git
    ```
2. Buka folder repository pada terminal.
3. Pindah ke direktori *src* dengan `cd src`
4. Pilih jenis algoritma yang ingin dijalankan (n titik atau 3 titik). 
    Untuk menjalankan program kurva Bézier dengan 3 titik:
    ```
    python dnc-3.py
    ```
    Untuk menjalankan program kurva Bézier dengan n titik:
    ```
    python dnc-n.py
    ```
    Jangan lupa untuk adjust jenis python yang digunakan, apabila mengunakan python3, ubah python menjadi <code>python3</code>.
5. Untuk 3 titik: masukkan start point, control point, end point, serta jumlah iterasi. <br>
   Untuk n titik: masukkan n, start point, control points, end point, serta jumlah iterasi.
6. Klik enter/return.
7. Animasi kurva akan ditampilkan pada sebuah window baru.

## How to Run and Use (GUI ver.)
### Algoritma program dengan GUI hanya menghandle kasus kurva Bézier dengan 3 titik saja.
1. Clone repository ini dengan 
    ```
    git clone https://github.com/hiirrs/Tucil2_13522013_13522085.git
    ```
2. Buka folder repository pada terminal.
3. Pindah ke direktori *src* dengan `cd src`
4. Run GUI file dengan
    ```
    python3 gui.py
    ```
5. Klik enter/return.
6. Masukkan start point, control point, end point, serta jumlah iterasi pada kotak yang telah disediakan.
7. Klik generate curve.
8. Animasi kurva akan ditampilkan pada laman 'Animate', klik exit untuk keluar dari program.

## How to Run Executable