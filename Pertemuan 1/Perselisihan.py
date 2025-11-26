def selisih(A):
    min = 1000000
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if abs(A[i] - A[j]) < min:
                if abs(A[i] - A[j]) == 0:
                    continue
                else:
                    min = abs(A[i] - A[j])
    return min

A = [int(x) for x in input().split()]

print(selisih(A))