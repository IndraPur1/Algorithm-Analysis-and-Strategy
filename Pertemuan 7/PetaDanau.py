def hitungDanau(peta, x, y):
    # Inisialisasi array untuk melacak sel yang sudah dikunjungi
    sudahTerkunjungi = [[False] * y for _ in range(x)]
    
    # Arah pergerakan: atas, kanan, bawah, kiri (horizontal dan vertikal saja)
    arah = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def dfs(i, j):
        tumpukan = [(i, j)]
        sudahTerkunjungi[i][j] = True
        menyentuhTepi = False
        
        while tumpukan:
            r, c = tumpukan.pop()
            
            # Cek apakah sel ini berada di tepi peta
            if r == 0 or r == x-1 or c == 0 or c == y-1:
                menyentuhTepi = True
            
            # Jelajahi semua arah yang mungkin
            for dr, dc in arah:
                nr, nc = r + dr, c + dc
                
                # Validasi posisi baru
                if 0 <= nr < x and 0 <= nc < y:
                    # Jika air dan belum dikunjungi
                    if peta[nr][nc] == 0 and not sudahTerkunjungi[nr][nc]:
                        sudahTerkunjungi[nr][nc] = True
                        tumpukan.append((nr, nc))
        
        # Kembalikan apakah air ini menyentuh tepi
        return menyentuhTepi
    
    # Hitung jumlah danau
    jumlahDanau = 0
    
    # Periksa setiap sel dalam peta
    for i in range(x):
        for j in range(y):
            # Jika sel adalah air dan belum dikunjungi
            if peta[i][j] == 0 and not sudahTerkunjungi[i][j]:
                # Jika komponen air ini tidak menyentuh tepi, ini adalah danau
                if not dfs(i, j):
                    jumlahDanau += 1
    
    return jumlahDanau

# Membaca input
x, y = map(int, input().split())
peta = []

for _ in range(x):
    baris = list(map(int, input().split()))
    peta.append(baris)

# Hitung dan tampilkan jumlah danau
hasil = hitungDanau(peta, x, y)
print(hasil)