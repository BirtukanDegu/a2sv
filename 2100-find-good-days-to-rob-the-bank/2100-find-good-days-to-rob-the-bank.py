class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        n = len(security)   
        
        left = [0] * n # consecutive non-increasing
        right = [0] * n # consecutive non-decreasing
        
        for i in range(1, n):
            if security[i-1] >= security[i]:
                left[i] = left[i-1] + 1
            if security[n-i-1] <= security[n-i]:
                right[n-i-1] = right[n-i] + 1
                
        result = []
        for i in range(n):
            if(left[i] >= time and right[i] >= time):
                result.append(i)

        return result