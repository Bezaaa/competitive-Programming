class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        min_time = 0
        for i in range(1 , len(points)):
            x , y = points[i]
            first , second = points[i-1]
            min_time+=max(abs(second - y) , abs(first -x))
        return min_time

        