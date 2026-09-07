class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses # How many dependencies each course has
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
        
        queue = deque()
        
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
        
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []
