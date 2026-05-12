class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what is a valid tree? all connected each other, no cycle
        if len(edges) > (n - 1): return False

        tr = [[] for _ in range(n)] # i: num, val: children
        visited = set()

        for n1, n2 in edges:
            tr[n1].append(n2)
            tr[n2].append(n1)

        def dfs(node, prev):
            if node in visited: # cycle detected
                return False
            visited.add(node)
            for c in tr[node]:
                if c == prev:
                    continue
                if not dfs(c, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n