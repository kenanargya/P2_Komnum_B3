# P2_Komnum_B3

#### Anggota Kelompok 3
| | Nama  | NRP |
| ------------- | ------------- | ------------- |
| 1 | Ken Anargya Alkausar | 5025211168 |
| 2 | Faiz haq noviandra  | 5025211132 |
| 3 | Muhammad Arkan K. D  | 5025211236 |

## Metode Integrasi Romberg
Integrasi Romberg adalah teknik yang digunakan dalam integrasi numerik. Integrasi Romberg digunakan dalam integrasi numerik untuk menganalisis kasus di mana fungsi integrasi tersedia. Teknik ini menganalisis kasus di mana fungsi yang dapat disematkan tersedia. Keuntungan dari teknik ini adalah menghasilkan nilai dari fungsi yang digunakan untuk mengembangkan keuntungan menghasilkan nilai dari fungsi yang digunakan untuk mengembangkan metode integrasi numerik yang efisien. Integrasi Romberg didasarkan pada model integrasi numerik yang efisien. Integrasi Romberg didasarkan pada ekstrapolasi Richardson, suatu metode yang menggabungkan dua perkiraan integral secara numerik untuk mendapatkan nilai ketiga yang lebih akurat.

## Proses Integrasi Romberg
![image](https://user-images.githubusercontent.com/92387421/209123747-50fe2822-f8c4-462b-a881-efa07d8a5eef.png)

Kolom pertama pada tabel memuat hampiran integral tentu dengan menggunakan aturan trapesium rekursif. Kolom kedua merupakan hampiran integral yang sama dengan aturan Simpson rekursif (perbaikan pertama). Kolom ketiga merupakan hampiran integral yang sama dengan dengan aturan Boole rekursif (perbaikan kedua). Kolom keempat merupakan perbaikan ketiga, Demikian seterusnya.


![image](https://user-images.githubusercontent.com/92387421/209201643-ff142159-da78-428f-a839-fdcf3d578d49.png)

## Penjelasan Singkat
  1.  Pertama-tama dilakukan import modul integrate dari library scipy pada python
  2.  Kemudian dibuat variabel function untuk menginput fungsi yang akan dijalankan
  3.  Lalu didefinisikan fungsi f dengan parameter x, dengan f berisikan fungsi yang telah diinput dari variabel function
  4.  Selanjutnya dibuat variabel x untuk menginput batas bawah integrasi
  5.  Kemudian dibuat variabel y untuk menginput batas atas integrasi
  6.  Lalu dibuat variabel romberg sebagai fungsi dari integrasi romberg yang berisikan modul integrate dari library scipy dengan parameter yang berisikan fungsi f dan variabel x dan y
  7.  Kemudian output akan ditampilkan dengan show = True
