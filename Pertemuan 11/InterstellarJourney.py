def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

def union(parent, rank, x, y):
    px = find(parent, x)
    py = find(parent, y)
    if px != py:
        # Union by rank
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1

def min_warp_cost(N, M, Q, A, relations, journey):
    # Initialize Union-Find
    parent = list(range(N + 1))  # 1-based indexing
    rank = [0] * (N + 1)
    
    # Process relations to build connected components
    for b, c in relations:
        union(parent, rank, b, c)
    
    # Find the minimum warp cost for each component
    min_cost = [float('inf')] * (N + 1)  # Min cost for each component
    for i in range(1, N + 1):
        root = find(parent, i)
        min_cost[root] = min(min_cost[root], A[i - 1])
    
    # Calculate total cost for the journey
    total_cost = 0
    for i in range(Q - 1):
        planet1 = journey[i]
        planet2 = journey[i + 1]
        root1 = find(parent, planet1)
        root2 = find(parent, planet2)
        if root1 != root2:
            total_cost += min_cost[root1] + min_cost[root2]
    
    return total_cost

# Read input
N, M, Q = map(int, input().split())
A = list(map(int, input().split()))
relations = []
for _ in range(M):
    b, c = map(int, input().split())
    relations.append((b, c))
journey = list(map(int, input().split()))

# Print result
print(min_warp_cost(N, M, Q, A, relations, journey))