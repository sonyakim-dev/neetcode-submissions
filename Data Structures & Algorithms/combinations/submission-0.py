class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(i, fixed):
            if len(fixed) == k:
                result.append(fixed)
                return
            if i > n:
                return
                
            dfs(i + 1, fixed + [i])
            dfs(i + 1, fixed)

        dfs(1, [])
        return result