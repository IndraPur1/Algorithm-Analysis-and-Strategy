def bentengluffy(N, S, A):
    if S == 0:
        return '"Luffy Kalah"'
    elif S > N:
        return '"Banyaknya benteng tidak cukup dengan yang dibutuhkan"'
    else:
        maxsum = float('-inf')
        currentsum = 0
        for i in range(S):
            currentsum += A[i]
        maxsum = currentsum
        for i in range(S, N):
            currentsum += A[i] - A[i - S]
            maxsum = max(maxsum, currentsum)
        return maxsum

N = int(input())
S = int(input())
A = [int(x) for x in input().split(',')]

print(bentengluffy(N, S, A))