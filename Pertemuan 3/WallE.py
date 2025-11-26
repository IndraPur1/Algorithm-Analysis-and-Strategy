def merge_sort_interval(data):
    if len(data) <= 1:
        return data
    tengah = len(data) // 2
    kiri = merge_sort_interval(data[:tengah])
    kanan = merge_sort_interval(data[tengah:])
    return gabung(kiri, kanan)

def gabung(kiri, kanan):
    hasil = []
    i = 0
    j = 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i][0] <= kanan[j][0]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1
    while i < len(kiri):
        hasil.append(kiri[i])
        i += 1
    while j < len(kanan):
        hasil.append(kanan[j])
        j += 1
    return hasil

def hitung_grup_minimum(intervals):
    intervals = merge_sort_interval(intervals)
    akhir_grup = []

    for interval in intervals:
        ditempatkan = False
        for i in range(len(akhir_grup)):
            if interval[0] > akhir_grup[i]:
                akhir_grup[i] = interval[1]
                ditempatkan = True
                break
        if not ditempatkan:
            akhir_grup.append(interval[1])
    return len(akhir_grup)

baris = input()
intervals = eval(baris)

print(hitung_grup_minimum(intervals))