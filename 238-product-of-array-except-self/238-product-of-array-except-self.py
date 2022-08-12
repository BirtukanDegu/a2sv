class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        n = len(nums)
        result = [0 for i in range(n)]
        result[0]=1
        a = 1
        for i in range(1,n):
            a = a *nums[i-1]
            result[i] = a
        a = 1
        for i in range(n-2,-1,-1):
            a = a * nums[i+1]
            result[i] = result[i]*a
        return result
      