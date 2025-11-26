from collections import deque

def min_operations_to_zero(N):
    # Gunakan BFS untuk menemukan jumlah minimal operasi
    visited = set()  # Set untuk melacak angka yang sudah dikunjungi
    queue = deque([(N, 0)])  # (nilai saat ini, jumlah operasi)
    visited.add(N)
    
    while queue:
        current, operations = queue.popleft()
        
        # Cek apakah sudah mencapai 0
        if current == 0:
            return operations
        
        # Operasi 1: Tambah atau kurang 1
        if current - 1 >= 0 and current - 1 not in visited:
            queue.append((current - 1, operations + 1))
            visited.add(current - 1)
            
        if current + 1 not in visited:
            queue.append((current + 1, operations + 1))
            visited.add(current + 1)
        
        # Operasi 2: Kali 2
        if current * 2 not in visited:
            queue.append((current * 2, operations + 1))
            visited.add(current * 2)
        
        # Operasi 3: Bagi dengan 3^n (n>=0)
        divisor = 1  # 3^0 = 1
        while divisor <= current:
            if current % divisor == 0:
                result = current // divisor
                if result not in visited:
                    queue.append((result, operations + 1))
                    visited.add(result)
            divisor *= 3
    
    return -1  # Jika tidak bisa mencapai 0 (seharusnya tidak terjadi dalam kasus ini)

# Membaca input
N = int(input())

# Menghitung jumlah minimum operasi
result = min_operations_to_zero(N)
print(result)