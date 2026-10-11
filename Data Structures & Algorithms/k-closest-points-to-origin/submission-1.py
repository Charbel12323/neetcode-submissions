class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max_heap why the mac we want the closest so in a max heap the root is always the largest value therefore wif we keep popping untill 2 remain, we can just return since its going to the be the largest. nlogn

        max_heap = []

        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(max_heap, (-distance, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [[x,y] for _, x, y in max_heap]

    