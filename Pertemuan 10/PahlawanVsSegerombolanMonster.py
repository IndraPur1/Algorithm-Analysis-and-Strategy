def solve_hero_monsters():
    """
    Algoritma Greedy Optimized untuk Hero vs Monsters
    
    Strategi Greedy Baru:
    1. Pisahkan monster menjadi 2 kategori berdasarkan bonus
    2. Untuk monster dengan bonus positif: urutkan berdasarkan kekuatan (ascending)
    3. Untuk monster dengan bonus negatif/nol: urutkan berdasarkan bonus (descending)
    4. Proses secara berurutan dengan strategi yang berbeda
    """
    
    P, N = map(int, input().split())
    monsters = []
    
    for i in range(N):
        K, B = map(int, input().split())
        monsters.append((K, B, i))  # (power, bonus, original_index)
    
    # Pisahkan monster berdasarkan bonus
    positive_bonus = []
    non_positive_bonus = []
    
    for monster in monsters:
        power, bonus, idx = monster
        if bonus > 0:
            positive_bonus.append(monster)
        else:
            non_positive_bonus.append(monster)
    
    # Strategi Greedy:
    # 1. Monster dengan bonus positif: urutkan berdasarkan kekuatan (mudah ke sulit)
    #    Ini memastikan kita mengumpulkan kekuatan sebanyak mungkin terlebih dahulu
    positive_bonus.sort(key=lambda x: x[0])  # sort by power
    
    # 2. Monster dengan bonus non-positif: urutkan berdasarkan bonus (terbesar ke terkecil)
    #    Ini meminimalkan kerugian
    non_positive_bonus.sort(key=lambda x: x[1], reverse=True)  # sort by bonus descending
    
    current_power = P
    
    # Fase 1: Kalahkan semua monster dengan bonus positif
    for power, bonus, idx in positive_bonus:
        if current_power >= power:
            current_power += bonus
        else:
            print("NO")
            return
    
    # Fase 2: Kalahkan monster dengan bonus non-positif
    for power, bonus, idx in non_positive_bonus:
        if current_power >= power:
            current_power += bonus
            # Jika kekuatan menjadi negatif, tidak mungkin melanjutkan
            if current_power < 0:
                print("NO")
                return
        else:
            print("NO")
            return
    
    print("YES")

# Versi alternatif dengan pendekatan yang lebih sederhana
def solve_hero_monsters_v2():
    """
    Pendekatan Greedy Alternatif:
    Urutkan monster berdasarkan rasio bonus/power untuk optimasi
    """
    P, N = map(int, input().split())
    monsters = []
    
    for i in range(N):
        K, B = map(int, input().split())
        monsters.append((K, B))
    
    current_power = P
    
    # Pisahkan monster berdasarkan apakah mereka memberikan bonus positif
    good_monsters = [(k, b) for k, b in monsters if b > 0]
    bad_monsters = [(k, b) for k, b in monsters if b <= 0]
    
    # Untuk monster yang memberikan bonus: urutkan berdasarkan kekuatan (mudah dulu)
    good_monsters.sort()
    
    # Untuk monster yang tidak memberikan bonus: urutkan berdasarkan bonus (terbaik dulu)
    bad_monsters.sort(key=lambda x: -x[1])
    
    # Kalahkan monster yang memberikan bonus terlebih dahulu
    for power, bonus in good_monsters:
        if current_power >= power:
            current_power += bonus
        else:
            print("NO")
            return
    
    # Kemudian kalahkan monster yang tidak memberikan bonus
    for power, bonus in bad_monsters:
        if current_power >= power:
            current_power += bonus
        else:
            print("NO")
            return
    
    print("YES")

# Gunakan versi yang lebih sederhana
solve_hero_monsters_v2() 