class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        result = 0

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            visited[node] = True
            for n in adj[node]:
                if not visited[n]:
                    visited[n] = True
                    dfs(n)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                result += 1
            
        return result