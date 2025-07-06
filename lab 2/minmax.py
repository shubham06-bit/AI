# Minimax Algorithm Implementation

def minimax(node, depth, is_maximizing, tree):
    # Base case: if we reach a leaf node, return its value
    if node not in tree:
        return node

    # Maximizing player's turn
    if is_maximizing:
        best = float('-inf')
        for child in tree[node]:
            val = minimax(child, depth + 1, False, tree)
            best = max(best, val)
        return best
    # Minimizing player's turn
    else:
        best = float('inf')
        for child in tree[node]:
            val = minimax(child, depth + 1, True, tree)
            best = min(best, val)
        return best

# Tree based on the image
# Leaf nodes replaced with integer values
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [2, 4],     # H, I
    'E': [6, 9],     # J, K
    'F': [1, 2],     # L, N
    'G': [7, 5]      # R, S
}

# Start Minimax from root 'A' as maximizing player
result = minimax('A', 0, True, tree)
print("The optimal value is:", result)