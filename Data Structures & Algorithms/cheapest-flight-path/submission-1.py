class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v,w))
        
        heap = [(0, src, 0)]

        best = {} # {}
        while heap:
            cost, node, edges = heapq.heappop(heap)

            if node == dst:
                return cost
            
            if edges == k + 1:
                continue
            
            if (node, edges) in best and best[(node,edges)] < cost:
                continue

            for nei, price in graph[node]:

                if (
                    (nei, edges + 1) not in best
                    or price + cost < best[(nei, edges + 1)]
                ):
                    best[(nei, edges + 1)] = price + cost
                
                heapq.heappush(
                    heap,
                    (cost + price, nei, edges + 1)
                )
        
        return -1



            

        