class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DAG problem
        prereq = defaultdict(list) # key: course, val: prereqs
        visited = set()
        for c, p in prerequisites:
            prereq[c].append(p)

        def dfs(course):
            if course in visited:
                return False
            if prereq[course] == []:
                return True

            visited.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            prereq[course] = [] # remove all the connected course since it can be completed
            return True
        
        for n in range(numCourses):
            if not dfs(n): return False
        return True