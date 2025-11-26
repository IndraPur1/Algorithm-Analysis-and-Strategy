def koinasing(A):
    for i in range(len(A)):
        if A.count(A[i]) == 1:
            return i + 1
    return '"Tidak ditemukan"'

A = list(input())

print(koinasing(A))

# AAABAAAA
# A B A

# YXXX
# Y X X