# Fungsi rekursif Guardians untuk menentukan apakah semua guardian bisa dilewati
def Guardians(N, P, G, index=0):
    # Basis kasus: jika semua guardian sudah dilewati (index mencapai N), maka berhasil
    if index == N:
        return "YES"
    
    # Jika kekuatan P sekarang lebih kecil dari kekuatan guardian saat ini, maka gagal
    if P < G[index]: 
        return "NO"
    
    # Jika bisa melewati guardian saat ini, tambahkan kekuatannya ke P
    # lalu lanjut ke guardian berikutnya (index + 1)
    return Guardians(N, P + G[index], G, index + 1)

# -------------------------
# Input dari pengguna:
# N = jumlah guardian
# P = kekuatan awal pemain
N, P = map(int, input().split())

# G = daftar kekuatan tiap guardian
G = list(map(int, input().split()))

# Cetak hasil apakah pemain bisa melewati semua guardian
print(Guardians(N, P, G))