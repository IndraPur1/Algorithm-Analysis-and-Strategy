def cek_bebek(jumlah, daftar):
    frekuensi = [0] * (max(daftar) + 1) if daftar else [0]
    for angka in daftar:
        frekuensi[angka] += 1
    
    batas = 2
    for hitung in frekuensi:
        if hitung > batas:
            return "NO"
    
    unik = sum(1 for x in frekuensi if x > 0)
    if unik * 2 < jumlah + 1:
        return "NO"
    
    return "YES"

panjang = int(input().strip())
data = list(map(int, input().strip().split()))
print(cek_bebek(panjang, data))