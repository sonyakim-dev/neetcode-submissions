class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1

        for i, n in enumerate(nums):
            if last < i: break
            if n == val:
                while 0 <= i < last and nums[last] == val:
                    last -= 1
                nums[i] = nums[last]
                last -= 1
        print(nums)
        return last + 1