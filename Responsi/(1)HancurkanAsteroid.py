def asteroid():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    max_sumxy = float('-inf')
    max_x = 0
    max_y = 0

    for i in range(N):
        for j in range(M):
            current_sum = sum(A[i]) + sum(A[k][j] for k in range(N)) - A[i][j]
            if current_sum > max_sumxy:
                max_sumxy = current_sum
                max_x = i
                max_y = j
            elif current_sum == max_sumxy:
                if max_x > i:
                    max_x = min(max_x, i)
                    max_y = j
                elif max_x == i:
                    max_x = max_x
                    max_y = min(max_y, i)
                    
    print( max_y, (N - 1 - max_x), max_sumxy)

asteroid()