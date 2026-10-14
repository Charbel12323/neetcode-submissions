class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited_set = set()
        number_connected = 0

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for node in range(n):
            if node not in visited_set:
                queue = deque([node])
                visited_set.add(node)

                while queue:
                    curr = queue.popleft()

                    for neighbor in graph[curr]:
                        if neighbor not in visited_set:
                            visited_set.add(neighbor)
                            queue.append(neighbor)
                
                number_connected += 1
        
        return number_connected