from collections import deque

def is_path_exists(n, edges, start, target):
    # Buat representasi graf dalam bentuk adjacency list
    graph = [[] for _ in range(n)]
    
    # Isi adjacency list berdasarkan edges yang diberikan
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Graf tak berarah
    
    # Inisialisasi array untuk melacak simpul yang sudah dikunjungi
    visited = [False] * n
    
    # Inisialisasi queue untuk BFS
    queue = deque([start])
    visited[start] = True
    
    # Lakukan BFS
    while queue:
        vertex = queue.popleft()
        
        # Jika kita mencapai target, return True
        if vertex == target:
            return True
        
        # Kunjungi semua tetangga yang belum dikunjungi
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # Jika tidak ada path dari start ke target
    return False

# Membaca input
n = int(input())  # Jumlah node
e = int(input())  # Jumlah edge

edges = []
for _ in range(e):
    line = input().split()
    u, v = int(line[0]), int(line[1])
    edges.append((u, v))

line = input().split()
start, target = int(line[0]), int(line[1])

# Cek apakah terdapat path dari start ke target
result = is_path_exists(n, edges, start, target)
print(result)