"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        h = [] # occupied room; (end, start)
        result = 0

        for inter in intervals:
            s, e = inter.start, inter.end
            while h and h[0][0] <= s:
                heapq.heappop(h)

            heapq.heappush(h, (e, s))
            result = max(result, len(h))
            
        return result