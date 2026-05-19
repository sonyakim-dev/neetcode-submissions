class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        count = 0
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(i):
            visited.add(i)
            for neigh in graph[i]:
                if neigh not in visited:
                    dfs(neigh)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count