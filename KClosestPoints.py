class Solution:
    def distance(self , x , y):
        return ((x**2) + (y**2)) ** 0.5
    
    def copyArray(self , arr):
        an = []
        for i in arr:
            an.append(i)
        return an
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for point in points:
            distance.append(self.distance(point[0] , point[1]))
        
        ans = self.copyArray(distance)
        distance.sort()
        realAns = []
        for i in range(k):
            realAns.append(points[ans.index(distance[i])])
        
        return realAns
            
