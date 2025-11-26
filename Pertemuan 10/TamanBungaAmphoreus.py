def flower_planting_greedy():
    # Input
    line = input().split()
    garden = [int(x) for x in line[:-1]]  # Array taman kecuali elemen terakhir
    n = int(line[-1])  # Jumlah bunga yang akan ditanam
    
    # Buat list posisi yang bisa ditanami seperti activities dalam contoh
    available_positions = []
    for i in range(len(garden)):
        if garden[i] == 0:  # Petak kosong
            # Cek apakah posisi ini aman (tidak bersebelahan dengan bunga)
            can_plant = True
            # Cek kiri
            if i > 0 and garden[i-1] == 1:
                can_plant = False
            # Cek kanan  
            if i < len(garden)-1 and garden[i+1] == 1:
                can_plant = False
            
            if can_plant:
                available_positions.append(i)
    
    # Sort berdasarkan posisi seperti activities.sort(key=lambda x: x[1])
    # Dalam hal ini sort berdasarkan index (dari kiri ke kanan)
    available_positions.sort()
    
    # Inisialisasi seperti dalam activity selection
    planted_count = 0
    garden_copy = garden[:]  # Copy untuk simulasi penanaman
    
    # Loop seperti dalam activity selection dengan constraint checking
    for i in range(len(available_positions)):
        pos = available_positions[i]
        
        # Constraint check seperti start >= last_end_time dalam activity selection
        # Cek apakah posisi masih aman untuk ditanami
        can_plant = True
        
        # Cek kiri
        if pos > 0 and garden_copy[pos-1] == 1:
            can_plant = False
        # Cek kanan
        if pos < len(garden_copy)-1 and garden_copy[pos+1] == 1:
            can_plant = False
        
        if can_plant:
            # Select seperti selected.append() dalam activity selection
            garden_copy[pos] = 1
            planted_count += 1
            
            # Jika sudah mencapai target, berhenti
            if planted_count == n:
                break
    
    # Return true jika berhasil menanam semua bunga
    return planted_count >= n

# Jalankan program
result = flower_planting_greedy()
print("true" if result else "false")