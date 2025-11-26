def count_islands(grid, m, n):
    # Inisialisasi array untuk melacak sel yang sudah dikunjungi
    visited = [[False for _ in range(n)] for _ in range(m)]
    
    # Arah pergerakan: atas, kanan, bawah, kiri (tidak diagonal)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Fungsi DFS untuk menjelajahi pulau
    def dfs(row, col):
        # Jika di luar grid atau bukan daratan atau sudah dikunjungi, berhenti
        if (row < 0 or row >= m or col < 0 or col >= n or 
            grid[row][col] == 0 or visited[row][col]):
            return
        
        # Tandai sel ini sudah dikunjungi
        visited[row][col] = True
        
        # Jelajahi semua sel tetangga (atas, kanan, bawah, kiri)
        for dr, dc in directions:
            dfs(row + dr, col + dc)
    
    # Hitung jumlah pulau
    island_count = 0
    
    # Periksa setiap sel dalam grid
    for i in range(m):
        for j in range(n):
            # Jika sel adalah daratan dan belum dikunjungi
            if grid[i][j] == 1 and not visited[i][j]:
                # Mulai DFS dari sel ini
                dfs(i, j)
                # Setelah menjelajahi semua sel yang terhubung, tambahkan jumlah pulau
                island_count += 1
    
    return island_count

# Membaca input
m, n = map(int, input().split())
grid = []

for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# Hitung dan tampilkan jumlah pulau
result = count_islands(grid, m, n)
print(result)