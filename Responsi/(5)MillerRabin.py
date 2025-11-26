# Fungsi untuk mengecek apakah suatu bilangan n adalah prima menggunakan Algoritma Miller-Rabin
def is_prime(n, k=5):
    # 1. Menangani kasus khusus
    if n <= 1:  # Jika n ≤ 1, maka bukan bilangan prima
        return False
    if n in (2, 3):  # Jika n = 2 atau 3, maka pasti bilangan prima
        return True
    if n % 2 == 0:  # Jika n genap selain 2, maka pasti bukan prima
        return False

    # 2. Tulis n - 1 sebagai 2^s * d, dengan d ganjil
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # 3. Pilih basis uji coba (bilangan prima kecil yang sering digunakan)
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # 4. Lakukan uji Miller-Rabin sebanyak k kali
    for i in range(min(k, len(bases))):
        if bases[i] >= n:  # Jika basis lebih besar dari n, lewati
            continue
        
        # Hitung x = (basis[i] ** d) % n
        x = pow(bases[i], d, n)  

        # Jika x = 1 atau x = n - 1, lanjut ke iterasi berikutnya
        if x == 1 or x == n - 1:
            continue  

        # Ulangi pemeriksaan s - 1 kali untuk melihat apakah x berubah menjadi n - 1
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:  
                break  # Jika x = n - 1, lanjut ke basis berikutnya
        else:
            return False  # Jika tidak pernah mencapai n - 1, maka bukan prima

    return True  # Jika lulus semua uji coba, kemungkinan besar prima

# Input jumlah bilangan yang akan diuji
n = int(input())

# Uji setiap bilangan dan cetak hasilnya
for _ in range(n):
    number = int(input())
    print("Prima" if is_prime(number) else "Komposit")
