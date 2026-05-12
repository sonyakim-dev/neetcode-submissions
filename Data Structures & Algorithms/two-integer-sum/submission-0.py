class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub = dict() # key: num, value: index
        for i, n in enumerate(nums):
            if target - n in sub: return [sub[target - n], i]
            sub[n] = i