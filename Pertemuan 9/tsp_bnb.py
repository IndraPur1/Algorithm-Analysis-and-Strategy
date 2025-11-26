import sys
from queue import PriorityQueue

# Define the number of vertices and infinity value
N = 4
INF = sys.maxsize

# Node class to store each node along with the cost, level, and vertex
class Node:
    def __init__(self, parentMatrix, path, level, i, j):
        self.path = path.copy()
        self.reducedMatrix = [row.copy() for row in parentMatrix]
        self.cost = 0
        self.vertex = j
        self.level = level

        # Add this edge to the path
        if level != 0:
            self.path.append((i, j))

        # Change all entries of row i and column j to infinity
        # Also change the entry for vertex k to infinity
        if level != 0:
            for k in range(N):
                self.reducedMatrix[i][k] = INF
                self.reducedMatrix[k][j] = INF
            self.reducedMatrix[j][0] = INF
    def __lt__(self, other):
        return self.cost < other.cost
# Function to perform row reduction
def rowReduction(reducedMatrix):
    row = [INF]*N

    # Row[i] contains minimum in row i
    for i in range(N):
        for j in range(N):
            if reducedMatrix[i][j] < row[i]:
                row[i] = reducedMatrix[i][j]

    # Reduce the minimum value from each element in each row
    for i in range(N):
        for j in range(N):
            if reducedMatrix[i][j] != INF and row[i] != INF:
                reducedMatrix[i][j] -= row[i]

    return row

# Function to perform column reduction
def columnReduction(reducedMatrix):
    col = [INF]*N

    # Col[j] contains minimum in col j
    for i in range(N):
        for j in range(N):
            if reducedMatrix[i][j] < col[j]:
                col[j] = reducedMatrix[i][j]

    # Reduce the minimum value from each element in each column
    for i in range(N):
        for j in range(N):
            if reducedMatrix[i][j] != INF and col[j] != INF:
                reducedMatrix[i][j] -= col[j]

    return col

# Function to calculate the cost of the path
def calculateCost(reducedMatrix):
    cost = 0
    row = rowReduction(reducedMatrix)
    col = columnReduction(reducedMatrix)

    # Calculate the cost by adding the reduction values
    for i in range(N):
        cost += (row[i] if row[i] != INF else 0)
        cost += (col[i] if col[i] != INF else 0)

    return cost

# Function to print the path
def printPath(path):
    for pair in path:
        print(f"{pair[0] + 1} -> {pair[1] + 1}")

# Function to solve the TSP problem
def solve(CostGraphMatrix):
    # Create a priority queue to store live nodes of the search tree
    pq = PriorityQueue()

    # Create a root node and calculate its cost
    root = Node(CostGraphMatrix, [], 0, -1, 0)
    root.cost = calculateCost(root.reducedMatrix)

    # Add root to the list of live nodes
    pq.put((root.cost, root))

    # Continue until the priority queue becomes empty
    while not pq.empty():
        # Find a live node with the least estimated cost
        min = pq.get()[1]

        # Get the vertex number
        i = min.vertex

        # If all the cities have been visited
        if min.level == N - 1:
            min.path.append((i, 0))
            printPath(min.path)
            return min.cost

        # Generate all the children of min
        for j in range(N):
            if min.reducedMatrix[i][j] != INF:
                child = Node(min.reducedMatrix, min.path, min.level + 1, i, j)
                child.cost = min.cost + min.reducedMatrix[i][j] + calculateCost(child.reducedMatrix)
                pq.put((child.cost, child))

    return 0

# Define the cost matrix
CostGraphMatrix = [
    [ INF, 10, 15, 20 ],
    [ 10, INF, 35, 25 ],
    [ 15, 35, INF, 30 ],
    [ 20, 25, 30, INF ]
]

# Print the total cost of the tour
print("Total cost is", solve(CostGraphMatrix))