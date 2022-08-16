class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n=len(questions)
        profit=[0]*n
        rightmax=[0]*n
        profit[-1]=questions[-1][0]
        rightmax[-1]=profit[-1]
        for i in range(n-1,-1,-1):
            profit[i]=questions[i][0]
            nextindex=i+questions[i][1]+1
            if nextindex<n:
                profit[i]+=rightmax[nextindex]
            if i!=n-1:
                rightmax[i]=max(rightmax[i+1],profit[i])
        return rightmax[0]