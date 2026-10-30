# Program Rekap dan Analisis Nilai Matematika Kelas

## Deskripsi

Program ini membantu guru matematika membaca data nilai siswa, memvalidasi nilai, menghitung statistik, menentukan status ketuntasan, dan menyimpan laporan.

## Fitur

- Membaca data nilai siswa dari file.
- Memvalidasi nilai siswa.
- Menghitung rata-rata, nilai minimum, dan maksimum.
- Menentukan jumlah siswa tuntas dan belum tuntas.
- Menampilkan hasil analisis nilai.
- Menyimpan laporan hasil analisis ke file.

## Persyaratan

- Python 3.x

## Cara Menjalankan

Jalankan melalui terminal VS Code dari folder utama proyek:

```bash
python3 main.py
```

## Struktur Folder

- `main.py`: file utama program.
- `src/`: berisi modul input, proses, dan output.
- `data/`: menyimpan data nilai contoh.
- `tests/`: menyimpan test case.
- `docs/screenshot/`: menyimpan dokumentasi screenshot proyek.
- `proposal.md`: proposal proyek Pertemuan 14.

## Test Case

| ID | Fitur | Input | Expected | Actual | Status |
|---|---|---|---|---|---|
| TC01 | Rata-rata normal | [70, 80, 90] | 80.0 | 80.0 | PASS |
| TC02 | Data kosong | [] | 0 | 0 | PASS |
| TC03 | Nilai batas | 60 | [60] | [60] | PASS |
| TC04 | Nilai di bawah batas | 59 | [] | [] | PASS |
| TC05 | Input tidak valid | Citra,abc | Data tidak valid diabaikan | Nilai tidak valid: abc, data diabaikan | PASS |
| TC06 | Analisis data | Ayu,85; Budi,78 | Rata-rata 81.5, minimum 78, maksimum 85, tuntas 2 | Rata-rata 81.5, minimum 78, maksimum 85, tuntas 2 | PASS |

## Known Issues

Belum ada known issue yang dicatat pada pengujian ini.

## Anggota dan Kontribusi

Pengerjaan dilakukan secara individu, meliputi perancangan, implementasi, pengujian, debugging, dan dokumentasi proyek.

## Referensi/Bantuan

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 14.
- Bahan Ajar Algoritma dan Pemrograman Pertemuan 15.
- ChatGPT sebagai bantuan dalam memahami materi dan penyusunan kode.