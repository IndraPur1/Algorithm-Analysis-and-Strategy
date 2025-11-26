def dfs(i, j, n, m, grid, visited):
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0
    if grid[i][j] == '#' or visited[i][j]:
        return 0
    
    visited[i][j] = True
    
    count = 1 if grid[i][j] == 'A' else 0
    count += dfs(i-1, j, n, m, grid, visited)  
    count += dfs(i+1, j, n, m, grid, visited)  
    count += dfs(i, j-1, n, m, grid, visited)  
    count += dfs(i, j+1, n, m, grid, visited)  
    return count

def Start(grid, n, m):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'Y':
                return i, j
    return -1, -1

def artefak(n, m, grid):
    visited = [[False for x in range(m)] for y in range(n)]
    X, Y = Start(grid, n, m)
    return dfs(X, Y, n, m, grid, visited)

n, m = map(int, input().split())
grid = []
for i in range(n):
    row = input()
    if ' ' in row:
        row = row.split()
    else:
        row = list(row)
    grid.append(row)

print(artefak(n, m, grid))