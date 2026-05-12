class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curr_min, curr_max = 1, 1

        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1
            
            curr_min, curr_max = min(n * curr_min, n * curr_max, n), max(n * curr_min, n * curr_max, n)
            result = max(result, curr_min, curr_max)
        
        return result