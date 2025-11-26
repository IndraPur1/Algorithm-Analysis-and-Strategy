def dfsRekursif(graph, start, visited):
    if start in visited:
        return
    print(start, end=' ')
    visited.add(start)
    for neighbor in graph[start]:
        dfsRekursif(graph, neighbor, visited)
        
def dfsRekursif_multigraph(graph):
    visited = set()
    component = 1
    for node in graph:
        if node not in visited:
            print(f"\nKomponen {component}: ", end='')
            dfsRekursif(graph, node, visited)
            component += 1

    
graph = {
    "ANI": ["BUDI"],
    "BUDI": ["ANI", "CACA", "DINA"],
    "CACA": ["BUDI", "DINA"],
    "DINA": ["CACA", "BUDI"],
    "FIKRI": ["GINA"],
    "GINA": ["FIKRI", "HENDRA"],
    "HENDRA": ["GINA"],
}

dfsRekursif_multigraph(graph)