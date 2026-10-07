class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        total = 0
        heap = [(0, 0)]
        visited = set()
        n = len(points)
        while len(visited) < n:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)
            total += cost

            x1,y1 = points[node]

            for nei in range(n):
                if nei not in visited:
                    x2,y2 = points[nei]

                    distance = abs(x1 - x2) + abs(y1 - y2)

                    heapq.heappush(heap, (distance, nei))
            
        return total