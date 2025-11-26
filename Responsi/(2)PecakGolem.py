def ValidPermutasi(arr):
    for i in range (1, len(arr) - 1):
        if not ((arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1])):
            return False
    return True
    
def Permutasi(index):
    if len(index) == 0:
        return [[]]
    permutasi = []
    for i in range (len(index)):
        sisa = index[:i] + index[i+1:]
        for p in Permutasi(sisa):
            permutasi.append([index[i]] + p)
    return permutasi

def Golem(N):
    index = [str(i) for i in range (1, N+1)]
    AllPermutasi =  Permutasi(index)
    Valid = []
    for arr in AllPermutasi:
        if ValidPermutasi(arr):
            Valid.append(''.join(arr))
    return Valid

N = int(input().strip())

konfigurasi = Golem(N)
for config in konfigurasi:
    print(config)