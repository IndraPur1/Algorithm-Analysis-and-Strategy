def hitung_kekuatan_total(pasukan):
    return sum(pasukan)

def pasukan(A):
    evenly = []
    oddlings = []
    
    for x in A:
        if x % 2 == 0:
            evenly.append(x)
        else:
            oddlings.append(x)

    total_evenly = hitung_kekuatan_total(evenly)
    total_oddlings = hitung_kekuatan_total(oddlings)

    if total_oddlings <= 0 and total_evenly <= 0:
        print("Kedua pasukan sudah musnah")
    elif total_oddlings > total_evenly:
        print("Oddlings menang!")
        print(*oddlings)
        print(total_oddlings)
    elif total_evenly > total_oddlings:
        print("Evenly menang!")
        print(*evenly)
        print(total_evenly)
    elif total_oddlings == total_evenly and total_oddlings > 0:
        print("Kedua pasukan damai!")
        print(*(evenly + oddlings))
        print(total_evenly + total_oddlings)
    else:
        print("Kedua pasukan sudah musnah")

N = int(input().strip())
A = list(map(int, input().split()))

pasukan(A)