from collections import deque

def bfs_levels(n, edges, start):
    # Buat representasi graf dalam bentuk adjacency list
    graph = [[] for _ in range(n + 1)]
    
    # Isi adjacency list berdasarkan edges yang diberikan
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Graf tak berarah
    
    # Inisialisasi array untuk melacak simpul yang sudah dikunjungi
    visited = [False] * (n + 1)
    
    # Inisialisasi array untuk menyimpan level setiap simpul
    levels = [-1] * (n + 1)
    
    # Inisialisasi queue untuk BFS
    queue = deque([start])
    visited[start] = True
    levels[start] = 0
    
    # Inisialisasi list untuk menyimpan urutan kunjungan BFS
    bfs_order = []
    
    # Lakukan BFS
    while queue:
        vertex = queue.popleft()
        bfs_order.append(vertex)
        
        # Kunjungi semua tetangga yang belum dikunjungi
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                levels[neighbor] = levels[vertex] + 1
                queue.append(neighbor)
    
    return bfs_order, levels

# Function untuk parsing input edges
def parse_edges(edges_str):
    # Hapus semua spasi
    edges_str = edges_str.replace(" ", "")
    # Hapus bracket terluar
    edges_str = edges_str[2:-2]
    # Split berdasarkan "], ["
    pairs = edges_str.split("],[")
    
    edges = []
    for pair in pairs:
        u, v = map(int, pair.split(","))
        edges.append((u, v))
    
    return edges

# Membaca input
n = int(input())
edges_str = input().strip()
start = int(input())

# Parse edges
edges = parse_edges(edges_str)

# Lakukan BFS
bfs_order, levels = bfs_levels(n, edges, start)

# Format output
print(f"Urutan BFS: {', '.join(map(str, bfs_order))}")
print("Level:")

# Membuat dictionary untuk melacak vertex mana yang ada dalam output BFS
vertices_in_bfs = set(bfs_order)

# Tampilkan level dalam urutan yang sesuai dengan output yang diharapkan
# Dimulai dengan start vertex
print(f"simpul {start}: {levels[start]}")

# Kemudian tampilkan vertex lain dalam urutan BFS (kecuali start vertex)
for vertex in bfs_order:
    if vertex != start:
        print(f"simpul {vertex}: {levels[vertex]}")