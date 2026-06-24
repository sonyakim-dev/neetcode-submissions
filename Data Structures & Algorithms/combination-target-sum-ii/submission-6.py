class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # [1, 2, 2, 4, 5, 6, 9]
        result = []

        def dfs(i, fixed, total):
            if total == target:
                result.append(fixed)
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr = candidates[j]
                if total + curr <= target:
                    dfs(j + 1, fixed + [curr], total + curr)

        dfs(0, [], 0)
        return result