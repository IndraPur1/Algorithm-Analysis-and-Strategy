
def menara(basis, pangkat, mod):
    hasil = 1
    while pangkat > 0:
        if pangkat % 2 == 1:  
            hasil = (hasil * basis) % mod
        basis = (basis * basis) % mod  
        pangkat //= 2
    return hasil

def f(x, y, mod):
    if mod == 1:
        return 0
    
    if y == 0:
        return 1
    else:
        return menara(x, f(x, y - 1, mod), mod)  

A, B, M = map(int, input().split())

print(f(A, B, M))