class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > n:
                return num
