class Solution:
    def reorganizeString(self, s: str) -> str:
        result = ''
        h = [(-c, v) for v, c in Counter(s).items()]
        heapq.heapify(h)
        prev = None

        while h:
            c1, v1 = heapq.heappop(h)
            c2, v2 = heapq.heappop(h) if h else (0, '')
            
            if result and result[-1] == v1:
                return ''
            result += v1 + v2

            if c1 + 1 < 0:
                heapq.heappush(h, (c1 + 1, v1))
            if c2 + 1 < 0:
                heapq.heappush(h, (c2 + 1, v2))

        return result