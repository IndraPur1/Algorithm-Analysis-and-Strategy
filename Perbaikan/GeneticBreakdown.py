def cek_infeksi(dna_manusia, dna_virus):
    # Buat string untuk complementary strand dari DNA virus
    comp = ''
    for c in dna_virus:
        if c == 'A':
            comp += 'T'  # A pasangannya T
        elif c == 'T':
            comp += 'A'  # T pasangannya A
        elif c == 'C':
            comp += 'G'  # C pasangannya G
        elif c == 'G':
            comp += 'C'  # G pasangannya C

    max_match = 0  # Menyimpan jumlah kecocokan maksimum yang ditemukan
    panjang = len(dna_virus)  # Panjang DNA virus (juga panjang substring yang akan dibandingkan)

    # Sliding window: geser sepanjang DNA manusia dengan panjang DNA virus
    for i in range(len(dna_manusia) - panjang + 1):
        sub = dna_manusia[i:i+panjang]  # Ambil substring DNA manusia sepanjang DNA virus
        count = 0  # Hitung jumlah huruf yang cocok pada posisi yang sama
        for j in range(panjang):
            if sub[j] == comp[j]:  # Jika karakter sama dengan pasangan komplementer
                count += 1
        if count > max_match:  # Perbarui kecocokan maksimum jika ditemukan yang lebih besar
            max_match = count

    # Evaluasi apakah DNA manusia terinfeksi atau tidak
    # Jika jumlah kecocokan minimal 50% dari panjang DNA virus → terinfeksi
    if max_match * 2 >= panjang:
        print("Terinfeksi")
    else:
        print("Tidak Terinfeksi")

    # Cetak jumlah kecocokan maksimum
    print(max_match)


# Input DNA manusia dan DNA virus dari pengguna
dna_manusia = input()
dna_virus = input()

# Panggil fungsi untuk mengecek infeksi
cek_infeksi(dna_manusia, dna_virus)
