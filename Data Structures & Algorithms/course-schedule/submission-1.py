class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegress = [0] * numCourses
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegress[course] += 1
        
        queue = deque()

        for course in range(numCourses):
            if indegress[course] == 0:
                queue.append(course)
        
        complete = 0
        while queue:
            course = queue.popleft()
            complete += 1

            for neighbor in graph[course]:
                indegress[neighbor] -= 1
                if indegress[neighbor] == 0:
                    queue.append(neighbor)
            
        return complete == numCourses