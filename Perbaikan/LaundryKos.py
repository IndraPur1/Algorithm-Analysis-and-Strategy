# Fungsi untuk mencari lantai tempat kamar x berada
# Menggunakan binary search pada array prefix sum
def find_lantai(prefix, x):
    left = 0
    right = len(prefix) - 1
    while left <= right:
        mid = (left + right) // 2
        if x <= prefix[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left  # Mengembalikan indeks lantai tempat kamar x berada

# Membaca input jumlah lantai (N) dan jumlah kamar yang dicari (M)
NM = input().split()
N = int(NM[0])
M = int(NM[1])

# Membaca banyak kamar di setiap lantai (array F)
F = list(map(int, input().split()))

# Membaca daftar kamar yang ingin diketahui posisinya (array X)
X = list(map(int, input().split()))

# Membuat prefix sum dari jumlah kamar per lantai
# prefix[i] = jumlah total kamar dari lantai 0 sampai lantai i
prefix = [0] * N
prefix[0] = F[0]
for i in range(1, N):
    prefix[i] = prefix[i - 1] + F[i]

# Untuk setiap nomor kamar yang dicari
for x in X:
    # Cari lantai tempat kamar x berada menggunakan binary search
    lantai = find_lantai(prefix, x)

    # Hitung kamar ke-berapa di lantai tersebut
    # Jika lantai = 0, berarti kamar_ke = x (karena belum dikurangi apa pun)
    # Jika lantai > 0, kurangi dengan jumlah kamar sampai lantai sebelumnya
    kamar_ke = x if lantai == 0 else x - prefix[lantai - 1]

    # Output hasil: lantai (dimulai dari 1) dan nomor kamar di lantai itu
    print(lantai + 1, kamar_ke)
