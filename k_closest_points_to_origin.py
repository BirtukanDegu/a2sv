class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res=[]
        d={}
        for i in points:
            d[math.sqrt((i[0]**2)+(i[1]**2))]=d.get(math.sqrt((i[0]**2)+(i[1]**2)),[])+[i]
        sorted_d=sorted(d.keys())
        for i in sorted_d[:K]:
            if len(res)<K:
                res.extend(d[i])
            else:break
        return res
