class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix, postfix
        size = len(nums)
        result = [1] * len(nums)

        pre = 1
        for i in range(size):
            result[i] = pre
            pre *= nums[i]
        # [1, 1, 2, 8]

        post = 1
        for i in range(size-1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result