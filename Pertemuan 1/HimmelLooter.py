def looter(A):
    maxcurr = maxglobal = A[0]
    for i in range (len(A)):
        maxcurr = max(A[i], maxcurr + A[i])
        if maxcurr > maxglobal:
            maxglobal = maxcurr
    return maxglobal

N = int(input())
A = [int(x) for x in input().split()]

print(looter(A))