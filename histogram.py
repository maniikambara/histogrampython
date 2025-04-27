import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def hitung_histogram(gambar):
    # Menghitung histogram citra
    histogram = cv2.calcHist([gambar], [0], None, [256], [0, 256])
    histogram_normalisasi = histogram / float(gambar.size)
    return histogram.flatten(), histogram_normalisasi.flatten()

def hitung_statistik(histogram_normalisasi):
    # Menghitung statistik: rata-rata, variansi, dan deviasi standar
    rata_rata = np.sum(histogram_normalisasi * np.arange(256))
    varian = np.sum(histogram_normalisasi * (np.arange(256) - rata_rata)**2)
    deviasi_standar = np.sqrt(varian)
    return round(rata_rata, 2), round(varian, 2), round(deviasi_standar, 2)

def interpretasi_statistik(varian):
    # Interpretasi kontras citra berdasarkan variansi
    if varian < 500:
        kontras = "Kontras citra rendah"
    elif 500 <= varian < 1000:
        kontras = "Kontras citra sedang"
    else:
        kontras = "Kontras citra tinggi"
    
    return kontras

def tampilkan_histogram(histograms, histogram_normalisasis, juduls):
    # Menampilkan grafik histogram dengan label sumbu X dan Y
    plt.figure(figsize=(12, 6))
    for i, (histogram, histogram_normalisasi, judul) in enumerate(zip(histograms, histogram_normalisasis, juduls)):
        plt.subplot(1, 3, i+1)  # Membagi menjadi 3 bagian dalam satu baris
        plt.plot(histogram, color='blue', label="Jumlah Pixel")
        plt.plot(histogram_normalisasi, color='yellow', label="Distribusi Normalisasi")
        plt.title(judul)
        
        # Menambahkan label pada sumbu X dan Y
        plt.xlabel('Nilai Intensitas Pixel')  # Label sumbu X
        plt.ylabel('Frekuensi Pixel')  # Label sumbu Y
        
        plt.legend()

    plt.tight_layout()
    plt.show()

def proses_gambar(path_gambar, mode):
    gambar = cv2.imread(path_gambar)
    
    if gambar is None:
        messagebox.showerror("Error", "Gambar tidak ditemukan atau format tidak didukung!")
        return

    hasil_text.delete(1.0, END)  # Menghapus hasil sebelumnya
    if mode == "RGB":
        gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)  # Mengubah ke RGB
    else:
        gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)  # Mengubah ke Grayscale

    gambar_pil = Image.fromarray(gambar_rgb)
    gambar_pil.thumbnail((200, 200))  # Mengubah ukuran untuk preview
    gambar_tk = ImageTk.PhotoImage(gambar_pil)
    
    label_preview.config(image=gambar_tk)
    label_preview.image = gambar_tk  # Menyimpan referensi gambar untuk mencegah penghapusan

    if mode == "RGB":
        histograms = []
        histogram_normalisasis = []
        juduls = []
        
        saluran = ('Red', 'Green', 'Blue')
        for i, channel in enumerate(saluran):
            histogram_saluran, histogram_normalisasi = hitung_histogram(gambar_rgb[:, :, i])
            rata_rata, varian, deviasi_standar = hitung_statistik(histogram_normalisasi)
            kontras = interpretasi_statistik(varian)
            
            hasil_text.insert(END, f"\nStatistik Saluran {channel}:\n")
            hasil_text.insert(END, f"Rata-rata {channel}: {rata_rata}\n")
            hasil_text.insert(END, f"Varian {channel}: {varian}\n")
            hasil_text.insert(END, f"Deviasi Standar {channel}: {deviasi_standar}\n")
            hasil_text.insert(END, f"Interpretasi: {kontras}\n")
            
            histograms.append(histogram_saluran)
            histogram_normalisasis.append(histogram_normalisasi)
            juduls.append(f"Histogram {channel}")
        
        tampilkan_histogram(histograms, histogram_normalisasis, juduls)
        
    else:
        histogram_gray, histogram_normalisasi = hitung_histogram(gambar_rgb)
        rata_rata, varian, deviasi_standar = hitung_statistik(histogram_normalisasi)
        kontras = interpretasi_statistik(varian)
        
        hasil_text.insert(END, f"\nStatistik Citra Grayscale:\n")
        hasil_text.insert(END, f"Rata-rata Grayscale: {rata_rata}\n")
        hasil_text.insert(END, f"Varian Grayscale: {varian}\n")
        hasil_text.insert(END, f"Deviasi Standar Grayscale: {deviasi_standar}\n")
        hasil_text.insert(END, f"Interpretasi: {kontras}\n")
        
        tampilkan_histogram([histogram_gray], [histogram_normalisasi], ["Histogram Grayscale"])

def unggah_gambar():
    path_gambar = filedialog.askopenfilename(filetypes=[("File Gambar", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if path_gambar:
        mode = mode_var.get()
        proses_gambar(path_gambar, mode)

root = Tk()
root.title("Penghitung Histogram dan Statistik Citra")

mode_var = StringVar(value="RGB")
radio_rgb = Radiobutton(root, text="RGB", variable=mode_var, value="RGB")
radio_rgb.pack(anchor=W)
radio_grayscale = Radiobutton(root, text="Grayscale", variable=mode_var, value="Grayscale")
radio_grayscale.pack(anchor=W)

tombol_upload = Button(root, text="Pilih Gambar", command=unggah_gambar)
tombol_upload.pack(pady=20)

hasil_text = Text(root, width=80, height=10)
hasil_text.pack(pady=20)

label_preview = Label(root)
label_preview.pack(pady=20)

root.mainloop()