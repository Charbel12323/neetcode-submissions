class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        What makes a valid tree
        - No cycles
        - Fully connected

        How do we figure out if there are cycle
        IN a tree, the number of edges must be exactlly n - 1. If it is greater that means there is a cycle

        Now how do we figure out if its connected or not
        We can build an adjaceny list
        We can iterate through it once
        If everything was found then were good if not then it is not connected
        Time Compelxiry = O(V + E)
        Space = O(V+E)
        """

        if len(edges) != n - 1: # Detects cycles for us
            return False

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        nodesVisited = set()
        nodesVisited.add(0)
        queue =deque([0])

        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                if neighbour not in nodesVisited:
                    nodesVisited.add(neighbour)
                    queue.append(neighbour)
        

            
        return True if len(nodesVisited) == n else False
            