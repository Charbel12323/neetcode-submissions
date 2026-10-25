class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        numberOfConnected = 0

        def bfs(node):
            queue = deque([node])
            visited.add(node)

            while queue:
                node = queue.popleft()
                
                for nei in graph[node]:
                    if nei in visited:
                        continue
                    
                    visited.add(nei)
                    queue.append(nei)
                
        for node in range(n):
            if node in visited:
                continue
            
            bfs(node)
            numberOfConnected += 1
        
        return numberOfConnected