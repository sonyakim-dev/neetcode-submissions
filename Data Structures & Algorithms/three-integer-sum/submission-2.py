class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if an el is neg, needs pos, if an el is pos, needs neg
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        result = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]: continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] + n > 0:
                    r -= 1
                elif nums[l] + nums[r] + n < 0:
                    l += 1
                else:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return result