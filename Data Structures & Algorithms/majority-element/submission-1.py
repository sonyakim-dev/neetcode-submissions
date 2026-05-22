class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) / 2
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1
            if counter[n] > maj: return n