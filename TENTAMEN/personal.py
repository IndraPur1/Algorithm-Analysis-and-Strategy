def cari_pembagi(n):
    pembagi = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            pembagi.append(i)
            if i != n // i:
                pembagi.append(n // i)
    return sorted(pembagi)

def cari_kombinasi_13(pembagi, target=13):
    hasil = []
    def backtrack(index, total, path):
        nonlocal hasil
        if total > target:
            return
        if total == target:
            if not hasil or path < hasil:
                hasil = path[:]
            return
        
        for i in range(index, len(pembagi)):
            backtrack(i + 1, total + pembagi[i], path + [pembagi[i]])

    backtrack(0, 0, [])
    return hasil if hasil else [-1]

t = int(input())
for _ in range(t):
    x = int(input())
    pembagi = cari_pembagi(x)
    hasil = cari_kombinasi_13(pembagi)
    print(*hasil)