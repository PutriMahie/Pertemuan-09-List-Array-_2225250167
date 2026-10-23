# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Putri Ayu Anisa Mahie  
**NIM:** 2225250167  
**Kelas:** 3F  

## Tujuan

Mengolah kumpulan data numerik menggunakan list Python, serta memahami cara mengakses, mengubah, menambahkan, menghapus, dan menghitung data dalam list.

## Struktur Program

File latihan dan praktik yang digunakan dalam pertemuan ini:

- `latihan/nilai.py` — latihan membuat dan mengakses list nilai.
- `latihan/manipulasi_nilai.py` — latihan mengubah, menambahkan, dan menghapus data dalam list.
- `latihan/statistik_nilai.py` — latihan menghitung total, rata-rata, nilai minimum, dan maksimum.
- `latihan/nilai_lulus.py` — latihan menentukan nilai yang memenuhi batas kelulusan.
- `praktik/analisis_nilai_mahasiswa.py` — program utama untuk menganalisis data nilai mahasiswa menggunakan fungsi dan list.

## Cara Menjalankan

Program dapat dijalankan melalui terminal VS Code dengan perintah:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

Jika menggunakan Windows dan perintah `python3` tidak tersedia, dapat menggunakan:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

## Test Case

| No. | Data | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | `[75, 80, 65, 90, 88]` | Rata-rata = 79.60 | Rata-rata = 79.60 | Berhasil |
| 2 | `[75, 55, 80, 60, 45, 90]` | Nilai lulus = `[75, 80, 60, 90]` | Nilai lulus = `[75, 80, 60, 90]` | Berhasil |
| 3 | `[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]` | Jumlah nilai lulus = 7 | Jumlah nilai lulus = 7 | Berhasil |

## Refleksi

Saya memahami bahwa indeks pada list Python dimulai dari angka `0`, sehingga data pertama dapat diakses menggunakan indeks `0`, sedangkan data terakhir dapat diakses menggunakan indeks `-1`.

Kesalahan yang berhasil saya perbaiki adalah **indentasi pada Python**, terutama pada bagian `if`, `for`, dan fungsi. Saya memahami bahwa kode yang berada di dalam fungsi, perulangan, atau kondisi harus menggunakan indentasi yang benar agar program dapat dijalankan.