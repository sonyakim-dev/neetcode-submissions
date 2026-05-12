class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        s = sorted(count.items(), key = lambda x: x[1], reverse = True)
        return [val for val, _ in s[:k]]

        