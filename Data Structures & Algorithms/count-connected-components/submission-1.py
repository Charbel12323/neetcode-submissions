class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        connectedGraphs = 0
        visited = set()

        def dfs(node):
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                connectedGraphs += 1
        
        return connectedGraphs