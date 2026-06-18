class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_val, curr_count = nums[0], 0
        for n in nums:
            if curr_val == n:
                curr_count += 1
            else:
                curr_count -= 1
                
            if curr_count < 0:
                curr_val = n
                curr_count = 1
        return curr_val