class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            h.append((math.sqrt(x ** 2 + y ** 2), x, y))
        heapq.heapify(h)
        
        result = []
        for i in range(k):
            d, x, y = heapq.heappop(h)
            result.append([x, y])

        return result