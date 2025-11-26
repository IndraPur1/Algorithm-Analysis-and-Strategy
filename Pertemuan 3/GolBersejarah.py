def GolBersejarah(N, awal=0, akhir=31):
    if awal == akhir:
        return (akhir >> awal) & 1

    mid = (awal + akhir) // 2
    
    left_count = GolBersejarah(N, awal, mid)
    right_count = GolBersejarah(N, mid + 1, akhir)
    return left_count + right_count

N = int(input())
print(GolBersejarah(N))