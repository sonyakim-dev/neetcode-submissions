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
        h = [] # min heap; store end time
        rooms = 0

        for inter in intervals:
            if h and h[0] <= inter.start:
                heapq.heappop(h)
            heapq.heappush(h, inter.end)

        return len(h)