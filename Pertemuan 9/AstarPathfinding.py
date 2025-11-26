import heapq

def manhattan_distance(x1, y1, x2, y2):
    # Fungsi heuristik Manhattan Distance
    return abs(x1 - x2) + abs(y1 - y2)

def astar_grid(grid, start, goal):
    global min_path_length
    rows, cols = len(grid), len(grid[0])
    sx, sy = start
    gx, gy = goal
    
    # Jika start dan goal sama
    if sx == gx and sy == gy:
        min_path_length = 0
        return
    
    # Arah yang bisa dilalui: atas, kanan, bawah, kiri
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Open set dengan format (f_score, g_score, (x, y))
    open_set = [(manhattan_distance(sx, sy, gx, gy), 0, (sx, sy))]
    
    # Simpan g_score untuk setiap sel
    g_score = {(sx, sy): 0}
    
    # Kumpulan node yang sudah dikunjungi
    visited = set()
    
    while open_set:
        # Ambil node dengan f_score terkecil
        f, g, (x, y) = heapq.heappop(open_set)
        
        # Jika node ini sudah pernah dikunjungi, lewati
        if (x, y) in visited:
            continue
        
        # Tandai sebagai sudah dikunjungi
        visited.add((x, y))
        
        # Jika sudah mencapai tujuan
        if x == gx and y == gy:
            min_path_length = g
            return
        
        # Eksplor semua arah
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Cek validitas sel berikutnya
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                new_g = g + 1
                
                # Update g_score jika lebih baik
                if (nx, ny) not in g_score or new_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = new_g
                    f_score = new_g + manhattan_distance(nx, ny, gx, gy)
                    heapq.heappush(open_set, (f_score, new_g, (nx, ny)))
    
    # Jika tidak ada jalur ditemukan
    min_path_length = -1
    return

# Input
N, M = map(int, input().split())
sx, sy, gx, gy = map(int, input().split())
grid = []

for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# Inisialisasi variabel hasil
min_path_length = float('inf')

# Mulai pencarian
astar_grid(grid, (sx, sy), (gx, gy))

# Output hasil
print(min_path_length)