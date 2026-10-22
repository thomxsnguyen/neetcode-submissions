"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the intervals by start time
        # intialize a start end time from the first interval create a min character
        # while iterating through the intervals, compare the end time to see if its shorter, if so return false, otherwise return true

        
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True
        
        