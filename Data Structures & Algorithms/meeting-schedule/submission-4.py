"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            prev_s, prev_e = intervals[i-1].start, intervals[i-1].end
            s, e = intervals[i].start, intervals[i].end
            if s < prev_e: return False
        return True