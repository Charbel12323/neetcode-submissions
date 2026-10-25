class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Minimum time to reach n nodes from the singal source
        There are multiple paths to each node, where each path might have a different time
        Our brute force is to try all those paths but since we are porcoessing each node more than once O(V+E ^ 2)
        Better solution is if we can process each node once by getting the shorted distance almost immediately
        # We can use a min heap to store the shorted distance we current have to each nod and whatever node we proces is guaranteed to have ths horted distsnace
        """

        visited = set()
        min_heap = [(0,k)]
        time = 0
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w)) # Directed
        
        while min_heap:
            time_taken, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited.add(node)
            time = time_taken
            
            for nei, weight in graph[node]:
                heapq.heappush(min_heap, (time_taken + weight, nei))
        
        return time if len(visited) == n else -1

        
