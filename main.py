from pathlib import Path
from src.input_data import baca_data
from src.proses import hitung_rata_rata, status_lulus, ringkasan
from src.output import tampilkan_ringkasan, simpan_laporan


def main():
    print("PENGUJIAN PROGRAM")

    assert hitung_rata_rata([70, 80, 90]) == 80
    print("TC01 PASS - Rata-rata normal")

    assert hitung_rata_rata([]) == 0
    print("TC02 PASS - Data kosong")

    assert status_lulus([60]) == [60]
    print("TC03 PASS - Nilai batas 60")

    assert status_lulus([59]) == []
    print("TC04 PASS - Nilai di bawah batas")

    folder_proyek = Path(__file__).parent
    path_data = folder_proyek / "data" / "contoh_data.txt"
    path_laporan = folder_proyek / "laporan.txt"

    data = baca_data(path_data)

    assert len(data) == 2
    print("TC05 PASS - Input tidak valid ditangani")

    nilai = [item["nilai"] for item in data]
    hasil = ringkasan(nilai)

    assert hasil == {
        "jumlah": 2,
        "rata_rata": 81.5,
        "minimum": 78,
        "maksimum": 85,
        "lulus": 2
    }
    print("TC06 PASS - Analisis data")

    tampilkan_ringkasan(hasil)
    simpan_laporan(hasil, path_laporan)

    print("\nLaporan berhasil disimpan.")
    print("Semua 6 test case berhasil.")


if __name__ == "__main__":
    main()