def delima(i, sum1, sum2, A):
    if i == len(A):
        return abs(sum1 - sum2)
    return min(delima(i+1, sum1 + A[i], sum2,A), delima(i + 1, sum1, sum2 + A[i], A))

i=0
sum1 = 0
sum2 = 0
N = int(input())
A = list(map(int, input().split()))
print(delima(i, sum1, sum2, A))