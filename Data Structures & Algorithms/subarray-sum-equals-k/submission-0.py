class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        acc = 0
        result = 0

        for n in nums:
            acc += n
            if acc - k in prefix:
                result += prefix[acc - k]
            prefix[acc] += 1
        
        return result