class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        h = [] # (dest, passenger)
        curr = 0

        for p, s, e in trips:
            while h and h[0][0] <= s:
                curr -= heapq.heappop(h)[1]

            curr += p
            if curr > capacity:
                return False
            
            heapq.heappush(h, (e, p))

        return True
