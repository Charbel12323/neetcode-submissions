class MedianFinder:

    def __init__(self):
        self.left_side = []
        self.right_side = []

        heapq.heapify(self.left_side)
        heapq.heapify(self.right_side)
    def addNum(self, num: int) -> None:

        if not self.left_side or num <= -self.left_side[0]:
            heapq.heappush(self.left_side, -num)
        else:
            heapq.heappush(self.right_side, num)

        # Left side can only have one value greater

        if (len(self.left_side) - len(self.right_side)) > 1: 
            value = -heapq.heappop(self.left_side)
            heapq.heappush(self.right_side, value)
        
        elif len(self.left_side) < len(self.right_side):
            value = heapq.heappop(self.right_side)
            heapq.heappush(self.left_side, -value)
        

        

    def findMedian(self) -> float:
        # We can have a min heap and a max heap
        # The left side stores the smaller values using a max_heap
        # The right side stores the bigger values using the min_heap
        # We must keep 1 extra value on the left
        # We use. min_heap on the right to pop the left most element on the right side
        # We use a max_heap on the left to pop the biggest value on the right side

        total = len(self.left_side) + len(self.right_side)

        if total % 2 == 0:
            return (-self.left_side[0] + self.right_side[0]) / 2
        
        return -self.left_side[0]