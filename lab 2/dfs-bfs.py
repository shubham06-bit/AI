# Define the graph as an adjacency list
graph = {
    '1': ['2', '7', '8'],
    '2': ['3', '6'],
    '3': ['4', '5'],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': ['9', '12'],
    '9': ['10', '11'],
    '10': [],
    '11': [],
    '12': []
}

# DFS Iterative Function
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    print("DFS Traversal:", end=' ')
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Add children in reverse to maintain left-to-right traversal
            stack.extend(reversed(graph[node]))

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = [start]
    print("\nBFS Traversal:", end=' ')
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

# Main Execution
if __name__ == "__main__":
    start_node = '1'  # Make sure this matches a key in the graph
    dfs_iterative(graph, start_node)
    bfs(graph, start_node)
