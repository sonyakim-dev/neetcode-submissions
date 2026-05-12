class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = dict() # key: num, value: index
        for i, n in enumerate(nums):
            if target - n in hist:
                return [hist[target - n], i]
            hist[n] = i
        
        # T.C: O(n), S.C: O(n)