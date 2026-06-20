class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [2, 10, 30, 30, 30, 30]
        #     lr
        record = set([nums[0]])
        l, r = 1, 1
        while r < len(nums):
            while r < len(nums) and nums[r] in record:
                r += 1
            if r >= len(nums): break
            nums[l] = nums[r]
            record.add(nums[r])
            l += 1
            r += 1
        return l