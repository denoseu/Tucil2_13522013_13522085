<h2 align="center"> Tugas Kecil 2 IF2211 Strategi Algoritma </h2>
<h1 align="center">  Membangun Kurva <em> Bézier </em> dengan Algoritma <em> Divide and Conquer </em> Titik Tengah berbasis</h1>

## Contributors
|   NIM    |                  Nama                  |
| :------: | :------------------------------------: |
| 13522013 |        Denise Felicia Tiowanni         |
| 13522085 |          Zahira Dina Amalia            |


## Deskripsi Program
Program ini, sesuai namanya, mengimplementasikan pembuatan kurva Bézier dengan algoritma titik tengah berbasis divide and conquer. Program ini akan menerima input berupa titik seperti start point, control point, maupun endpoint dari pengguna untuk kemudian diolah menjadi sebuah kurva Bézier. Program juga akan meminta pengguna memasukkan banyak iterasi yang diinginkan untuk memperhalus kurva.

## Project Structure
```
│
├── bin
│
├── doc
│   ├── Tucil2_13522013_13522085.pdf
│
├── src
│   ├── assets
│   │   ├── page-1
│   │   └── page-2
│   ├── brute-force.py
│   ├── dnc-3.py
│   ├── dnc-n.py
│   └── gui.py
│
├── test
│   ├── brute-force-1.png
│   ├── brute-force-2.png
│   ├── brute-force-3.png
│   ├── brute-force-4.png
│   ├── brute-force-5.png
│   ├── brute-force-6.png
│   ├── dnc-1.png
│   ├── dnc-2.png
│   ├── dnc-3.png
│   ├── dnc-4.png
│   ├── dnc-5.png
│   ├── dnc-6.png
│   ├── gui_input.png
│   └── gui_result.png
│
└── README.md

```

## Program Requirements
Pastikan Python dan pip sudah terinstall pada sistem. Cek Python dengan <code>python --version</code> dan pip dengan <code>pip -V</code>.
### Program requirements untuk DNC-3-titik dan DNC-n-titik
1. <b> Matplotlib </b> <br>
    Berikut adalah command untuk mengunduh matplotlib.
    ```
    pip install matplotlib
    ```
### Program requirements untuk GUI
1. <b> Tkinter </b> <br>
    Berikut adalah command untuk mengunduh Tkinter.
    ```
    pip install tk
    ```
2. <b> Matplotlib </b> <br>
    Berikut adalah command untuk mengunduh matplotlib.
    ```
    pip install matplotlib
    ```
3. <b> PIL </b> <br>
    Berikut adalah command untuk mengunduh PIL.
    ```
    pip install Pillow
    ```

<h1 align="center"> <b> <span style="color:#E3A0BE">BRUTE FORCE </b> </h1>

## How to Run and Use (CLI ver.)
1. Clone repository ini dengan 
    ```
    git clone https://github.com/hiirrs/Tucil2_13522013_13522085.git
    ```
2. Buka folder repository pada terminal.
3. Pindah ke direktori *src* dengan `cd src`
4. Masukkan command berikut pada terminal:
    ```
    python brute-force.py
    ```
    Jangan lupa untuk adjust jenis python yang digunakan, apabila mengunakan python3, ubah python menjadi <code>python3</code>.
5. Masukkan jumlah titik, start point, control point(s), end point, serta jumlah iterasi.
6. Klik enter/return.
7. Animasi kurva akan ditampilkan pada sebuah window baru.

## How to Run Executable
Clone repository ini dengan 
    ```
    git clone https://github.com/hiirrs/Tucil2_13522013_13522085.git
    ```
### Windows
1. Buka folder repository pada terminal.
2. Pindah ke direktori *bin* dengan `cd bin`
3. Pindah ke direktori *windows* dengan `cd windows`
4. Masukkan command <code>dnc-3.exe</code> atau <code>dnc-n.exe</code>
### MacOS
1. Buka folder repository pada terminal.
2. Pindah ke direktori *bin* dengan `cd bin`
3. Pindah ke direktori *macOS* dengan `cd macOS`
4. Pindah ke direktori *dist* dengan `cd dist`
5. Masukkan command <code>./brute-force</code>


<h1 align="center"> <b> <span style="color:#E3A0BE">DIVIDE AND CONQUER </span> </b> </h1>

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
    Untuk menjalankan program kurva Bézier dengan 4 hingga n titik:
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
Clone repository ini dengan 
    ```
    git clone https://github.com/hiirrs/Tucil2_13522013_13522085.git
    ```
### Windows
1. Buka folder repository pada terminal.
2. Pindah ke direktori *bin* dengan `cd bin`
3. Pindah ke direktori *windows* dengan `cd windows`
4. Masukkan command <code>dnc-3.exe</code> atau <code>dnc-n.exe</code>
### MacOS
1. Buka folder repository pada terminal.
2. Pindah ke direktori *bin* dengan `cd bin`
3. Pindah ke direktori *macOS* dengan `cd macOS`
4. Pindah ke direktori *dist* dengan `cd dist`
5. Masukkan command <code>./dnc-3</code> atau <code>./dnc-n</code>
