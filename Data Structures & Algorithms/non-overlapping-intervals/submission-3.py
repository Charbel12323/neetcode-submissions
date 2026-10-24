class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Return the minimum number of intervals I need to remove to keep the most non overlapping intervals still there

        """
        The input is not sorted
        Is it safe to assume that the intervals array will never be empty
        Are intervals overlapping ifprev end and curretn start are equal. No they are not

        intervals = [[1,2],[1,10], [2,4]]
        # Clearly if we remove teh interval with the shorted ending time, it would lead to more overlapping problems.

        We should sort by the end time. 
        intervals = [1,2],[2,4],[1,10]
        """

        intervals.sort(key=lambda x:x[1])

        count = 0
        prev_end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] < prev_end:
                count += 1
            else:
                prev_end = interval[1]

        return count