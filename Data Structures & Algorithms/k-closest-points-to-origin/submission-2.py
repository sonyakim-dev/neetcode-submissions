class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [] # (dis, x, y)
        for x, y in points:
            heapq.heappush(h, (-(x ** 2 + y ** 2), x, y))
            if len(h) > k:
                heapq.heappop(h)
        return [[x, y] for _, x, y in h]