class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # number of neg values should be even
        # track both min and max since once we enter the big neg while curr min in neg,
        # it comes a big pos number
        # edge case; when enter 0, reset min and max
        result = max(nums)
        curr_min, curr_max = 1, 1

        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1

            curr_min, curr_max = min(n, n * curr_min, n * curr_max), max(n, n * curr_min, n * curr_max)
            result = max(result, curr_min, curr_max)

        return result