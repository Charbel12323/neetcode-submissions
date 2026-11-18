class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited_set = set()
        graph = defaultdict(list)
        numberOfConnected = 0
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for node in range(n):
            if node in visited_set:
                continue
            
            queue = deque([node])
            while queue:
                current_node = queue.popleft()
                visited_set.add(current_node)
                for neighbour in graph[current_node]:
                    if neighbour in visited_set:
                        continue
                    
                    queue.append(neighbour)
            
            numberOfConnected += 1
        
        return numberOfConnected
            
