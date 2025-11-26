# Fungsi gampang untuk mencari target dalam array terurut (bisa naik atau turun)
def gampang(arr, target):
    # Jika array kosong, langsung cetak "Tidak ditemukan"
    if not arr:
        print('"Tidak ditemukan"')
    else:
        # Deteksi apakah array urut naik (ascending) atau turun (descending)
        asc = arr[0] < arr[-1]
        
        # Inisialisasi batas kiri (l) dan kanan (r) untuk binary search
        l, r = 0, len(arr) - 1
        
        # Lakukan pencarian selama batas kiri <= kanan
        while l <= r:
            # Hitung indeks tengah
            m = (l + r) // 2
            
            # Jika elemen tengah adalah target, cetak indeks dan hentikan pencarian
            if arr[m] == target:
                print(m)
                break
            
            # Jika array urut naik dan target lebih kecil dari elemen tengah
            # atau array urut turun dan target lebih besar dari elemen tengah
            # maka target ada di sebelah kiri, geser batas kanan
            if (asc and target < arr[m]) or (not asc and target > arr[m]):
                r = m - 1
            else:
                # Jika tidak, target ada di sebelah kanan, geser batas kiri
                l = m + 1
        else:
            # Jika loop selesai tanpa menemukan target, cetak "Tidak ditemukan"
            print('"Tidak ditemukan"')

# Input array dan target
arr = eval(input())
target = int(input()) 

# Panggil fungsi gampang untuk mencari target
gampang(arr, target)
