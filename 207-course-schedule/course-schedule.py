class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """ 
        prereq = [ai , bi]
        u must take bi to take ai
        meaning bi is the pre req for ai
        numcourses = 2
        1 , [0]
        0 , [1]
        we implement topological sort and if the len order and num courses fdoesnt match we return false
        """
        # create the graph
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        for course , pre in prerequisites:
            graph[pre].append(course)
            incoming[course]+=1
        queue = deque()
        order = []
        for course in range(numCourses):
            if incoming[course] == 0:
               queue.append(course)
        while queue:
            source = queue.popleft()
            order.append(source)
            for neighbour in graph[source]:
                incoming[neighbour]-=1
                if incoming[neighbour] == 0:
                    queue.append(neighbour)
        return len(order) == numCourses