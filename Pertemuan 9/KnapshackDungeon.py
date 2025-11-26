import sys
from queue import PriorityQueue

# Define infinity value
INF = sys.maxsize

# Node class untuk menyimpan status pencarian
class Node:
    def __init__(self, level, profit, weight, items_included):
        self.level = level  # Level di pohon pencarian (item ke berapa)
        self.profit = profit  # Total profit/harga yang sudah diambil
        self.weight = weight  # Total berat yang sudah diambil
        self.items_included = items_included.copy()  # Items yang diambil
        self.bound = 0  # Upper bound untuk cabang ini
    
    def __lt__(self, other):
        # Prioritaskan node dengan bound lebih tinggi (negatif untuk min-heap)
        return -self.bound < -other.bound

# Fungsi untuk menghitung upper bound dengan pendekatan fractional knapsack
def calculate_bound(node, items, capacity, n):
    # Jika berat melebihi kapasitas, bound = 0
    if node.weight > capacity:
        return 0
    
    # Inisialisasi bound dengan profit saat ini
    profit_bound = node.profit
    
    # Inisialisasi berat saat ini
    weight = node.weight
    
    # Mulai dari item berikutnya
    j = node.level
    
    # Tambahkan item selanjutnya selama masih ada kapasitas
    while j < n and weight + items[j][1] <= capacity:
        weight += items[j][1]
        profit_bound += items[j][0]
        j += 1
    
    # Jika masih ada item dan kapasitas, tambahkan sebagian dari item berikutnya
    if j < n:
        profit_bound += (capacity - weight) * (items[j][0] / items[j][1])
    
    return profit_bound

# Fungsi utama Branch and Bound untuk masalah Knapsack
def knapsack_branch_and_bound(items, capacity, n):
    # Urutkan items berdasarkan rasio profit/weight (menurun)
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    # Inisialisasi PriorityQueue
    pq = PriorityQueue()
    
    # Buat node root
    u = Node(-1, 0, 0, [])
    u.bound = calculate_bound(u, items, capacity, n)
    
    # Masukkan node root ke queue
    pq.put(u)
    
    # Inisialisasi hasil terbaik
    best_profit = 0
    best_weight = 0
    best_items = []
    
    # Lakukan eksplorasi selama queue tidak kosong
    while not pq.empty():
        # Ambil node dengan bound tertinggi
        u = pq.get()
        
        # Jika bound lebih kecil dari profit terbaik, pangkas cabang
        if u.bound < best_profit:
            continue
        
        # Jika ini adalah node root, lanjutkan
        if u.level == -1:
            v_level = 0
        else:
            v_level = u.level + 1
        
        # Jika sudah mencapai akhir items
        if v_level == n:
            continue
        
        # Pilihan 1: Ambil item berikutnya
        if u.weight + items[v_level][1] <= capacity:
            # Buat node baru
            v = Node(v_level, u.profit + items[v_level][0], u.weight + items[v_level][1], u.items_included)
            v.items_included.append(v_level)
            
            # Update hasil terbaik jika node ini lebih baik
            if v.profit > best_profit and v.weight <= capacity:
                best_profit = v.profit
                best_weight = v.weight
                best_items = v.items_included.copy()
            
            # Hitung bound untuk node baru
            v.bound = calculate_bound(v, items, capacity, n)
            
            # Jika bound menjanjikan, tambahkan ke queue
            if v.bound > best_profit:
                pq.put(v)
        
        # Pilihan 2: Tidak ambil item berikutnya
        v = Node(v_level, u.profit, u.weight, u.items_included)
        
        # Hitung bound untuk node baru
        v.bound = calculate_bound(v, items, capacity, n)
        
        # Jika bound menjanjikan, tambahkan ke queue
        if v.bound > best_profit:
            pq.put(v)
    
    # Kembalikan hasil terbaik
    return best_profit, best_weight

# Input
N = int(input())
X = int(input())
items = []

for _ in range(N):
    price, weight = map(int, input().split())
    items.append((price, weight))

# Solve the problem
best_profit, best_weight = knapsack_branch_and_bound(items, X, N)

# Output
print(best_profit, best_weight)