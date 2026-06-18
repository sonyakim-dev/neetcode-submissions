class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size # [1, 1, 1, 1]

        pre = 1
        for i in range(size):
            result[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(size-1, -1, -1):
            result[i] *= post
            post *= nums[i]
        
        return result