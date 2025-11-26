import sys
from queue import PriorityQueue

# Define infinity value
INF = sys.maxsize

# Node class untuk menyimpan status pencarian
class Node:
    def __init__(self, current_city, path, total_time):
        self.current_city = current_city  # Kota saat ini
        self.path = path.copy()  # Jalur yang sudah dilalui
        self.total_time = total_time  # Total waktu tempuh
    
    def __lt__(self, other):
        return self.total_time < other.total_time

# Fungsi untuk menghitung batas bawah (lower bound)
def calculate_lower_bound(current_city, destination, graph, N, visited):
    # Untuk jalur dari current_city ke destination
    # Lower bound sederhana: total waktu tempuh sejauh ini
    # Kita bisa menambahkan heuristik di sini jika diperlukan, 
    # tapi untuk graf berarah dengan bobot, ini cukup sulit tanpa informasi tambahan
    return 0  # Kembalikan 0 sebagai tambahan, total sudah dihitung di node

# Fungsi utama Branch and Bound untuk masalah jalur terpendek
def find_shortest_path(graph, N):
    # Periksa apakah ada jalur keluar dari kota awal
    has_path_from_start = False
    for j in range(N):
        if graph[0][j] != -1:
            has_path_from_start = True
            break
    
    if not has_path_from_start:
        return -1  # Tidak ada jalur keluar dari kota awal
    
    # Buat priority queue untuk menyimpan node-node yang akan dieksplor
    pq = PriorityQueue()
    
    # Buat node awal (kota 0)
    start_node = Node(0, [0], 0)
    
    # Masukkan node awal ke priority queue
    pq.put((start_node.total_time, start_node))
    
    # Inisialisasi hasil terbaik
    best_time = INF
    
    # Lakukan eksplorasi selama queue tidak kosong
    while not pq.empty():
        # Ambil node dengan estimasi waktu terendah
        _, current_node = pq.get()
        
        # Jika node ini memiliki waktu lebih besar dari solusi terbaik yang sudah ditemukan, pangkas
        if current_node.total_time >= best_time:
            continue
        
        # Jika sudah mencapai kota tujuan (N-1), update hasil terbaik
        if current_node.current_city == N - 1:
            best_time = min(best_time, current_node.total_time)
            continue
        
        # Coba kunjungi semua kota tetangga yang belum dikunjungi
        for next_city in range(N):
            # Periksa apakah ada terowongan ke kota berikutnya
            if graph[current_node.current_city][next_city] == -1:
                continue
            
            # Periksa apakah kota berikutnya sudah pernah dikunjungi (menghindari siklus)
            if next_city in current_node.path:
                continue
            
            # Hitung waktu tempuh baru
            new_time = current_node.total_time + graph[current_node.current_city][next_city]
            
            # Jika waktu baru sudah melebihi solusi terbaik, pangkas
            if new_time >= best_time:
                continue
            
            # Buat node baru dengan kunjungan ke kota berikutnya
            new_path = current_node.path.copy()
            new_path.append(next_city)
            
            new_node = Node(next_city, new_path, new_time)
            
            # Hitung bound untuk node baru
            bound = new_time + calculate_lower_bound(next_city, N-1, graph, N, new_path)
            
            # Jika node ini masih memiliki potensi solusi yang lebih baik, tambahkan ke queue
            if bound < best_time:
                pq.put((bound, new_node))
    
    # Kembalikan hasil terbaik, atau -1 jika tidak ada jalur
    return best_time if best_time != INF else -1

# Input
N = int(input())
graph = []

for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

# Solve the problem
result = find_shortest_path(graph, N)

# Output
print(result)