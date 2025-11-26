def cari_hilang_terbesar(arr, n):
    # Membuat array penanda (boolean) dengan panjang n+1,
    # untuk menandai apakah angka dari 0 hingga n muncul di array input.
    penanda = [False] * (n + 1)  # Inisialisasi semua bernilai False

    # Menandai angka-angka yang muncul di dalam array.
    # Jika suatu angka ada di array, ubah penanda[angka] menjadi True.
    for angka in arr:
        penanda[angka] = True

    # Melakukan pencarian dari angka terbesar (n) ke terkecil (0).
    # Tujuannya: mencari angka terbesar yang belum ditandai (masih False),
    # artinya angka tersebut hilang dari array.
    for i in range(n, -1, -1):
        if not penanda[i]:
            return i  # Mengembalikan angka terbesar yang hilang

n = int(input())
arr = list(map(int, input().split()))
print(angka(arr, n))