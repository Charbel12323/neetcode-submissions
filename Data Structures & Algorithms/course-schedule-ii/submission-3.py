class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
        
        results = []
        while queue:
            course = queue.popleft()
            results.append(course)
            for neighbour in graph[course]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    queue.append(neighbour)
        
        return results if len(results) == len(indegrees) else []