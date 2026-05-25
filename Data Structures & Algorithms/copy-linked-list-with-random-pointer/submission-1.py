"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = dict() # key: val, val: Node

        def dfs(curr):
            if not curr: return None
            if curr in nodes:
                return nodes[curr]

            copy = Node(curr.val)
            nodes[curr] = copy

            copy.next = dfs(curr.next)
            copy.random = nodes.get(curr.random)

            return copy

        return dfs(head)