class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 <= k <= max(piles) -->> binary search
        l, r = 1, max(piles)
        time = r

        while l <= r:
            m = (l + r) // 2
            temp = 0
            for p in piles:
                temp += math.ceil(p / m)
            if temp > h: # koko needs to eat more!!
                l = m + 1
            else:
                time = m
                r = m - 1
        return time