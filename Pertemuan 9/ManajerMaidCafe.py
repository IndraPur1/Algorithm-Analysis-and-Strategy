class Node:
    def __init__(self, level, penugasan, cost):
        self.level = level
        self.penugasan = penugasan
        self.cost = cost
        self.bound = 0

def hitungBound(node, n, cost_matrix, belum_ditugaskan):
    batas_bawah = node.cost

    for i in range(node.level + 1, n):
        min_cost = float('inf')
        for j in belum_ditugaskan:
            if cost_matrix[i][j] < min_cost:
                min_cost = cost_matrix[i][j]
        batas_bawah += min_cost

    return batas_bawah

def penugasanBranchAndBound(cost_matrix, n):
    if n == 1:
        return cost_matrix[0][0]

    antrian = []

    root = Node(-1, [], 0)
    belum_ditugaskan = list(range(n))
    root.bound = hitungBound(root, n, cost_matrix, belum_ditugaskan)
    antrian.append(root)

    min_cost = float('inf')

    while antrian:
        antrian.sort(key=lambda x: x.bound)
        node_sekarang = antrian.pop(0)

        if node_sekarang.bound >= min_cost:
            continue

        level = node_sekarang.level + 1

        for j in range(n):
            if j not in node_sekarang.penugasan:
                penugasan_baru = node_sekarang.penugasan + [j]
                cost_baru = node_sekarang.cost + cost_matrix[level][j]

                if level == n - 1:
                    if cost_baru < min_cost:
                        min_cost = cost_baru
                else:
                    node_baru = Node(level, penugasan_baru, cost_baru)
                    belum_ditugaskan = [x for x in range(n) if x not in penugasan_baru]
                    node_baru.bound = hitungBound(node_baru, n, cost_matrix, belum_ditugaskan)
                    antrian.append(node_baru)

    return min_cost

n = int(input())
cost_matrix = []

for _ in range(n):
    baris = list(map(int, input().split()))
    cost_matrix.append(baris)

hasil = penugasanBranchAndBound(cost_matrix, n)
print(hasil)