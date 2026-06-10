class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        visited = set()
        for c, p in prerequisites:
            prereq[c].append(p)
        
        def dfs(course):
            if course in visited:
                return False
            if prereq[course] == []:
                return True

            visited.add(course)
            for p in prereq[course]:
                if not dfs(p): return False
            visited.remove(course)
            prereq[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True