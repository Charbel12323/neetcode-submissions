class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        for u, v,w in times:
            adj[u].append((v,w))
        
        heap = [(0, k)]
        visited_set = set()
        t = 0

        while heap:
            time, node = heapq.heappop(heap)
            
            if node in visited_set:
                continue
            
            visited_set.add(node)

            t = time
            for nei, w in adj[node]:
                if nei not in visited_set:
                    heapq.heappush(heap, (time + w, nei))
        
        return t if len(visited_set) == n else -1
            

