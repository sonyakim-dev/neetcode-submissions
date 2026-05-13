class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles) == h, return max val
        # 0 <= k <= max(piles)
        l, r = 1, max(piles)
        result = r
        
        while l <= r:
            k = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            
            if time <= h:
                result = k
                r = k -1
            else:
                l = k + 1
        return result