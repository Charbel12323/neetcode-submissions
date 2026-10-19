class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We have dependencies
        # Each course can have multiple dependencies
        # Therefore we can build an ajency list
        # Where each node is the course pre req and its neighbours are the courses that depend on it
        # We can only process courses with 0 pre-requisites
        # So we have to get the count of pre requisuites
        # We put them all in a queue and start procesing. Each time we process a pre requ
        # We check its neighbours and if it has any then we can reduce the pre rew and count if its 0 then we can add it to the queue
        # SO to finish all courses we need to keep track of all the courses that we have completed. Once we keep track of them we can then check if they are equal to numCourses
        
        preReqCount = [0] * numCourses

        graph = defaultdict(list) # pre-req : [courses that depend on the prereq]

        # A directed graph
        for course, preReq in prerequisites:
            graph[preReq].append(course)
            preReqCount[course] += 1
        
        queue = deque()

        for course in range(len(preReqCount)):
            if preReqCount[course] == 0:
                queue.append(course)
        
        course_completed = set()

        while queue:
            course = queue.popleft()

            
            course_completed.add(course)
            
            for neighbour in graph[course]:
                preReqCount[neighbour] -= 1
                if preReqCount[neighbour] == 0:
                    if neighbour not in course_completed:
                        queue.append(neighbour)
        
        return True if len(course_completed) == numCourses else False
            

