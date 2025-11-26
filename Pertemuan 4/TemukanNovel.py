def find_range(arr, target):
    res = [-1, -1]  # Inisialisasi hasil awal jika target tidak ditemukan

    # --- Cari posisi pertama (index awal target) ---
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Hitung posisi tengah
        if arr[mid] < target:
            left = mid + 1  # Target pasti di kanan
        else:
            if arr[mid] == target:
                res[0] = mid  # Simpan kemungkinan posisi pertama
            right = mid - 1  # Terus cari ke kiri untuk posisi awal

    # --- Cari posisi terakhir (index akhir target) ---
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Hitung posisi tengah
        if arr[mid] > target:
            right = mid - 1  # Target pasti di kiri
        else:
            if arr[mid] == target:
                res[1] = mid  # Simpan kemungkinan posisi terakhir
            left = mid + 1  # Terus cari ke kanan untuk posisi akhir

    # Jika tidak ditemukan sama sekali, res tetap [-1, -1]
    return res if res[0] != -1 else [-1, -1]

# --- Bagian Input dan Output ---
arr = list(map(int, input().split()))  # Input array yang sudah terurut
target = int(input())                  # Input nilai target yang dicari
print(find_range(arr, target))         # Cetak hasil dalam bentuk [awal, akhir]