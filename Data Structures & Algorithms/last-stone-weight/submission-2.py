class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if x < y:
                heapq.heappush(max_heap, -(y-x))
            else:
                continue
        
        return -(max_heap[0]) if max_heap else 0
