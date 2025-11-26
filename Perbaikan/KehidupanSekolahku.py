# Daftar kode morse untuk huruf A-Z (index 0 = A, index 1 = B, dst.)
morse = [
  '.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
  '....', '..', '.---', '-.-', '.-..', '--', '-.',
  '---', '.--.', '--.-', '.-.', '...', '-', '..-',
  '...-', '.--', '-..-', '-.--', '--..'
]

# Ubah list morse menjadi set untuk pencarian cepat
kode_set = set(morse)

# Dictionary untuk menyimpan hasil sementara (memoization)
memo = {}

# Fungsi utama untuk menghitung kemungkinan pemecahan string morse menjadi huruf
def hitung_kemungkinan(s):
    # Basis: jika string kosong, berarti sudah terbentuk kombinasi yang valid
    if s == "":
        return 1

    # Jika hasil untuk string s sudah dihitung sebelumnya, langsung kembalikan
    if s in memo:
        return memo[s]

    res = 0  # Inisialisasi hasil
    # Coba ambil potongan dari panjang 1 sampai 4 (maksimal panjang kode morse huruf adalah 4)
    for i in range(1, 5):
        if i <= len(s):
            potong = s[:i]  # Ambil potongan awal sepanjang i
            if potong in kode_set:  # Cek apakah potongan adalah kode morse valid
                # Lanjutkan dengan sisa string, dan tambahkan hasilnya
                res += hitung_kemungkinan(s[i:])
    
    # Simpan hasil ke memo agar tidak dihitung ulang
    memo[s] = res
    return res

# Input string morse tanpa spasi
s = input().strip()

# Cetak jumlah kemungkinan pemecahan string menjadi huruf
print(hitung_kemungkinan(s))
