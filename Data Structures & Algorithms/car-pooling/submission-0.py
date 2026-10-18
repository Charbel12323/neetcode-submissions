
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort trips by starting location
        trips.sort(key=lambda trip: trip[1])

        # Min heap storing (end_location, passengers)
        min_heap = []
        passengers = 0

        for count, start, end in trips:

            # Remove passengers from completed trips
            while min_heap and min_heap[0][0] <= start:
                end_prev, count_prev = heapq.heappop(min_heap)
                passengers -= count_prev

            # Add passengers from the current trip
            passengers += count

            # Check total occupancy
            if passengers > capacity:
                return False

            # Track when these passengers will exit
            heapq.heappush(min_heap, (end, count))

        return True
