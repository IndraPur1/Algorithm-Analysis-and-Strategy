def gold_mining_greedy():
    # Buat list mines seperti activities dalam contoh
    mines = []
    for i in range(n):
        efficiency = gold[i] / time[i]  # Rasio emas per waktu
        mines.append((gold[i], time[i], efficiency))
    
    # Sort berdasarkan efisiensi seperti activities.sort(key=lambda x: x[1])
    # Dalam hal ini sort berdasarkan efficiency descending (yang terbaik dulu)
    # Jika efisiensi sama, prioritaskan gold lebih banyak
    mines.sort(key=lambda x: (x[2], x[0]), reverse=True)
    
    # Inisialisasi seperti dalam activity selection
    total_gold = 0
    remaining_time = T
    
    # Loop seperti dalam activity selection dengan constraint checking
    for i in range(len(mines)):
        gold_amount, time_needed, efficiency = mines[i]
        # Constraint check seperti start >= last_end_time dalam activity selection
        if time_needed <= remaining_time:
            # Select seperti selected.append() dalam activity selection
            total_gold += gold_amount
            # Update seperti last_end_time = end dalam activity selection
            remaining_time -= time_needed
    
    return total_gold

# Input
n, T = map(int, input().split())
gold = list(map(int, input().split()))
time = list(map(int, input().split()))

# Jalankan program
result = gold_mining_greedy()
print(result)