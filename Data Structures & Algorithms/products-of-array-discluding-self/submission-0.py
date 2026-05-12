class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size

        for i in range(1, size):
            result[i] = nums[i-1] * result[i-1]
        
        postfix = nums[-1]
        for i in range(size-2, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result