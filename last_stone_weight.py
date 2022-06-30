class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)-1):
            stones.sort()                             
            stones[-2] = abs(stones[-2] - stones[-1]) 
            stones.pop()                              
        return stones[0] 
