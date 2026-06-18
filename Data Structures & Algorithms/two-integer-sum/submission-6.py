class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        return two indicies
        must have exactly one pair, return the smaller index
        """
        ## Hashmap
        search = dict() # key: target - num, value: index
        for i, n in enumerate(nums):
            if target - n in search:
                return [search[target - n], i]
            search[n] = i