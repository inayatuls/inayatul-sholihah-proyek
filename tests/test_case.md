# Test Case Proyek

| ID | Fitur | Input | Expected | Actual | Status |
|---|---|---|---|---|---|
| TC01 | Rata-rata normal | [70, 80, 90] | 80.0 | 80.0 | PASS |
| TC02 | Data kosong | [] | 0 | 0 | PASS |
| TC03 | Nilai batas | 60 | [60] | [60] | PASS |
| TC04 | Nilai di bawah batas | 59 | [] | [] | PASS |
| TC05 | Input tidak valid | Citra,abc | Data tidak valid diabaikan | Nilai tidak valid diabaikan | PASS |
| TC06 | Analisis data | Ayu,85; Budi,78 | Rata-rata 81.5, minimum 78, maksimum 85, tuntas 2 | Rata-rata 81.5, minimum 78, maksimum 85, tuntas 2 | PASS |