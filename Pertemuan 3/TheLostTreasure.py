def Treasure(S, kiri, kanan):
    if kiri == kanan:
        return S[kiri]
    
    mid = (kiri + kanan) // 2

    maxkiri = Treasure(S, kiri, mid)
    maxkanan = Treasure(S, mid + 1, kanan)

    if maxkiri > maxkanan:
        return maxkiri
    else:
        return maxkanan
    
n = int(input())
S = list(map(int, input().split()))

print(Treasure(S, 0, n - 1))