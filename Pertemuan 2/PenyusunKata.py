def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

def permutasi(arr):
    if len(arr) == 0:
        return [[]]
    hasil = []
    for i in range(len(arr)):
        sisa = arr[:i] + arr[i+1:]
        for p in permutasi(sisa):
            hasil.append([arr[i]] + p)
    return hasil

def PenyusunanKata(teks, batasan):
    teks = list(teks)
    posisi_tetap = {pos - 1: huruf for huruf, pos in batasan}
    
    huruf_bebas = [teks[i] for i in range(len(teks)) if i not in posisi_tetap]
    
    permutasi_unik = []
    for p in permutasi(huruf_bebas):
        if p not in permutasi_unik:
            permutasi_unik.append(p)
    
    jumlah = 0
    for perm in permutasi_unik:
        temp_teks = list(teks)
        indeks_perm = 0
        
        for i in range(len(teks)):
            if i not in posisi_tetap:
                temp_teks[i] = perm[indeks_perm]
                indeks_perm += 1
        
        if all(temp_teks[pos] == huruf for pos, huruf in posisi_tetap.items()):
            jumlah += 1
    
    return jumlah

teks = input().strip()
m = int(input().strip())
batasan = [tuple(input().split()) for _ in range(m)]
batasan = [(huruf, int(pos)) for huruf, pos in batasan]

print(PenyusunanKata(teks, batasan))