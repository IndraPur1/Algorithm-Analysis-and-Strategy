def space_mission():
    N, W = map(int, input().split())  # Membaca jumlah peralatan (N) dan kapasitas pesawat (W)
    items = [tuple(map(int, input().split())) for _ in range(N)]  # Membaca daftar peralatan sebagai (berat, nilai kepentingan)
    
    dp = [[0] * (W + 1) for _ in range(N + 1)]  # Membuat tabel DP berukuran (N+1) x (W+1), diisi dengan 0
    
    for i in range(1, N + 1):  # Iterasi setiap peralatan (1 sampai N)
        w, p = items[i - 1]  # Mendapatkan berat dan nilai kepentingan peralatan ke-i
        for j in range(W + 1):  # Iterasi kapasitas dari 0 sampai W
            if j >= w:  # Jika kapasitas saat ini cukup untuk menampung peralatan ini
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + p)  
                # Pilih maksimum antara: 
                # 1. Tidak membawa peralatan ini (dp[i-1][j])
                # 2. Membawa peralatan ini (dp[i-1][j-w] + p)
            else:
                dp[i][j] = dp[i - 1][j]  # Jika berat melebihi kapasitas, gunakan nilai sebelumnya (tidak ambil peralatan)

    print(dp[N][W])  # Cetak nilai kepentingan maksimum yang bisa didapatkan dalam batas kapasitas

space_mission()  # Memanggil fungsi utama
