class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result=0
        piles.sort()
        n = len(piles)
        for i in range(n//3,n, 2):
            result+=piles[i]
           
        return result
