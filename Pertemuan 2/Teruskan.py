def teruskan(A, X, i = 0):
    if i >= len(A):
        return '"Tidak ditemukan"'
    elif A[i] == X:
        return i
    else:
        return teruskan(A, X, i + 1)

A = eval(input().strip())
X = int(input().strip()) 
print(teruskan(A, X))