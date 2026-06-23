class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a > 0: h.append((-a, 'a'))
        if b > 0: h.append((-b, 'b'))
        if c > 0: h.append((-c, 'c'))
        heapq.heapify(h)
        result = ''

        while h:
            c, v = heapq.heappop(h)
            if len(result) >= 2 and result[-2] == result[-1] == v:
                if not h: break
                c2, v2 = heapq.heappop(h)
                result += v2
                if c2 + 1 < 0:
                    heapq.heappush(h, (c2 + 1, v2))
                heapq.heappush(h, (c, v))
            else:
                result += v
                if c + 1 < 0:
                    heapq.heappush(h, (c + 1, v))

        return result
