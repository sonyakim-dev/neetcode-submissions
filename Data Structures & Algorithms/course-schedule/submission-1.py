class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detection
        prereq = [[] for n in range(numCourses)]
        visited = set()
        for a, b in prerequisites:
            prereq[a].append(b)

        def dfs(i):
            if i in visited: return False
            if prereq[i] == []: return True

            visited.add(i)
            for c in prereq[i]:
                if not dfs(c): return False
            visited.remove(i)
            prereq[i] = []
            return True

        for n in range(numCourses):
            if not dfs(n): return False
        return True