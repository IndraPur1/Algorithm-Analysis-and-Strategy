# Fungsi utama untuk menghitung jumlah inversi dalam array
def count_inversions(arr):
    # Membuat array sementara (temp) yang akan digunakan saat proses merge
    temp = [0] * len(arr)
    # Memanggil fungsi merge_sort dan mengembalikan jumlah inversi
    return merge_sort(arr, temp, 0, len(arr) - 1)

# Fungsi rekursif untuk melakukan merge sort dan menghitung inversi
def merge_sort(arr, temp, left, right):
    count = 0
    if left < right:
        # Menentukan titik tengah array
        mid = (left + right) // 2

        # Menghitung jumlah inversi di bagian kiri
        count += merge_sort(arr, temp, left, mid)

        # Menghitung jumlah inversi di bagian kanan
        count += merge_sort(arr, temp, mid + 1, right)

        # Menghitung jumlah inversi saat proses merge dua bagian
        count += merge(arr, temp, left, mid, right)

    return count

# Fungsi untuk melakukan merge dua bagian array yang sudah terurut,
# sekaligus menghitung jumlah inversi yang terjadi
def merge(arr, temp, left, mid, right):
    i = left      # Pointer untuk bagian kiri
    j = mid + 1   # Pointer untuk bagian kanan
    k = left      # Pointer untuk array temp
    count = 0     # Variabel untuk menyimpan jumlah inversi

    # Menggabungkan dua bagian array sambil menghitung jumlah inversi
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            # Jika elemen di kiri lebih besar dari elemen di kanan,
            # maka semua elemen dari arr[i] sampai arr[mid] akan membentuk inversi
            count += (mid - i + 1)
            j += 1
        k += 1

    # Menyalin sisa elemen dari bagian kiri (jika masih ada)
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Menyalin sisa elemen dari bagian kanan (jika masih ada)
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Menyalin isi array temp ke array asli
    for idx in range(left, right + 1):
        arr[idx] = temp[idx]

    return count

# --- Input dari pengguna ---
n = int(input())                             # Membaca jumlah elemen array
arr = list(map(int, input().split()))       # Membaca elemen array

# --- Output jumlah inversi ---
print(count_inversions(arr))