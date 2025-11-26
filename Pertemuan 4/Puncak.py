def puncak(arr):
    # Inisialisasi batas kiri dan kanan untuk binary search
    left, right = 0, len(arr) - 1

    # Lakukan pencarian selama batas kiri belum melewati batas kanan
    while left <= right:
        # Hitung indeks tengah
        mid = (left + right) // 2

        # Bandingkan elemen tengah dengan elemen setelahnya
        # Jika elemen tengah lebih kecil dari elemen setelahnya,
        # artinya kita berada di lereng naik, dan puncak ada di sebelah kanan
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            # Jika elemen tengah lebih besar dari elemen setelahnya,
            # artinya kita sudah melewati puncak atau berada di puncak,
            # maka cari ke kiri
            right = mid - 1

    # Setelah loop berhenti, nilai left akan menunjukkan indeks puncak
    # Tambah 1 karena output yang diminta kemungkinan berbasis 1 (1-based index)
    print(left + 1)

# --- Input ---
n = int(input())  # Input jumlah elemen array
arr = list(map(int, input().split()))  # Input elemen array

# --- Output ---
puncak(arr)  # Panggil fungsi untuk mencetak indeks puncak