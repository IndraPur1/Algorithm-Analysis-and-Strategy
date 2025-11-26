import heapq
import time
from collections import defaultdict

# Fungsi untuk menampilkan pohon pencarian
def tampilkan_pohon_pencarian(pohon, simpul_awal, simpul_tujuan, nama_algo, nama_kasus):
    print(f"\nPohon Pencarian untuk {nama_algo} pada {nama_kasus}:")
    def cetak_pohon(simpul, awalan="", kedalaman=0):
        if simpul not in pohon:
            return
        skor, induk = pohon[simpul]
        if nama_algo == "Dijkstra":
            teks_skor = f"biaya={skor:.3f}%"
        elif nama_algo == "A*":
            teks_skor = f"f={skor:.3f}%"
        else:  # Greedy
            teks_skor = f"heuristik={skor:.3f}%"
        tanda = " (Tujuan)" if simpul == simpul_tujuan else ""
        teks_induk = f"dari {induk}" if induk else "Akar"
        print(f"{awalan}{'  ' * kedalaman}{simpul} ({teks_skor}, {teks_induk}){tanda}")
        for anak in sorted([n for n, (s, p) in pohon.items() if p == simpul]):
            cetak_pohon(anak, awalan, kedalaman + 1)
    cetak_pohon(simpul_awal)

# Algoritma Dijkstra
def cari_jalur_dijkstra(graf, awal, tujuan):
    jarak = {simpul: float('inf') for simpul in graf}  # Jarak awal ke semua simpul
    jarak[awal] = 0
    antrian = [(0, awal, [awal])]  # (biaya, simpul, jalur)
    pohon = {awal: (0, None)}  # Simpul: (biaya, induk)
    sudah_dikunjungi = set()
    
    while antrian:
        biaya_sekarang, simpul_sekarang, jalur = heapq.heappop(antrian)
        if simpul_sekarang in sudah_dikunjungi:
            continue
        sudah_dikunjungi.add(simpul_sekarang)
        if simpul_sekarang == tujuan:
            return biaya_sekarang, jalur, pohon
        for tetangga, bobot in graf[simpul_sekarang].items():
            if tetangga not in sudah_dikunjungi:
                jarak_baru = biaya_sekarang + bobot
                if jarak_baru < jarak[tetangga]:
                    jarak[tetangga] = jarak_baru
                    pohon[tetangga] = (jarak_baru, simpul_sekarang)
                    heapq.heappush(antrian, (jarak_baru, tetangga, jalur + [tetangga]))
    return float('inf'), [], pohon

# Algoritma A*
def cari_jalur_a_bintang(graf, awal, tujuan, heuristik):
    biaya_g = {simpul: float('inf') for simpul in graf}  # Biaya aktual dari awal
    biaya_g[awal] = 0
    antrian = [(heuristik[awal], 0, awal, [awal])]  # (f_skor, g_skor, simpul, jalur)
    pohon = {awal: (heuristik[awal], None)}  # Simpul: (f_skor, induk)
    sudah_dikunjungi = set()
    
    while antrian:
        f_skor, biaya_g_sekarang, simpul_sekarang, jalur = heapq.heappop(antrian)
        if simpul_sekarang in sudah_dikunjungi:
            continue
        sudah_dikunjungi.add(simpul_sekarang)
        if simpul_sekarang == tujuan:
            return biaya_g_sekarang, jalur, pohon
        for tetangga, bobot in graf[simpul_sekarang].items():
            if tetangga not in sudah_dikunjungi:
                biaya_g_baru = biaya_g_sekarang + bobot
                if biaya_g_baru < biaya_g[tetangga]:
                    biaya_g[tetangga] = biaya_g_baru
                    f_skor_baru = biaya_g_baru + heuristik[tetangga]
                    pohon[tetangga] = (f_skor_baru, simpul_sekarang)
                    heapq.heappush(antrian, (f_skor_baru, biaya_g_baru, tetangga, jalur + [tetangga]))
    return float('inf'), [], pohon

# Algoritma Greedy Best-First Search
def cari_jalur_greedy(graf, awal, tujuan, heuristik):
    antrian = [(heuristik[awal], 0, awal, [awal])]  # (heuristik, biaya, simpul, jalur)
    pohon = {awal: (heuristik[awal], None)}  # Simpul: (h_skor, induk)
    sudah_dikunjungi = set()
    
    while antrian:
        h_skor, biaya, simpul_sekarang, jalur = heapq.heappop(antrian)
        if simpul_sekarang in sudah_dikunjungi:
            continue
        sudah_dikunjungi.add(simpul_sekarang)
        if simpul_sekarang == tujuan:
            return biaya, jalur, pohon
        for tetangga, bobot in graf[simpul_sekarang].items():
            if tetangga not in sudah_dikunjungi:
                pohon[tetangga] = (heuristik[tetangga], simpul_sekarang)
                heapq.heappush(antrian, (heuristik[tetangga], biaya + bobot, tetangga, jalur + [tetangga]))
    return float('inf'), [], pohon

# Fungsi untuk menjalankan eksperimen
def jalankan_eksperimen(graf, awal, tujuan, heuristik, nama_algo, nama_kasus):
    waktu_mulai = time.time()
    if nama_algo == "Dijkstra":
        biaya, jalur, pohon = cari_jalur_dijkstra(graf, awal, tujuan)
    elif nama_algo == "A*":
        biaya, jalur, pohon = cari_jalur_a_bintang(graf, awal, tujuan, heuristik)
    else:  # Greedy
        biaya, jalur, pohon = cari_jalur_greedy(graf, awal, tujuan, heuristik)
    waktu_eksekusi = time.time() - waktu_mulai
    tampilkan_pohon_pencarian(pohon, awal, tujuan, nama_algo, nama_kasus)
    return {
        'biaya': biaya,
        'jalur': jalur,
        'waktu': waktu_eksekusi,
        'iterasi': len(jalur) if jalur else 0
    }

# Kasus Uji 1: 4 Simpul
graf_kasus1 = {
    'ETH/USDT': {'USDT/DAI': 0.3, 'DAI/USDC': 0.4},
    'USDT/DAI': {'DAI/USDC': 0.2},
    'DAI/USDC': {'BTC/USDC': 0.2},
    'BTC/USDC': {}
}
heuristik_kasus1 = {
    'ETH/USDT': 0.6,
    'USDT/DAI': 0.4,
    'DAI/USDC': 0.2,
    'BTC/USDC': 0.0
}

# Kasus Uji 2: 10 Simpul
graf_kasus2 = {
    'ETH/USDT': {'USDT/DAI': 0.3, 'ETH/DAI': 0.4, 'ETH/BTC': 0.3},
    'USDT/DAI': {'DAI/USDC': 0.2, 'USDT/BTC': 0.3},
    'DAI/USDC': {'BTC/USDC': 0.3, 'USDC/ETH': 0.2},
    'BTC/USDC': {'BTC/DAI': 0.3},
    'ETH/BTC': {'BTC/USDC': 0.2, 'USDT/BTC': 0.3},
    'USDT/BTC': {'USDT/DAI': 0.3, 'DAI/BTC': 0.4},
    'ETH/DAI': {'ETH/USDT': 0.4, 'DAI/USDC': 0.3},
    'USDC/ETH': {'ETH/BTC': 0.3},
    'BTC/DAI': {'DAI/USDC': 0.3},
    'DAI/BTC': {'BTC/USDC': 0.3}
}
heuristik_kasus2 = {
    'ETH/USDT': 0.5, 'USDT/DAI': 0.5, 'DAI/USDC': 0.3, 'BTC/USDC': 0.0,
    'ETH/BTC': 0.2, 'USDT/BTC': 0.5, 'ETH/DAI': 0.6, 'USDC/ETH': 0.5,
    'BTC/DAI': 0.6, 'DAI/BTC': 0.3
}

# Kasus Uji 3: 15 Simpul
graf_kasus3 = {
    'ETH/USDT': {'USDT/DAI': 0.3, 'ETH/DAI': 0.4, 'ETH/BTC': 0.3, 'ETH/LINK': 0.3},
    'USDT/DAI': {'DAI/USDC': 0.2, 'USDT/BTC': 0.3, 'USDT/LINK': 0.3},
    'DAI/USDC': {'BTC/USDC': 0.3, 'USDC/ETH': 0.2, 'LINK/USDC': 0.3},
    'BTC/USDC': {'BTC/DAI': 0.3},
    'ETH/BTC': {'BTC/USDC': 0.2, 'USDT/BTC': 0.3, 'BTC/LINK': 0.3},
    'USDT/BTC': {'USDT/DAI': 0.3, 'DAI/BTC': 0.4},
    'ETH/DAI': {'ETH/USDT': 0.4, 'DAI/USDC': 0.3},
    'USDC/ETH': {'ETH/BTC': 0.3},
    'BTC/DAI': {'DAI/USDC': 0.3},
    'DAI/BTC': {'BTC/USDC': 0.3},
    'ETH/LINK': {'USDT/LINK': 0.3, 'LINK/USDC': 0.3},
    'USDT/LINK': {'USDT/DAI': 0.3, 'BTC/LINK': 0.3},
    'BTC/LINK': {'LINK/USDC': 0.3},
    'LINK/USDC': {'BTC/USDC': 0.3},
    'ETH/BNB': {'ETH/USDT': 0.4}
}
heuristik_kasus3 = {
    'ETH/USDT': 0.5, 'USDT/DAI': 0.5, 'DAI/USDC': 0.3, 'BTC/USDC': 0.0,
    'ETH/BTC': 0.2, 'USDT/BTC': 0.5, 'ETH/DAI': 0.6, 'USDC/ETH': 0.5,
    'BTC/DAI': 0.6, 'DAI/BTC': 0.3, 'ETH/LINK': 0.6, 'USDT/LINK': 0.6,
    'BTC/LINK': 0.3, 'LINK/USDC': 0.3, 'ETH/BNB': 0.7
}

# Jalankan eksperimen untuk semua kasus uji
daftar_kasus = [
    ('Kasus Uji 1 (4 Simpul)', graf_kasus1, heuristik_kasus1, 'ETH/USDT', 'BTC/USDC'),
    ('Kasus Uji 2 (10 Simpul)', graf_kasus2, heuristik_kasus2, 'ETH/USDT', 'BTC/USDC'),
    ('Kasus Uji 3 (15 Simpul)', graf_kasus3, heuristik_kasus3, 'ETH/USDT', 'BTC/USDC')
]
algoritma = ['Dijkstra', 'A*', 'Greedy']

for nama_kasus, graf, heuristik, awal, tujuan in daftar_kasus:
    print(f"\n--- {nama_kasus} ---")
    for algo in algoritma:
        hasil = jalankan_eksperimen(graf, awal, tujuan, heuristik, algo, nama_kasus)
        print(f"\nHasil {algo}:")
        print(f"  Biaya: {hasil['biaya']:.3f}%")
        print(f"  Jalur: {' -> '.join(hasil['jalur'])}")
        print(f"  Waktu Eksekusi: {hasil['waktu']:.6f} detik")
        print(f"  Iterasi: {hasil['iterasi']}")