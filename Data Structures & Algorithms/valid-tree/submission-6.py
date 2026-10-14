class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited_nodes = {0}

        queue = deque([0])

        while queue:
            node = queue.popleft()


            for neighbor in graph[node]:
                if neighbor not in visited_nodes:
                    visited_nodes.add(neighbor)
                    queue.append(neighbor)
        
        return True if len(visited_nodes) == n else False