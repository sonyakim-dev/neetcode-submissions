class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            i = (l + r) // 2
            result = min(result, nums[i])
            if nums[i] >= nums[l]:
                l = i + 1
            else:
                r = i - 1

        return result