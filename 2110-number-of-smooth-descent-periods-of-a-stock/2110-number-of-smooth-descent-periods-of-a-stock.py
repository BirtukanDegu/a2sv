class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lastPrice = None
        counter = 0
        seen = 0
        
        for price in prices:
            if lastPrice and lastPrice - price == 1:
                counter += 1 + seen
                seen += 1
            else:
                seen = 0
                
            counter += 1
            lastPrice = price
            
        return counter
            