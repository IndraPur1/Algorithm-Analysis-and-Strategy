import heapq
import math

def euclidean_distance(p1, p2):
    lat1, lon1 = p1
    lat2, lon2 = p2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def a_star(start, goal, graph, city_coords):
    open_set = [(euclidean_distance(city_coords[start], city_coords[goal]), 0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, weight in graph.get(current, []):
            tentative_g = current_g + weight
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + euclidean_distance(city_coords[neighbor], city_coords[goal])
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    return None

# Koordinat setiap kota
city_coords = {
    'A': (1.0, 1.0),
    'B': (1.0, 2.0),
    'C': (2.0, 2.0),
    'D': (3.0, 2.0),
    'E': (2.0, 1.0)
}

# Representasi graf (graph) sebagai adjacency list
graph = {
    'A': [('B', 1), ('E', 1.5)],
    'B': [('A', 1), ('C', 1.5)],
    'C': [('B', 1.5), ('D', 2)],
    'D': [('C', 2)],
    'E': [('A', 1.5), ('C', 1)],
}

start = 'A'
goal = 'D'

# Jalankan A* dan cetak jalur
path = a_star(start, goal, graph, city_coords)
print("Jalur terpendek dari {} ke {}:".format(start, goal), path)