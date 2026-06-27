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
        h = [] # occupied room; (end)
        rooms = 0

        for inter in intervals:
            while h and h[0] <= inter.start:
                heapq.heappop(h)

            heapq.heappush(h, inter.end)
            rooms = max(rooms, len(h))
            
        return rooms