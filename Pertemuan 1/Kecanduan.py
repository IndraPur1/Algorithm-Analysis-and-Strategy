def kecanduan(A, K):
    for i in range(len(A)):
        if A[i] == K:
            return i
    return '"Tidak ditemukan"'

input_str = input().strip('[]')
if input_str:
    A = [int(x) for x in input_str.split(',')]
else:
    A = []

K = int(input())

print(kecanduan(A, K))