class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hist = set()
        for n in nums:
            if n in hist: return True
            hist.add(n)
        return False