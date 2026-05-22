class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what is valid tree? all connected, no cycle
        neigh = defaultdict(list)
        visited = set()
        
        for n1, n2 in edges:
            neigh[n1].append(n2)
            neigh[n2].append(n1)
        
        # we need prev (parent node) to prevent false cycle detection
        def dfs(i, prev):
            if i in visited: return False
            visited.add(i)
            for n in neigh[i]:
                if n == prev: continue
                if not dfs(n, i): return False
            return True

        return dfs(0, -1) and len(visited) == n