class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        numberOfConnected = 0
        visited_set = set()
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(node):
            queue = deque([node])
            visited_set.add(node)

            while queue:
                vertex = queue.popleft()

                for nei in graph[vertex]:
                    if nei not in visited_set:
                        visited_set.add(nei)
                        queue.append(nei)
        


        
        for i in range(n):
            if i not in visited_set:
                bfs(i)
                numberOfConnected += 1
        
        return numberOfConnected
        
