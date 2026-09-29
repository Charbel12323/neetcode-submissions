class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegress = [0] * numCourses
        preReq_course = defaultdict(list)

        for course, prerequisite in prerequisites:
            indegress[course] += 1
            preReq_course[prerequisite].append(course)
        
        queue = deque()

        for course in range(len(indegress)):
            if indegress[course] == 0:
                queue.append(course)

        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1

            for neighbour in preReq_course[course]:
                indegress[neighbour] -= 1
                if indegress[neighbour] == 0:
                    queue.append(neighbour)
        
        return completed == numCourses

