def Noxus(penduduk, kiri, kanan):
    if kiri == kanan:
        return penduduk[kiri]
    
    mid = (kiri + kanan) // 2
    rakyatkiri = Noxus(penduduk, kiri, mid)
    rakyatkanan = Noxus(penduduk, mid + 1, kanan)

    if rakyatkiri == rakyatkanan:
        return rakyatkiri

    countkiri = sum(1 for i in range(kiri, kanan + 1) if penduduk[i] == rakyatkiri)
    countkanan = sum(1 for i in range(kiri, kanan + 1) if penduduk[i] == rakyatkanan)

    if countkiri > (kanan - kiri + 1) // 2:
        return rakyatkiri
    elif countkanan > (kanan - kiri + 1) // 2:
        return rakyatkanan
    else:
        return -1

n = int(input())
penduduk = list(map(int, input().split()))

print(Noxus(penduduk, 0, n - 1))