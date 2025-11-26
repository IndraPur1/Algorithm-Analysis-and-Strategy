from collections import defaultdict

def main():
    # Membaca input
    N, M, Q = map(int, input().split())
    warp_costs = list(map(int, input().split()))
    
    # Membuat graph yang merepresentasikan relasi antar planet
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        # Konversi dari 1-indexed ke 0-indexed
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    # Membaca urutan planet yang ingin dikunjungi
    journey = list(map(int, input().split()))
    # Konversi dari 1-indexed ke 0-indexed
    journey = [planet - 1 for planet in journey]
    
    total_cost = 0
    
    # Melakukan perjalanan sesuai urutan
    for i in range(1, Q):
        current_planet = journey[i-1]
        next_planet = journey[i]
        
        # Jika planet sama, tidak perlu warp
        if current_planet == next_planet:
            continue
        
        # Cek apakah planet terhubung
        if is_connected(graph, current_planet, next_planet, N):
            # Jika terhubung, tidak perlu biaya
            continue
        else:
            # Jika tidak terhubung, cari planet terdekat untuk melakukan warp
            # dengan biaya paling kecil
            min_cost = float('inf')
            
            # Cari semua planet yang terhubung dengan planet saat ini
            connected_to_current = find_connected_planets(graph, current_planet, N)
            # Cari semua planet yang terhubung dengan planet tujuan
            connected_to_next = find_connected_planets(graph, next_planet, N)
            
            # Cari pasangan planet dengan biaya warp paling kecil
            for planet_a in connected_to_current:
                for planet_b in connected_to_next:
                    cost = warp_costs[planet_a] + warp_costs[planet_b]
                    min_cost = min(min_cost, cost)
            
            total_cost += min_cost
    
    print(total_cost)

def is_connected(graph, start, end, n):
    """
    Menggunakan DFS untuk memeriksa apakah dua planet terhubung
    """
    visited = [False] * n
    
    def dfs(node):
        if node == end:
            return True
        
        visited[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        
        return False
    
    return dfs(start)

def find_connected_planets(graph, start, n):
    """
    Mencari semua planet yang terhubung dengan planet start
    """
    visited = [False] * n
    connected = []
    
    def dfs(node):
        visited[node] = True
        connected.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(start)
    return connected

if __name__ == "__main__":
    main()