from collections import deque

def min_coins_to_reach_destination(n, m, lit_cells):
    # Konversi koordinat dari 1-indexed ke 0-indexed
    lit_cells = set((r-1, c-1) for r, c in lit_cells)
    
    # Queue untuk BFS - (baris, kolom, koin, status_baris, status_kolom)
    # status_baris/kolom: -1 jika tidak ada baris/kolom yang menyala, atau indeks baris/kolom yang menyala
    queue = deque([(0, 0, 0, -1, -1)])
    
    # Set untuk menyimpan status yang telah dikunjungi
    visited = set([(0, 0, -1, -1)])
    
    while queue:
        r, c, coins, lit_row, lit_col = queue.popleft()
        
        # Cek apakah sudah mencapai tujuan
        if r == n-1 and c == m-1:
            return coins
        
        # Arah pergerakan: atas, kanan, bawah, kiri
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            
            # Cek apakah sel tetangga valid
            if 0 <= new_r < n and 0 <= new_c < m:
                # Cek apakah sel tetangga menyala (awalnya atau karena baris/kolom yang menyala)
                new_cell_lit = (new_r, new_c) in lit_cells or new_r == lit_row or new_c == lit_col
                
                if new_cell_lit and (new_r, new_c, lit_row, lit_col) not in visited:
                    visited.add((new_r, new_c, lit_row, lit_col))
                    queue.append((new_r, new_c, coins, lit_row, lit_col))
        
        # Jika sel saat ini menyala, coba opsi menyalakan baris/kolom baru
        if (r, c) in lit_cells:
            # Coba menyalakan baris
            if lit_row != r:  # Jika baris ini belum menyala
                if (r, c, r, -1) not in visited:
                    visited.add((r, c, r, -1))
                    queue.append((r, c, coins + 1, r, -1))
            
            # Coba menyalakan kolom
            if lit_col != c:  # Jika kolom ini belum menyala
                if (r, c, -1, c) not in visited:
                    visited.add((r, c, -1, c))
                    queue.append((r, c, coins + 1, -1, c))
    
    # Jika tidak ada jalur yang ditemukan
    return -1

# Membaca input
n, m, k = map(int, input().split())
lit_cells = []

for _ in range(k):
    r, c = map(int, input().split())
    lit_cells.append((r, c))

# Hitung dan tampilkan jumlah minimum koin
result = min_coins_to_reach_destination(n, m, lit_cells)
print(result)