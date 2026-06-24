class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(i, fixed):
            result.append(fixed)
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                dfs(j + 1, fixed + [nums[j]])
        
        dfs(0, [])
        return result