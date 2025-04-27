# Penghitung Histogram dan Statistik Citra

Program ini adalah aplikasi Python dengan antarmuka grafis (GUI) yang digunakan untuk menghitung dan menampilkan histogram dari citra (gambar) serta melakukan analisis statistik. Program ini mendukung citra dalam format RGB dan Grayscale.

## Fitur Utama

1. **Pemilihan Gambar**: Pengguna dapat memilih gambar yang ingin dianalisis, baik dalam format RGB maupun Grayscale.
2. **Histografi**: Program menghitung dan menampilkan histogram dari gambar yang dipilih.
3. **Normalisasi Histogram**: Histogram yang ditampilkan juga mencakup normalisasi untuk menunjukkan frekuensi kemunculan nilai intensitas pixel.
4. **Statistik**:
   - **Rata-rata (Mean)**: Menampilkan rata-rata nilai intensitas dari gambar.
   - **Variansi (Variance)**: Menampilkan variansi yang menggambarkan sebaran nilai intensitas di sekitar rata-rata.
   - **Deviasi Standar (Standard Deviation)**: Menampilkan deviasi standar yang menunjukkan jarak rata-rata pixel terhadap nilai rata-rata.
5. **Interpretasi Kontras Citra**: Program memberikan interpretasi kontras citra berdasarkan nilai variansi dan deviasi standar.

## Persyaratan

Program ini memerlukan beberapa pustaka Python untuk berjalan dengan baik. Berikut adalah daftar pustaka yang perlu diinstal:

- `opencv-python` (untuk pemrosesan citra)
- `numpy` (untuk perhitungan numerik)
- `matplotlib` (untuk menampilkan grafik histogram)
- `Pillow` (untuk memanipulasi gambar di GUI)
- `tkinter` (untuk membuat antarmuka grafis)

Untuk menginstal pustaka yang diperlukan, Anda dapat menggunakan `pip` dengan menjalankan perintah berikut:

```bash
pip install opencv-python numpy matplotlib Pillow
