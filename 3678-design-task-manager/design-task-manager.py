import heapq

class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.heap = [] 
        self.task_map = {}  

        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (priority, userId)
            heapq.heappush(self.heap, (-priority, -taskId, userId, taskId))

    def add(self, userId, taskId, priority):
        self.task_map[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId, userId, taskId))

    def edit(self, taskId, newPriority):
        userId = self.task_map[taskId][1]
        self.task_map[taskId] = (newPriority, userId)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId, taskId))

    def rmv(self, taskId):
        if taskId in self.task_map:
            del self.task_map[taskId]
            

    def execTop(self):
        while self.heap:
            priority, neg_taskId, userId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map:
                current_priority, current_user = self.task_map[taskId]
              
                if current_priority == -priority and current_user == userId:
                    del self.task_map[taskId]
                    return userId
        return -1
