"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)

        heap = []

        for i in range(len(intervals)):
            current = intervals[i]
            
            if heap and current.start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, current.end)
        
        return len(heap)