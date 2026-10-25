class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        visited = set()
        min_heap = [(0,0)] # Cost and node
        nodes = len(points)

        while len(visited) < nodes:
            cost, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited.add(node)
            total += cost

            x1,y1 = points[node]
            for nei in range(nodes):
                if nei not in visited:
                    x2,y2 = points[nei]

                    distance = abs(x2 - x1) + abs(y2-y1)

                    heapq.heappush(min_heap, (distance, nei))
            
        return total

