
import heapq

# Graph and heuristic definition
graph = {
    's': {'a': 6, 'd': 3},
    'a': {'b': 5, 's': 6},
    'b': {'c': 4, 'a': 5},
    'c': {'b': 4},
    'd': {'s': 3, 'e': 2},
    'e': {'d': 2, 'f': 4},
    'f': {'e': 4, 'g': 3},
    'g': {'f': 3}
}

heuristic = {
    's': 12,
    'a': 8,
    'd': 9,
    'b': 7,
    'c': 5,
    'e': 4,
    'f': 2,
    'g': 0
}

# Greedy Best First Search
def greedy_search(graph, start, goal):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    path = []

    while pq:
        h, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        path.append(current)

        if current == goal:
            return path

        for neighbor in graph.get(current, {}):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    return None

# A* Search
def a_star_search(graph, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))  # (f, g, current, path)
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor, cost in graph.get(current, {}).items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None

# Run both searches
start_node = 's'
goal_node = 'g'

greedy_result = greedy_search(graph, start_node, goal_node)
a_star_result = a_star_search(graph, start_node, goal_node)

print("Greedy Best First Search Path:", greedy_result)
print("A* Search Path:", a_star_result)