def tampilkan_ringkasan(hasil):
    print("\nHASIL ANALISIS NILAI")
    print("Jumlah siswa:", hasil["jumlah"])
    print("Rata-rata:", hasil["rata_rata"])
    print("Nilai minimum:", hasil["minimum"])
    print("Nilai maksimum:", hasil["maksimum"])
    print("Jumlah siswa tuntas:", hasil["lulus"])
    print("Jumlah siswa belum tuntas:", hasil["jumlah"] - hasil["lulus"])


def simpan_laporan(hasil, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write("LAPORAN ANALISIS NILAI MATEMATIKA\n")
        file.write(f"Jumlah siswa: {hasil['jumlah']}\n")
        file.write(f"Rata-rata: {hasil['rata_rata']}\n")
        file.write(f"Nilai minimum: {hasil['minimum']}\n")
        file.write(f"Nilai maksimum: {hasil['maksimum']}\n")
        file.write(f"Jumlah siswa tuntas: {hasil['lulus']}\n")
        file.write(
            f"Jumlah siswa belum tuntas: {hasil['jumlah'] - hasil['lulus']}\n"
        )