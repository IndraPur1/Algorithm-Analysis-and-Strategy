def pena():
    results = []
    for i in range(1, N + 1):
        visited = [0] * (N + 1)
        current = i
        while True:
            visited[current] += 1
            if visited[current] == 2:
                results.append(current)
                break
            current = P[current - 1]
    return results

N = int(input())
P = list(map(int, input().split()))
print(*pena())