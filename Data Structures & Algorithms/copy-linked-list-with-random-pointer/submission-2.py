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
        ## DFS

        # nodes = dict() # key: orig Node, val: copy Node
        # def dfs(curr):
        #     if not curr: return None
        #     if curr in nodes:
        #         return nodes[curr]

        #     copy = Node(curr.val)
        #     nodes[curr] = copy

        #     copy.next = dfs(curr.next)
        #     copy.random = nodes.get(curr.random)

        #     return copy

        # return dfs(head)


        ## One Pass
        nodes = defaultdict(lambda: Node(0))
        nodes[None] = None
        curr = head

        while curr:
            nodes[curr].val = curr.val
            nodes[curr].next = nodes[curr.next]
            nodes[curr].random = nodes[curr.random]
            curr = curr.next
        return nodes[head]