class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        if N % 2 == 0: return True # can always win by picking larger one of odd or even subarray
        
		# DP
        dp = nums[:]
        for i in range(1, N):
            for j in range(N - i):
                dp[j] = max(nums[j] - dp[j + 1], nums[j + i] - dp[j])
        
        return dp[0] >= 0