class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## DP - bottom-up
        ## T.C: O(n^2)
        size = len(nums)
        dp = [1] * size

        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
            