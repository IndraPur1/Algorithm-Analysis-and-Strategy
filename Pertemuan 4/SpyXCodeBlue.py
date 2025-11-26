# Fungsi untuk menghitung waktu minimum yang dibutuhkan agar petunjuk terkumpul
def codeblu(arr, c):
    # Inisialisasi batas pencarian waktu
    kiri = 1  # Waktu minimum mulai dari 1 menit (bisa juga 0 jika ingin lebih longgar)
    # Batas maksimum waktu: agen dengan peringkat tertinggi mengumpulkan semua petunjuk
    kanan = max(arr) * c * c
    # Variabel hasil untuk menyimpan waktu minimum yang valid
    hasil = kanan

    # Binary search untuk mencari waktu minimum
    while kiri <= kanan:
        mid = (kiri + kanan) // 2  # Waktu tengah (coba)

        total_petunjuk = 0  # Total petunjuk yang bisa dikumpulkan dalam waktu mid

        # Hitung berapa banyak petunjuk yang bisa dikumpulkan semua agen dalam waktu mid
        for nilai in arr:
            if nilai == 0:
                continue  # Jika peringkat agen 0, lewati agar tidak error pembagian nol

            # Menghitung maksimal petunjuk yang bisa dikumpulkan agen ini dalam waktu mid
            # Rumus: waktu = nilai * n² → n = sqrt(waktu / nilai)
            # Jadi total petunjuk = floor(sqrt(mid / nilai))
            max_petunjuk = int((mid / nilai) ** 0.5)

            total_petunjuk += max_petunjuk  # Tambah ke total petunjuk dari semua agen

        # Jika total petunjuk sudah cukup atau lebih dari yang dibutuhkan
        if total_petunjuk >= c:
            hasil = mid         # Simpan waktu ini sebagai kandidat hasil
            kanan = mid - 1     # Coba cari waktu lebih kecil (optimasi)
        else:
            kiri = mid + 1      # Jika belum cukup, cari waktu yang lebih besar

    # Setelah binary search selesai, hasil berisi waktu minimum yang bisa digunakan
    return hasil

# --- Input dari pengguna ---
# Membaca array peringkat agen
arr = [int(x) for x in input().split()]

# Membaca jumlah total petunjuk yang harus dikumpulkan
c = int(input())

# Cetak waktu minimum yang diperlukan
print(codeblu(arr, c))
