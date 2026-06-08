class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        for a in arr:
            heapq.heappush(h, (-(abs(a - x)), -a))
            if len(h) > k:
                heapq.heappop(h)
        return sorted([-(h[i][1]) for i in range(k)])