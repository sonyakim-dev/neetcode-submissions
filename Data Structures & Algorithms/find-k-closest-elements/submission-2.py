class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = [] # (|val - x|, val)
        for n in arr:
            heapq.heappush(h, (-(abs(x - n)), -n))
            if len(h) > k:
                heapq.heappop(h)

        return sorted([-val for _, val in h])