class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        if size < 4: return []

        result = []
        nums.sort()

        for i in range(size - 3):
            if i > 0 and nums[i] == nums[i-1]: continue

            for j in range(i + 1, size - 2):
                if j > i + 1 and nums[j] == nums[j-1]: continue

                l, r = j + 1, size - 1
                while l < r:
                    sum4 = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum4 > target:
                        r -= 1
                    elif sum4 < target:
                        l += 1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1

        return result