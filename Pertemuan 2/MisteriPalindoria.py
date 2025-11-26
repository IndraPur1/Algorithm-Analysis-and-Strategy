def hitung_frekuensi(teks):
    frekuensi = {}
    
    for huruf in teks:
        if huruf in frekuensi:
            frekuensi[huruf] += 1
        else:
            frekuensi[huruf] = 1
    return frekuensi

def bisa_jadi_palindrom(teks):
    frekuensi = hitung_frekuensi(teks)
    jumlah_ganjil = 0
    
    for nilai in frekuensi.values():
        if nilai % 2 != 0:
            jumlah_ganjil += 1
    return jumlah_ganjil <= 1

def permutasi_unik(sisa, hasil, daftar_hasil, dipake):
    if len(sisa) == 0:
        daftar_hasil.append(hasil)
        return
    
    i = 0
    while i < len(sisa):
        if i == 0 or sisa[i] != sisa[i - 1] or dipake[i - 1]:  
            dipake[i] = True
            permutasi_unik(sisa[:i] + sisa[i + 1:], hasil + sisa[i], daftar_hasil, dipake)
            dipake[i] = False  
        
        i += 1

def generate_palindrom(teks):
    if bisa_jadi_palindrom(teks) == False:
        return "Kabur!"

    frekuensi = hitung_frekuensi(teks)
    tengah = ""
    bagian_kiri = []

    for huruf in sorted(frekuensi.keys()):  
        jumlah = frekuensi[huruf]
        
        if jumlah % 2 != 0:
            tengah = huruf
        bagian_kiri.extend(huruf * (jumlah // 2))

    daftar_hasil = []
    dipake = [False] * len(bagian_kiri)
    permutasi_unik(bagian_kiri, "", daftar_hasil, dipake)

    hasil_akhir = []
    for kiri in daftar_hasil:
        hasil_akhir.append(kiri + tengah + kiri[::-1])

    return " ".join(sorted(hasil_akhir))

teks = input().strip()
print(generate_palindrom(teks))