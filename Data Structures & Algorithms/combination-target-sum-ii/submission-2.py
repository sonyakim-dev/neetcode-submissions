class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        unique combination, chosen at most once
        """
        candidates.sort()
        result = []

        def dfs(i, fixed, target):
            if target == 0:
                result.append(fixed.copy())
                return
            if target < 0 or i >= len(candidates):
                return
            num = candidates[i]
            dfs(i + 1, fixed + [num], target - num)
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, fixed, target)

        dfs(0, [], target)
        return result