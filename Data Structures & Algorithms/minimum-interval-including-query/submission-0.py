import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by start
        intervals.sort()

        # Will store:
        # (interval_length, interval_end)
        heap = []

        # Store answer for each query
        answer = {}

        i = 0

        # Process queries from smallest to largest
        for query in sorted(queries):

            # Add every interval that has started by this query
            while i < len(intervals) and intervals[i][0] <= query:
                start = intervals[i][0]
                end = intervals[i][1]

                length = end - start + 1

                heapq.heappush(heap, (length, end))

                i += 1

            # Remove intervals that cannot contain this query anymore
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            # The shortest valid interval is at the top
            if heap:
                answer[query] = heap[0][0]
            else:
                answer[query] = -1

        # Put answers back in original query order
        return [answer[query] for query in queries]