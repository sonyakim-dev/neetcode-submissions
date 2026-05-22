"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = dict() # key: number, val: Node

        def dfs(node):
            if node.val in clone:
                return clone[node.val]

            new_node = Node(node.val)
            clone[node.val] = new_node
            for neigh in node.neighbors:
                new_node.neighbors.append(dfs(neigh))
            return new_node

        return dfs(node) if node else None