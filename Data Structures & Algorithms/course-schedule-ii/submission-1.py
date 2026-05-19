class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort
        prereq = defaultdict(list)
        visited = [0] * numCourses # 0: not visited, -1: visited, 1: solved
        result = []
        for c, p in prerequisites:
            prereq[c].append(p)
        
        def dfs(i):
            if visited[i] == -1: return False # cycle detected
            if visited[i] == 1: return True

            visited[i] = -1
            for p in prereq[i]:
                if not dfs(p): return False
            visited[i] = 1
            result.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return result
            