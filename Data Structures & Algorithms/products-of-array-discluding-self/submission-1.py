class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre: [1, 1, 2, 8]
        # post: [48, 24, 6, 1]
        size = len(nums)
        result = [1] * size

        # calc prefix
        pre = 1
        for i in range(size):
            result[i] = pre
            pre *= nums[i]
        
        # calc postfix
        post = 1
        for i in range(size-1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result

        # T.C: O(n), S.C: O(n)