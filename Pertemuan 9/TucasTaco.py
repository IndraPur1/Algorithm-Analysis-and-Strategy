def generate_combinations(open_count, close_count, current, result):
    # Basis: jika sudah mencapai N pasang topping
    if open_count == N and close_count == N:
        result.append(current)
        return
    
    # Tambahkan topping buka "(" jika masih ada yang tersisa
    if open_count < N:
        generate_combinations(open_count + 1, close_count, current + "(", result)
    
    # Tambahkan topping tutup ")" jika valid (jumlah tutup < jumlah buka)
    if close_count < open_count:
        generate_combinations(open_count, close_count + 1, current + ")", result)

def count_taco_combinations():
    global all_combinations
    
    # Mulai pembangkitan kombinasi dengan backtracking
    generate_combinations(0, 0, "", all_combinations)
    
    # Kembalikan jumlah kombinasi yang mungkin
    return len(all_combinations)

# Input
N = int(input())

# Inisialisasi list untuk menyimpan semua kombinasi valid
all_combinations = []

# Hitung kombinasi taco dan simpan jumlahnya
total_combinations = count_taco_combinations()

# Output hasil
print(total_combinations)