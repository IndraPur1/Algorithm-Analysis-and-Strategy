# Fungsi Qiyana untuk mencari indeks koin palsu dalam daftar koin
def Qiyana(n):
    # Menentukan jenis koin yang paling sering muncul (asumsi: koin asli adalah yang paling banyak)
    # max(set(n), key=n.count) artinya:
    # dari semua jenis koin yang unik (set), pilih yang jumlah kemunculannya paling banyak
    KoinAsli = max(set(n), key=n.count) 

    # Iterasi untuk mencari koin yang berbeda dengan KoinAsli
    for i in range(len(n)):  
        if n[i] != KoinAsli:
            # Jika ditemukan koin yang berbeda (koin palsu), langsung kembalikan indeksnya
            return i

    # Jika semua koin sama dengan koin asli, berarti tidak ada koin palsu
    return -1

# --- Input dari pengguna ---
n = int(input())                       # Input jumlah koin
n = list(map(int, input().split()))   # Input daftar jenis koin

# Cetak hasil indeks koin palsu (jika ada), jika tidak ada maka -1
print(Qiyana(n))