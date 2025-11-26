def generate_permutations(prefix, remaining, result):
    # Basis: jika string tersisa kosong, tambahkan permutasi yang sudah jadi
    if not remaining:
        result.add(prefix)
        return
    
    # Rekursi: coba setiap karakter yang tersisa
    for i in range(len(remaining)):
        # Lewati jika karakter ini sama dengan karakter sebelumnya (untuk menghindari duplikat)
        if i > 0 and remaining[i] == remaining[i-1]:
            continue
        
        # Ambil karakter di posisi i untuk ditambahkan ke prefix
        new_prefix = prefix + remaining[i]
        
        # Buat string baru tanpa karakter yang sudah diambil
        new_remaining = remaining[:i] + remaining[i+1:]
        
        # Lanjutkan rekursi
        generate_permutations(new_prefix, new_remaining, result)

def print_permutations(s):
    global all_permutations
    
    # Urutkan karakter input untuk memastikan permutasi dalam urutan leksikografis
    sorted_chars = ''.join(sorted(s))
    
    # Hasilkan semua permutasi
    generate_permutations("", sorted_chars, all_permutations)
    
    # Cetak permutasi secara berurutan
    for perm in sorted(all_permutations):
        print(perm)

# Input
S = input().strip()

# Inisialisasi set untuk menyimpan permutasi unik
all_permutations = set()

# Mulai proses permutasi
print_permutations(S)