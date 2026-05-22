class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detection
        prereq = defaultdict(list)
        visited = set()
        for c, p in prerequisites:
            prereq[c].append(p)

        def dfs(i):
            if i in visited: return False
            if prereq[i] == []: return True

            visited.add(i)
            for pre in prereq[i]:
                if not dfs(pre): return False
            visited.remove(i)
            prereq[i] = [] # remove all the connected course since it can be completed
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True