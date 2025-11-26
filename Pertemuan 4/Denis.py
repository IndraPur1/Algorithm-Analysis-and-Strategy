# Fungsi rekursif untuk mencari jumlah bola minimum yang total angkanya tepat mencapai H
# Menggunakan teknik Decrease and Conquer + Memoization (top-down dynamic programming)

def DenisBeban(H, arr, temp):
    # Basis kasus: jika target H = 0, maka tidak perlu bola sama sekali
    if H == 0:
        return 0

    # Basis kasus: jika H negatif, kombinasi ini tidak valid
    if H < 0:
        return float('inf')  # dianggap tak terhingga agar tidak dipilih sebagai solusi minimum

    # Jika nilai H sudah pernah dihitung sebelumnya, langsung ambil dari memo temp (caching)
    if H in temp:
        return temp[H]

    # Inisialisasi jumlah minimum bola sebagai tak terhingga
    min_bola = float('inf')

    # Coba semua kemungkinan bola yang bisa diambil dari daftar
    for i in arr:
        # Kurangi H dengan nilai bola i, lalu tambah 1 (karena kita menggunakan 1 bola tersebut)
        # Ambil nilai minimum dari semua kemungkinan
        min_bola = min(min_bola, DenisBeban(H - i, arr, temp) + 1)

    # Simpan hasil untuk H agar tidak dihitung ulang (memoization)
    temp[H] = min_bola

    # Kembalikan jumlah bola minimum yang diperlukan untuk mencapai H
    return min_bola

# -----------------------------
# Input dari pengguna
N, H = map(int, input().split())           # N = jumlah jenis bola, H = total angka target
arr = list(map(int, input().split()))      # arr = daftar angka bola yang tersedia

# Panggil fungsi dengan H, daftar bola, dan dictionary kosong sebagai penyimpanan cache
hasil = DenisBeban(H, arr, {})

# Jika hasil = tak terhingga, berarti tidak mungkin mencapai H, cetak -1
# Jika hasil valid, cetak jumlah bola minimum
print(hasil if hasil != float('inf') else -1)
