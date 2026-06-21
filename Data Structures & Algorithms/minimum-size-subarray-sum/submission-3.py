class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [0, 2, 3, 8, 9, 14, 17]
        #  l  r
        nums = [0] + nums
        result = len(nums)
        l = 0
        for r in range(1, len(nums)):
            nums[r] += nums[r-1]

            while nums[r] - nums[l] >= target:
                result = min(result, r - l)
                l += 1

        return result if result != len(nums) else 0