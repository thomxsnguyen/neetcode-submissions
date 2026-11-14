class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        # [1,3],
        # [1,5],
        # [6,7]]
        output = [intervals[0]]

        for start, end in intervals:
            prevEnd = output[-1][1]

            if start <= prevEnd:
                output[-1][1] = max(prevEnd, end)
            else:
                output.append([start, end])
        
        return output
            