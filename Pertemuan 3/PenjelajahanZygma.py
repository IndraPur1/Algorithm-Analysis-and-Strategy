def zygma(N, arr):
    data = []
    for i in range(N):
        data.append((arr[i], i))
    
    data.sort()

    selisih_terkecil = abs(data[1][0] - data[0][0])
    indeks_awal_terkecil = min(data[0][1], data[1][1]) + 1

    for i in range(1, N - 1):
        nilai1, indeks1 = data[i]
        nilai2, indeks2 = data[i + 1]
        selisih = abs(nilai2 - nilai1)
        indeks_terkecil_input = min(indeks1, indeks2) + 1

        if selisih < selisih_terkecil:
            selisih_terkecil = selisih
            indeks_awal_terkecil = indeks_terkecil_input
        elif selisih == selisih_terkecil:
            if indeks_terkecil_input < indeks_awal_terkecil:
                indeks_awal_terkecil = indeks_terkecil_input
    print(selisih_terkecil, indeks_awal_terkecil)

N = int(input())
arr = list(map(int, input().split()))

zygma(N, arr)