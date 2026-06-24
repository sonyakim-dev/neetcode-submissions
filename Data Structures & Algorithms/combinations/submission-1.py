class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(i, fixed):
            if len(fixed) == k:
                result.append(fixed)
                return
            if i > n: return

            for j in range(i, n + 1):
                dfs(j + 1, fixed + [j])

        dfs(1, [])
        return result