def onizuka(arr):
    left, right = 0, len(arr) - 1  # Inisialisasi batas kiri (left) dan kanan (right)

    # Binary Search
    while left <= right:
        mid = (left + right) // 2  # Hitung posisi tengah
        
        if arr[mid] == mid:
            # Jika arr[mid] == mid, berarti semua elemen sebelum mid benar.
            # Pindah pencarian ke kanan untuk menemukan yang hilang.
            left = mid + 1
        else:
            # Jika arr[mid] != mid, berarti ada yang hilang di sebelah kiri atau mid itu sendiri.
            # Pindah pencarian ke kiri.
            right = mid - 1

    # Left sekarang menunjukkan posisi pertama yang tidak sesuai dengan index.
    return left  # ID murid yang hilang

# --- Input ---
n = int(input())  # Masukkan jumlah murid N
arr = list(map(int, input().split()))  # Masukkan list ID murid dalam urutan naik

# --- Output ---
print(onizuka(arr))  # Cetak hasil ID murid yang hilang