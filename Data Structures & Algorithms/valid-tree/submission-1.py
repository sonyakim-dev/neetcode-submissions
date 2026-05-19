class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what is a valid tree? no cycle, all connected
        tree = defaultdict(list)
        visited = set()
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs(i, prev):
            if i in visited: return False
            visited.add(i)
            for neigh in tree[i]:
                if neigh == prev: continue
                if not dfs(neigh, i): return False
            return True

        return dfs(0, -1) and len(visited) == n