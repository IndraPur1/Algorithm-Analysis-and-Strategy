def awal(data, target):
    kiri = 0
    kanan = len(data) - 1
    hasil = -1
    while kiri <= kanan:
        mid = (kiri + kanan) // 2
        if data[mid] == target:
            hasil = mid
            kanan = mid - 1
        elif data[mid] < target:
            kiri = mid + 1
        else:
            kanan = mid - 1
    return hasil

def akhir(data, target):
    kiri = 0
    kanan = len(data) - 1
    hasil = -1
    while kiri <= kanan:
        mid = (kiri + kanan) // 2
        if data[mid] == target:
            hasil = mid
            kiri = mid + 1
        elif data[mid] < target:
            kiri = mid + 1
        else:
            kanan = mid - 1
    return hasil

n, k = map(int, input().split())
data = list(map(int, input().split()))

awal = awal(data, k)
akhir = akhir(data, k)

if awal == -1 and akhir == -1:
    print("-1 -1")
else:
    print(awal + 1, akhir + 1)
