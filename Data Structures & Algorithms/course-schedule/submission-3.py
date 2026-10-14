class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a,b] b -> a
        # 0 to numCourses - 1
        # Return true if possible to finish all courses else false

        # We can keep track of the number of pre-requisites per course
        # So once we process a course, we can then update the count of all the courses that depend on this course
        # When its eqwual to 0 we can then process this coruse
        # To detect a cycle we can keep track of the completed courses. If the numebr of completed courses isnt equal to teh number o courtses then we can return False
        
        graph = defaultdict(list)
        indegrees = [0] * (numCourses)

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1
        
        queue = deque()
        
        for course_num in range(len(indegrees)):
            if indegrees[course_num] == 0:
                queue.append(course_num)
        
        coursesCompleted = 0
        while queue:
            course = queue.popleft()
            coursesCompleted += 1
            for neighbor in graph[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return True if coursesCompleted == numCourses else False


