class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals are already non overlapping, no need ot sort
        # we would need to track some sort of start time and end time
        # if the starting time is less than the new intervals' start time, we can merge that start time together
        # if the start time is greater than the end time, the new intervals end time is less than the next intervals start time we can insert right there since its in ascending order

        
        # conditon check to see if the new interval fits in interval i
        # check to see if the end time is less than the next intervals start time, if so, we can insert it there

        newStart, newEnd = newInterval[0], newInterval[1]
        inserted = False

        result = []
        for start, end in intervals:
            if end < newStart:
                result.append([start, end])
            elif newEnd < start:
                if not inserted:
                    result.append([newStart, newEnd])
                    inserted = True
                result.append([start, end])
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        
        if not inserted:
            result.append([newStart, newEnd])
        
        return result
        



