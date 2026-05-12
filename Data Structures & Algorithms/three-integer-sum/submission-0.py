class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num: continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = num + nums[l] + nums[r]
                if s == 0:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return result