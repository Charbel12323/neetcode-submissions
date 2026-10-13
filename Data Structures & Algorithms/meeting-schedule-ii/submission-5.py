"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        max_count = 0

        for interval in intervals:

            while min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, interval.end)
            max_count = max(max_count, len(min_heap))
        
        return max_count
            
