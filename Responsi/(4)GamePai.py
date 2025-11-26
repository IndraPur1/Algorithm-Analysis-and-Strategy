# Fungsi quicksort untuk mengurutkan array tanpa menggunakan import
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Fungsi binary search manual untuk menghitung jumlah elemen <= skor Pai
def binarysearch(arr, s):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= s:
            left = mid + 1
        else:
            right = mid
    return left  # posisi pertama elemen > s = jumlah elemen <= s

# Fungsi untuk menghitung total hadiah dari semua hari
def total_hadiah(arr, S):
    arr = quicksort(arr)  # Urutkan skor minimal hadiah
    total = 0
    for skor_pai in S:
        # Perbaikan di sini: skor_pai dikirim ke binarysearch, bukan seluruh list S
        hadiah_hari_ini = binarysearch(arr, skor_pai)
        total += hadiah_hari_ini
    return total

# --- Input dari pengguna ---
N, K = map(int, input().split())          # N = jumlah skor hadiah, K = jumlah hari
arr = list(map(int, input().split()))     # daftar skor minimal hadiah
S = list(map(int, input().split()))       # skor harian yang didapat Pai

# Cetak total hadiah
print(total_hadiah(arr, S))
