def hitungZonaAman(grid, n, m):
    # Array untuk menyimpan sel yang sudah dikunjungi
    sudahDikunjungi = [[False] * m for _ in range(n)]
    
    # Arah pergerakan: atas, kanan, bawah, kiri (tidak diagonal)
    arah = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Fungsi DFS untuk menjelajahi zona aman
    def dfs(baris, kolom):
        # Jika di luar grid atau bukan zona aman atau sudah dikunjungi, berhenti
        if (baris < 0 or baris >= n or kolom < 0 or kolom >= m or 
            grid[baris][kolom] == 0 or sudahDikunjungi[baris][kolom]):
            return
        
        # Tandai sel ini sudah dikunjungi
        sudahDikunjungi[baris][kolom] = True
        
        # Jelajahi semua sel tetangga (atas, kanan, bawah, kiri)
        for db, dk in arah:
            dfs(baris + db, kolom + dk)
    
    # Hitung jumlah zona aman
    jumlahZonaAman = 0
    
    # Periksa setiap sel dalam grid
    for i in range(n):
        for j in range(m):
            # Jika sel adalah zona aman dan belum dikunjungi
            if grid[i][j] == 1 and not sudahDikunjungi[i][j]:
                # Mulai DFS dari sel ini
                dfs(i, j)
                # Setelah menjelajahi semua sel yang terhubung, tambahkan jumlah zona aman
                jumlahZonaAman += 1
    
    return jumlahZonaAman

# Membaca input
n, m = map(int, input().split())
grid = []

for _ in range(n):
    baris = list(map(int, input().split()))
    grid.append(baris)

# Hitung dan tampilkan jumlah zona aman
hasil = hitungZonaAman(grid, n, m)
print(hasil)