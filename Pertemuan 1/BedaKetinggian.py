def bedaketinggian(A):
    list = []

    list.append(A[0])

    for i in range(1,len(A)-1):
        if (A[i-1] <= A[i] and A[i+1] <= A[i]) or (A[i-1] >= A[i] and A[i+1] >= A[i]):
            list.append(A[i])

    list.append(A[len(A)-1])

    maxim = 0

    for i in range(len(list)-1):
        maxim = max(maxim, abs(list[i] - list[i+1]))
    
    return maxim

N = int(input())
A = list(map(int, input().split()))

print(bedaketinggian(A))