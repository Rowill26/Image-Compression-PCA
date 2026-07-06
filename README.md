# 🖼️ Image Compression PCA

Aplikasi web sederhana untuk **kompresi gambar menggunakan algoritma Principal Component Analysis (PCA)**, diimplementasikan dari nol (manual, tanpa `sklearn`) menggunakan NumPy. Proyek ini dibuat sebagai tugas mata kuliah **Aljabar Linear**.

Unggah gambar, atur jumlah komponen utama yang ingin dipertahankan, dan lihat hasil kompresinya secara langsung — lengkap dengan runtime eksekusi dan persentase kompresi.

---

## ✨ Fitur

- 📤 Unggah gambar (JPG, PNG, dll.) langsung dari browser
- 🎚️ Atur jumlah komponen utama (k) yang digunakan untuk rekonstruksi
- 🖼️ Perbandingan visual **Before** vs **After** secara berdampingan
- ⏱️ Menampilkan waktu eksekusi algoritma (runtime)
- 📉 Menampilkan persentase kompresi data
- ⬇️ Unduh langsung hasil gambar yang telah dikompresi
- 🧮 Implementasi PCA manual (mean centering, matriks kovarians, dekomposisi eigen) — bukan library siap pakai

---

## 🧠 Cara Kerja Singkat

Setiap channel warna (R, G, B) dari gambar diperlakukan sebagai matriks tersendiri, lalu direduksi dimensinya menggunakan PCA:

1. Hitung rata-rata (mean) tiap kolom matriks, lalu pusatkan datanya
2. Bentuk matriks kovarians dari data yang telah dipusatkan
3. Hitung eigenvalue & eigenvector dari matriks kovarians
4. Urutkan eigenvector berdasarkan eigenvalue terbesar (descending)
5. Ambil `k` komponen utama teratas, proyeksikan, lalu rekonstruksi kembali data
6. Gabungkan kembali ketiga channel menjadi satu gambar RGB utuh

Semakin kecil nilai `k`, semakin besar kompresinya — namun detail gambar yang hilang juga akan semakin banyak.

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
|---|---|
| Backend | Python, Flask |
| Komputasi | NumPy (implementasi PCA manual) |
| Pengolahan Citra | Pillow (PIL) |
| Keamanan Upload | Werkzeug (`secure_filename`) |
| Frontend | HTML, CSS, JavaScript (vanilla) |

---

## 📁 Struktur Proyek

```
Image-Compression-PCA/
├── static/
│   ├── uploads/          # Gambar asli yang diunggah pengguna
│   └── compressed/       # Gambar hasil kompresi
├── templates/
│   └── index.html        # Halaman utama aplikasi
├── app.py                 # Routing & logika server Flask
├── main.py                 # Implementasi algoritma PCA
└── README.md
```

---

## 🚀 Instalasi & Menjalankan Secara Lokal

### 1. Clone repository
```bash
git clone https://github.com/<username>/Image-Compression-PCA.git
cd Image-Compression-PCA
```

### 2. Buat virtual environment (opsional tapi disarankan)
```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3. Install dependencies
```bash
pip install flask numpy pillow werkzeug
```

> 💡 Jika kamu punya file `requirements.txt`, cukup jalankan `pip install -r requirements.txt`

### 4. Jalankan aplikasi
```bash
python app.py
```

### 5. Buka di browser
```
http://127.0.0.1:5000
```

---

## 📖 Cara Menggunakan

1. Buka aplikasi di browser
2. Klik area upload dan pilih gambar yang ingin dikompresi
3. Geser slider **Image Compression Rate** untuk menentukan jumlah komponen utama
4. Klik **Process Image**
5. Bandingkan hasil **Before** dan **After**, lihat metrik runtime & persentase kompresi
6. Klik tombol **Download** untuk mengunduh hasil kompresi

---

## 👥 Kontributor

Proyek ini dikembangkan untuk tugas Aljabar Linear — Program Studi Informatika, Fakultas Teknologi Informasi dan Sains Data, Universitas Sebelas Maret.

| Nama | NIM |
|---|---|
| Khalisah Nur Ihsaniyah | L0125048 |
| Syifa Kaila Putri | L0125068 |
| Rolland William Yohanes George | L0125113 |

**Dosen Pengampu:** Prof. Drs. Bambang Harjito, M.App.Sc., Ph.D.

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik/pembelajaran. Bebas digunakan dan dimodifikasi untuk tujuan edukasi.
