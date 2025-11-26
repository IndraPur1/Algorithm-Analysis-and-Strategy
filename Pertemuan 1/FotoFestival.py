def foto_festival_terbaik():
    N, M = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]

    best_quality = float('-inf')
    best_size = 0
    best_x, best_y = 0, 0

    for size in range(1, min(N, M) + 1): 
        for i in range(N - size + 1):
            for j in range(M - size + 1): 
                quality = sum(A[x][y] for x in range(i, i + size) for y in range(j, j + size))

                if (quality > best_quality or
                    (quality == best_quality and size > best_size) or
                    (quality == best_quality and size == best_size and i < best_x) or
                    (quality == best_quality and size == best_size and i == best_x and j < best_y)):
                    best_quality = quality
                    best_size = size
                    best_x, best_y = i, j

    print(best_quality, best_size, best_x + 1, best_y + 1)


foto_festival_terbaik()