# Fungsi untuk mengecek apakah A * B = C menggunakan algoritma Freivalds
def freivalds(A, B, C, n, k=5):
    for _ in range(k):  # Lakukan uji coba sebanyak k kali untuk meningkatkan akurasi
        # 1. Pilih vektor acak r (disederhanakan menjadi semua elemen 1)
        r = [1] * n  

        # 2. Hitung Br = B * r (perkalian matriks dengan vektor)
        Br = [sum(B[i][j] * r[j] for j in range(n)) for i in range(n)]

        # 3. Hitung AB_r = A * (B * r)
        AB_r = [sum(A[i][j] * Br[j] for j in range(n)) for i in range(n)]

        # 4. Hitung Cr = C * r
        Cr = [sum(C[i][j] * r[j] for j in range(n)) for i in range(n)]

        # 5. Jika AB_r ≠ Cr untuk suatu uji coba, maka A * B ≠ C
        if AB_r != Cr:
            return "Tidak Sama"

    # Jika lolos semua uji coba, kemungkinan besar A * B = C
    return "Sama"

# Input ukuran matriks
n = int(input())

# Input matriks A
A = [list(map(int, input().split())) for _ in range(n)]

# Input matriks B
B = [list(map(int, input().split())) for _ in range(n)]

# Input matriks C
C = [list(map(int, input().split())) for _ in range(n)]

# Jalankan algoritma Freivalds dan cetak hasilnya
print(freivalds(A, B, C, n))
