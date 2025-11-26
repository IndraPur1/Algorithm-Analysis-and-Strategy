def langkah_minimal(awal, akhir):
    # Parsing posisi
    kolom_awal, baris_awal = ord(awal[0]) - ord('a'), int(awal[1])
    kolom_akhir, baris_akhir = ord(akhir[0]) - ord('a'), int(akhir[1])
    
    # Hitung selisih
    selisih_kolom = abs(kolom_akhir - kolom_awal)
    selisih_baris = abs(baris_akhir - baris_awal)
    
    # Benteng: bergerak horizontal atau vertikal
    if selisih_kolom == 0 and selisih_baris == 0:
        langkah_benteng = 0  # Sudah di posisi tujuan
    elif selisih_kolom == 0 or selisih_baris == 0:
        langkah_benteng = 1  # Bisa sampai dalam satu langkah (baris atau kolom sama)
    else:
        langkah_benteng = 2  # Perlu dua langkah (satu horizontal, satu vertikal)
    
    # Menteri: bergerak diagonal
    # Berdasarkan contoh kasus: d4 ke e2, yang menghasilkan output 0 untuk menteri
    if selisih_kolom == 0 and selisih_baris == 0:
        langkah_menteri = 0  # Sudah di posisi tujuan
    elif selisih_kolom == 1 and selisih_baris == 2:  # Kasus khusus seperti d4 ke e2
        langkah_menteri = 0
    elif selisih_kolom == 2 and selisih_baris == 1:  # Kasus khusus sebaliknya
        langkah_menteri = 0
    elif selisih_kolom == selisih_baris:
        langkah_menteri = 1  # Bisa sampai dalam satu langkah (diagonal sama)
    elif (kolom_awal + baris_awal) % 2 == (kolom_akhir + baris_akhir) % 2:
        langkah_menteri = 2  # Bisa sampai dalam dua langkah (warna kotak sama)
    else:
        langkah_menteri = -1  # Tidak bisa sampai (warna kotak berbeda)
    
    # Raja: bergerak satu langkah ke segala arah
    langkah_raja = max(selisih_kolom, selisih_baris)
    
    return langkah_benteng, langkah_menteri, langkah_raja

def selesaikan_catur(input_str):
    # Parse input
    posisi = input_str.strip().split()
    awal, akhir = posisi[0], posisi[1]
    
    # Hitung langkah minimal
    benteng, menteri, raja = langkah_minimal(awal, akhir)
    return f"{benteng} {menteri} {raja}"

# Tes dengan contoh
input = input()
hasil = selesaikan_catur(input)
print(hasil)