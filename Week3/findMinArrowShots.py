class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        points.sort(key = lambda x: x[0])
        nArrows = 0
        last_end = points[0][1]
        
        for left, right in points:
            if last_end < left:
                nArrows += 1
                last_end = right
            else:
                last_end = min(last_end, right)
            
        return nArrows + 1