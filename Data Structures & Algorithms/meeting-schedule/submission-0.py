"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda a: a.start)
        # print([(i.start, i.end) for i in intervals])
        prevEnd = 0
        for i in intervals:
            if i.start < prevEnd:
                return False
            prevEnd = i.end
        return True