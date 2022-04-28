#import math
#from array import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        newarray = []
        for i in range(len(points)):
            newarray.append(points[i][0]**2 + points[i][-1]**2)
        newar = sorted(newarray)
        newar2 = newar[:k]
        maximum = newar2[k-1]
        newarray2 = []
        for j in range(len(points)):
            if (points[j][0]**2 + points[j][1]**2)<=maximum:
                newarray2.append(points[j])
        newarray3 = newarray2[:k]
        return newarray3
