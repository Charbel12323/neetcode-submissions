class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Intervals are given in sorted order

        return a new array intervals with the inserted interval
        [start, end]

        if start > end -> Add the interval
        If not, merge both intervals and try again in the next round
        Until there are no longer any intervals


        We could either merge, or just add them

        Functionality of adding them
        If start < end and end < start
        """


        results = []

        for interval in intervals:
            start_interval = interval[0]
            end_interval = interval[1]

            if end_interval < newInterval[0]:
                results.append(interval)
            
            elif start_interval > newInterval[1]:
                results.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(start_interval, newInterval[0])
                newInterval[1] = max(end_interval, newInterval[1])
        
        results.append(newInterval)

        return results                
            
            
