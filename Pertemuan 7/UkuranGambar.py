from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree(nodes):
    if not nodes or nodes[0] == "null":
        return None
    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        if i < len(nodes) and nodes[i] != "null":
            node.left = TreeNode(int(nodes[i]))
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] != "null":
            node.right = TreeNode(int(nodes[i]))
            queue.append(node.right)
        i += 1
    return root

def largest_values_per_level(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_max = float('-inf')
        for _ in range(level_size):
            node = queue.popleft()
            level_max = max(level_max, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_max)
    return result

n = int(input())
nodes = input().split()
root = construct_binary_tree(nodes)
result = largest_values_per_level(root)
print(" ".join(map(str, result)))