# Piagam Proyek — The Build

## Bagian A: Identitas Proyek

### 1. Nama Aplikasi
**BookHub** — Aplikasi pencatatan dan pencarian koleksi buku pribadi.

### 2. Masalah yang Diselesaikan
Sulitnya melacak buku yang dimiliki, dipinjam, atau ingin dibeli. 
Pencatatan manual di buku tulis sering hilang dan tidak bisa dicari dengan cepat.

### 3. Pengguna Sasaran
- Mahasiswa dan dosen yang gemar membaca
- Pegawai perpustakaan kecil
- Kolektor buku pribadi

### 4. Fitur Utama
1. Tambah buku baru (dengan validasi ISBN 13 digit)
2. Cari buku berdasarkan judul atau penulis
3. Lihat detail buku berdasarkan ID
4. (Akan datang) Edit dan hapus buku

### 5. Batasan (Out of Scope)
- Tidak ada fitur login/autentikasi di tahap ini
- Tidak ada integrasi dengan API eksternal (Google Books, dll)
- Data disimpan di memori (in-memory), belum persisten ke database