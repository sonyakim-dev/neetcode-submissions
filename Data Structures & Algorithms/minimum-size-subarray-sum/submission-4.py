class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        curr_sum = 0
        l = 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                result = min(result, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return result if result != len(nums) + 1 else 0