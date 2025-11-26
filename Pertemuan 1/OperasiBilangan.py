def operasibilangan(A):
    P = 0
    if len(A) % 2 == 0:
        for i in range(len(A)):
            P += A[i]
    else:
        for i in range(len(A) // 2):
            P = P + A[i]
        t = int(i + 1)
        for j in range(t+1,len(A)):
            P = P + A[j]
        P = P * A[t]
    return P

A = [int(x) for x in input().split()]

print(operasibilangan(A))