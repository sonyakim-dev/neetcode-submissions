class Solution:
    def rob(self, nums: List[int]) -> int:
        ## dfs
        # if len(nums) == 1: return nums[0]
        # def dfs(i, flag):
        #     if i >= len(nums) or (flag and i == len(nums) - 1):
        #         return 0
        #     return max(dfs(i+1, flag), dfs(i+2, flag or i == 0) + nums[i])
        # return max(dfs(0, True), dfs(1, False))

        ## bottom-up
        def helper(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                rob1, rob2 = rob2, max(rob1 + n, rob2)
            return rob2
        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])

        