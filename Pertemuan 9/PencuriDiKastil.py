import sys
from queue import PriorityQueue

# Define infinity value
INF = sys.maxsize

# Node class untuk menyimpan status pencarian
class Node:
    def __init__(self, level, profit, weight, items_included):
        self.level = level  # Level di pohon pencarian (item ke berapa)
        self.profit = profit  # Total profit/nilai yang sudah diambil
        self.weight = weight  # Total berat yang sudah diambil
        self.items_included = items_included.copy()  # Items yang diambil
        self.bound = 0  # Upper bound untuk cabang ini
    
    def __lt__(self, other):
        # Prioritaskan node dengan bound lebih tinggi (negatif untuk min-heap)
        return -self.bound < -other.bound

# Fungsi untuk menghitung upper bound dengan pendekatan fractional knapsack
def calculate_bound(node, weights, values, capacity, n):
    # Jika berat melebihi kapasitas, bound = 0
    if node.weight > capacity:
        return 0
    
    # Inisialisasi bound dengan profit saat ini
    profit_bound = node.profit
    
    # Inisialisasi berat saat ini
    weight = node.weight
    
    # Mulai dari item berikutnya
    j = node.level + 1
    
    # Tambahkan item selanjutnya selama masih ada kapasitas
    while j < n and weight + weights[j] <= capacity:
        weight += weights[j]
        profit_bound += values[j]
        j += 1
    
    # Jika masih ada item dan kapasitas, tambahkan sebagian dari item berikutnya
    if j < n:
        profit_bound += (capacity - weight) * (values[j] / weights[j])
    
    return profit_bound

# Fungsi utama Branch and Bound untuk masalah Knapsack
def knapsack_branch_and_bound(weights, values, capacity, n):
    # Buat list items dengan (nilai, berat, indeks asli)
    items = [(values[i], weights[i], i) for i in range(n)]
    
    # Urutkan items berdasarkan rasio nilai/berat (menurun)
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    # Ekstrak nilai dan berat yang sudah diurutkan
    sorted_values = [item[0] for item in items]
    sorted_weights = [item[1] for item in items]
    
    # Inisialisasi PriorityQueue
    pq = PriorityQueue()
    
    # Buat node root
    u = Node(-1, 0, 0, [])
    u.bound = calculate_bound(u, sorted_weights, sorted_values, capacity, n)
    
    # Masukkan node root ke queue
    pq.put(u)
    
    # Inisialisasi hasil terbaik
    best_profit = 0
    
    # Lakukan eksplorasi selama queue tidak kosong
    while not pq.empty():
        # Ambil node dengan bound tertinggi
        u = pq.get()
        
        # Jika bound lebih kecil dari profit terbaik, pangkas cabang
        if u.bound < best_profit:
            continue
        
        # Jika ini adalah node root, lanjutkan ke item pertama
        if u.level == -1:
            v_level = 0
        else:
            v_level = u.level + 1
        
        # Jika sudah mencapai akhir items
        if v_level == n:
            continue
        
        # Pilihan 1: Ambil item berikutnya jika muat
        if u.weight + sorted_weights[v_level] <= capacity:
            # Buat node baru
            v = Node(v_level, u.profit + sorted_values[v_level], u.weight + sorted_weights[v_level], u.items_included)
            v.items_included.append(v_level)
            
            # Update hasil terbaik jika node ini lebih baik
            if v.profit > best_profit:
                best_profit = v.profit
            
            # Hitung bound untuk node baru
            v.bound = calculate_bound(v, sorted_weights, sorted_values, capacity, n)
            
            # Jika bound menjanjikan, tambahkan ke queue
            if v.bound > best_profit:
                pq.put(v)
        
        # Pilihan 2: Tidak ambil item berikutnya
        v = Node(v_level, u.profit, u.weight, u.items_included)
        
        # Hitung bound untuk node baru
        v.bound = calculate_bound(v, sorted_weights, sorted_values, capacity, n)
        
        # Jika bound menjanjikan, tambahkan ke queue
        if v.bound > best_profit:
            pq.put(v)
    
    # Kembalikan hasil terbaik
    return best_profit

# Input
n, W = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

# Solve the problem
best_profit = knapsack_branch_and_bound(weights, values, W, n)

# Output
print(best_profit)