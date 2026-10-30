def baca_data(path):
    data = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for baris in file:
                bagian = baris.strip().split(",")

                if len(bagian) != 2:
                    print("Format data tidak valid.")
                    continue

                nama = bagian[0].strip()

                try:
                    nilai = int(bagian[1].strip())
                except ValueError:
                    print(f"Nilai tidak valid: {bagian[1].strip()}")
                    continue

                if nama and 0 <= nilai <= 100:
                    data.append({
                        "nama": nama,
                        "nilai": nilai
                    })
                else:
                    print("Nilai harus antara 0 sampai 100.")

    except FileNotFoundError:
        print("File tidak ditemukan.")

    return data