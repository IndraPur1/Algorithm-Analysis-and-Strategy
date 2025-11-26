def SubsBaik(S):
    if len(S) < 2:
        return ""
    
    unik = set(S)

    for i in range (len(S)):
        char = S[i]
        if char.swapcase() not in unik:
            kiri = SubsBaik(S[:i])
            kanan = SubsBaik(S[i + 1:])
            return kiri if len(kiri) >= len(kanan) else kanan
    return S

S = input()
print(SubsBaik(S))