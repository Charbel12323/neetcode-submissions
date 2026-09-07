class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, target, visited):
            if node == target:
                return True
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited: # We dont want an infinite loop
                    if dfs(neighbor, target, visited):
                        return True  

        for a,b in edges:
            if dfs(a,b, set()):
                return [a,b]
            
            graph[a].append(b)
            graph[b].append(a)