class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 <= k <= max(piles)
        l, r = 1, max(piles)
        result = r

        if h == len(piles):
            return r

        while l <= r:
            m = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / m)

            if time > h:
                l = m + 1
            else:
                result = m
                r = m - 1

        return result