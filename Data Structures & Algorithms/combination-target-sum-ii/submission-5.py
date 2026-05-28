class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(i, fixed, target):
            if target == 0:
                result.append(fixed.copy())
                return
            if i >= len(candidates) or target < 0:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if target - candidates[j] < 0:
                    break
                dfs(j + 1, fixed + [candidates[j]], target - candidates[j])

        dfs(0, [], target)
        return result