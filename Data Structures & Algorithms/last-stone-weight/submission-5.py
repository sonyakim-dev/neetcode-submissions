class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        
        while len(h) > 1:
            x, y = -heapq.heappop(h), -heapq.heappop(h)
            if x == y: continue
            heapq.heappush(h, -(max(x, y) - min(x, y)))

        return -h[0] if h else 0