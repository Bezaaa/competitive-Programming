class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        order = []

        for course , pre in prerequisites:
            graph[pre].append(course)
            incoming[course] +=1
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            order.append(course)
            for neigh in graph[course]:
                incoming[neigh]-=1
                if incoming[neigh] == 0:
                    queue.append(neigh)
        return order if len(order) == numCourses else []

        
        
        