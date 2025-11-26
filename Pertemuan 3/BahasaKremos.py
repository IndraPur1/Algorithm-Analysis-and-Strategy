def Kremos(a, b):
    if a == b:
        return True
    
    if len(a) % 2 == 1:
        return a == b
    
    mid = len(a) // 2
    a1 = a[:mid]
    a2 = a[mid:]
    b1 = b[:mid]
    b2 = b[mid:]

    equivalen1 = Kremos(a1, b1) and Kremos(a2, b2)
    equivalen2 = Kremos(a1, b2) and Kremos(a2, b1)

    return equivalen1 or equivalen2

a = input().strip()
b = input().strip()

if Kremos(a, b):
    print("YA")
else:
    print("TIDAK")