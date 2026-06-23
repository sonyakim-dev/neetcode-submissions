class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, fixed, total):
            if total == target:
                result.append(fixed)
                return
            for j in range(i, len(nums)):
                if total + nums[j] <= target:
                    dfs(j, fixed + [nums[j]], total + nums[j])

        dfs(0, [], 0)
        return result