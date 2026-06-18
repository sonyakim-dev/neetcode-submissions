class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0

        for n in nums:
            if n - 1 not in nums:
                curr = n
                while curr + 1 in nums:
                    curr += 1
                result = max(result, curr - n + 1)

        return result