class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # course b -> course a  [a,b]
        # im given a total number of courses
        # Return a valid order of me completing my courses
        # cant finish -> []
        
        # 1 course -> multiple pre-requisites
        # [1,1] -> Not possible
        # numCourses = 3 0 -> 1. not all courses have pre requisites
        # [0,1][1,2] 1 -> 0  2 -> 1 2->0
        # We can represnt the course as a node and its pre requiestes as its neighbours. and the edges will be directed edge from b -> a
        # Since we care about the ordering, we need to use topological sort
        # Every single course can eitehr have pre requiestes or no pre requiestes
        # indegress = [0] * numCourses 
        
        # for a, b in prerequisiutes:
            # graph[b].append(a)
            # pre_req_count[a] += 1
        
        # queue = deque[] # To store all teh coruses without any pre-reqs
        # for i in range(1, n + 1):
            # if i not in pre_req_count:
                # queue.append(i)
        
        # completed = 0
        
        # Were going to process all the courses without an pre-req
        # {course: list of courses that depend on this course}
        # whiel queue:
            # Process without pre -rews

        # Go traverse through our adjency list hashmap accordingly
        # while queue:
        #   0
        # append it results
        # for neighbor in grpah[course]:
        # update hashmap count decrementing
        # once its equal to 0 we add it the queue
        #

        indegrees = [0] * numCourses
        graph =  defaultdict(list) # {course: the list of courses that depend on this course}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
        
        queue = deque()

        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
            
        results = []

        while queue:
            course = queue.popleft()
            results.append(course)

            for neighbor in graph[course]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return results if len(results) == numCourses else []
        
        # Time Complexity = O(C + P)
        # Space complexity = O(C + P)

