class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # must loaded in order -->> sum of subarray
        # if len(weights) == days: return max(weights)
        # max(weights) <= cap <= sum(weights) -->> binary search
        l, r = max(weights), sum(weights)
        result = r

        def canShip(cap):
            ships, curr = 1, cap
            for w in weights:
                if w > curr:
                    ships += 1
                    curr = cap
                curr -= w
            return ships <= days

        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1

        return result